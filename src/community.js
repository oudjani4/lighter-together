(function () {
  var C = window.SITE_CONFIG || {};
  var H = { apikey: C.SUPABASE_ANON_KEY, "Content-Type": "application/json" };
  var API = C.SUPABASE_URL + "/rest/v1/";
  function el(t, c, x) { var n = document.createElement(t); if (c) n.className = c; if (x != null) n.textContent = x; return n; }
  function get(p) { return fetch(API + p, { headers: H }).then(function (r) { if (!r.ok) throw 0; return r.json(); }); }
  function post(t, b) { return fetch(API + t, { method: "POST", headers: Object.assign({ Prefer: "return=minimal" }, H), body: JSON.stringify(b) }).then(function (r) { if (!r.ok) throw 0; }); }
  function tooFast() { try { var n = Date.now(), l = +localStorage.getItem("lt_last") || 0; if (n - l < 30000) return true; localStorage.setItem("lt_last", n); } catch (e) {} return false; }
  function when(s) { return new Date(s).toLocaleDateString(); }
  function form(fields, btnText, onSubmit) {
    var f = el("form", "card"), msg = el("p", "meta"), inputs = {};
    fields.forEach(function (d) {
      var i = el(d.area ? "textarea" : "input"); i.placeholder = d.label; i.required = true;
      i.minLength = d.min; i.maxLength = d.max; if (d.area) i.rows = 4;
      inputs[d.key] = i; f.appendChild(i);
    });
    var hp = el("input"); hp.style.display = "none"; hp.tabIndex = -1; hp.autocomplete = "off"; f.appendChild(hp);
    var b = el("button", "btn", btnText); b.type = "submit"; f.appendChild(b); f.appendChild(msg);
    f.addEventListener("submit", function (e) {
      e.preventDefault(); if (hp.value) return;
      if (tooFast()) { msg.textContent = "Please wait a few seconds before posting again."; return; }
      var data = {}; for (var k in inputs) data[k] = inputs[k].value.trim();
      b.disabled = true;
      onSubmit(data).then(function () { f.reset(); msg.textContent = "Thank you! It will appear after review."; })
        .catch(function () { msg.textContent = "Something went wrong. Please try again later."; })
        .then(function () { b.disabled = false; });
    });
    return f;
  }
  function reportBtn(kind, id) {
    var a = el("button", "meta", "Report"); a.type = "button";
    a.onclick = function () { a.disabled = true; post("reports", { kind: kind, target_id: id }).then(function () { a.textContent = "Reported, thank you"; }).catch(function () { a.disabled = false; }); };
    return a;
  }
  var root = document.getElementById("ask-board");
  if (!root) return;
  root.appendChild(form([
    { key: "nickname", label: "Nickname (no real name needed)", min: 2, max: 40 },
    { key: "title", label: "Your question in one line", min: 5, max: 120 },
    { key: "body", label: "Tell us more (please do not share personal medical records)", min: 10, max: 1500, area: 1 }
  ], "Ask the community", function (d) { return post("questions", d); }));
  var list = el("div"); root.appendChild(list);
  Promise.all([
    get("questions?select=id,nickname,title,body,created_at&approved=eq.true&order=created_at.desc&limit=50"),
    get("answers?select=id,question_id,nickname,body,created_at&approved=eq.true&order=created_at.asc&limit=500")
  ]).then(function (res) {
    var qs = res[0], as = res[1];
    if (!qs.length) { list.appendChild(el("p", "meta", "No questions yet. Be the first to ask.")); return; }
    qs.forEach(function (q) {
      var c = el("article", "card");
      c.appendChild(el("h3", null, q.title));
      c.appendChild(el("p", "meta", q.nickname + " \u00b7 " + when(q.created_at)));
      c.appendChild(el("p", null, q.body));
      as.filter(function (a) { return a.question_id === q.id; }).forEach(function (a) {
        var r = el("div", "reply");
        r.appendChild(el("p", null, a.body));
        r.appendChild(el("p", "meta", a.nickname + " \u00b7 " + when(a.created_at)));
        r.appendChild(reportBtn("answer", a.id)); c.appendChild(r);
      });
      c.appendChild(form([
        { key: "nickname", label: "Nickname", min: 2, max: 40 },
        { key: "body", label: "Your reply", min: 2, max: 1500, area: 1 }
      ], "Reply", function (d) { d.question_id = q.id; return post("answers", d); }));
      c.appendChild(reportBtn("question", q.id));
      list.appendChild(c);
    });
  }).catch(function () { list.appendChild(el("p", "meta", "Could not load questions right now.")); });
})();
