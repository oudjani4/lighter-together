(function () {
  var C = window.SITE_CONFIG || {};
  var ready = C.SUPABASE_URL && C.SUPABASE_URL.indexOf("YOUR-PROJECT") === -1;
  var H = ready ? { apikey: C.SUPABASE_ANON_KEY, Authorization: "Bearer " + C.SUPABASE_ANON_KEY, "Content-Type": "application/json" } : {};

  function esc(s) {
    var d = document.createElement("div");
    d.textContent = s == null ? "" : String(s);
    return d.innerHTML;
  }

  // ---- Load approved stories ----
  var list = document.getElementById("stories");
  if (list) {
    if (!ready) {
      list.innerHTML = '<p class="meta">Community stories will appear here once the site is connected to its database.</p>';
    } else {
      fetch(C.SUPABASE_URL + "/rest/v1/stories?select=nickname,title,story,kg_lost,months,created_at&approved=eq.true&order=created_at.desc&limit=50", { headers: H })
        .then(function (r) { return r.json(); })
        .then(function (rows) {
          if (!rows.length) { list.innerHTML = '<p class="meta">No stories yet. Be the first to <a href="share-your-story.html">share yours</a>.</p>'; return; }
          list.innerHTML = rows.map(function (s) {
            var tags = "";
            if (s.kg_lost) tags += '<span class="tag">' + esc(s.kg_lost) + ' kg lost</span>';
            if (s.months) tags += '<span class="tag">' + esc(s.months) + ' months</span>';
            return '<div class="story"><h3>' + esc(s.title) + '</h3><p class="meta">by ' + esc(s.nickname) + ' · ' + new Date(s.created_at).toLocaleDateString() + '</p>' + tags + '<p>' + esc(s.story).replace(/\n/g, "<br>") + '</p></div>';
          }).join("");
        })
        .catch(function () { list.innerHTML = '<p class="meta">Could not load stories right now.</p>'; });
    }
  }

  // ---- Submit a story ----
  var form = document.getElementById("storyForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = document.getElementById("formMsg");
      msg.className = "msg";
      if (form.website && form.website.value) return; // honeypot
      if (!ready) { msg.className = "msg err"; msg.textContent = "Site database is not connected yet."; return; }
      var body = {
        nickname: form.nickname.value.trim().slice(0, 40),
        title: form.title.value.trim().slice(0, 120),
        story: form.story.value.trim().slice(0, 4000),
        kg_lost: form.kg_lost.value ? Number(form.kg_lost.value) : null,
        months: form.months.value ? Number(form.months.value) : null
      };
      if (body.story.length < 80) { msg.className = "msg err"; msg.textContent = "Please write at least 80 characters."; return; }
      var btn = form.querySelector("button");
      btn.disabled = true;
      fetch(C.SUPABASE_URL + "/rest/v1/stories", { method: "POST", headers: Object.assign({ Prefer: "return=minimal" }, H), body: JSON.stringify(body) })
        .then(function (r) {
          if (!r.ok) throw new Error();
          form.reset();
          msg.className = "msg ok";
          msg.textContent = "Thank you! Your story was submitted and will appear after review.";
        })
        .catch(function () { msg.className = "msg err"; msg.textContent = "Something went wrong. Please try again later."; })
        .finally(function () { btn.disabled = false; });
    });
  }
})();
