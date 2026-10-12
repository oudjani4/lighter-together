-- Run this once in Supabase > SQL Editor
create table if not exists public.stories (
  id bigint generated always as identity primary key,
  nickname text not null check (char_length(nickname) between 2 and 40),
  title text not null check (char_length(title) between 5 and 120),
  story text not null check (char_length(story) between 80 and 4000),
  kg_lost numeric check (kg_lost is null or (kg_lost >= 0 and kg_lost < 400)),
  months int check (months is null or (months >= 0 and months < 240)),
  approved boolean not null default false,
  created_at timestamptz not null default now()
);

alter table public.stories enable row level security;

-- Anyone can read ONLY approved stories
create policy "read approved" on public.stories
  for select using (approved = true);

-- Anyone can submit, but never as pre-approved
create policy "submit unapproved" on public.stories
  for insert with check (approved = false);

-- To approve a story: Table Editor > stories > tick "approved" on the row.
