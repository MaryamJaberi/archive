-- دسترسی سیمرغ: سطح‌ها، رول‌ها، آدم‌ها و اینکه هر مسیر در کدام سطح است.
-- قاعده: محتوای واقعی این‌جا نیست؛ فقط «چه کسی اجازهٔ چه سطحی را دارد».
-- سطح ۴ هیچ‌وقت روی سرور نمی‌رود: نه محتوایش، نه حتی نام فایل‌هایش.

create schema if not exists access;

create table access.levels (
  id        int primary key,
  key       text not null unique,
  fa        text not null,
  who       text not null,
  rule      text not null,
  color     text not null
);

create table access.areas   (key text primary key, fa text not null);
create table access.actions (key text primary key, fa text not null, note text default '');

create table access.roles (
  key      text primary key,
  fa       text not null,
  note     text default '',
  levels   int[]  not null default '{0}',
  actions  text[] not null default '{read}',
  areas    text[],                       -- null یعنی همهٔ حوزه‌ها
  created_at timestamptz not null default now()
);

create table access.people (
  id        uuid primary key default gen_random_uuid(),
  label     text not null,               -- برچسب، نه نام واقعی و نه ایمیل
  role_key  text not null references access.roles(key) on update cascade,
  status    text not null default 'active' check (status in ('active','paused','revoked')),
  user_id   uuid unique references auth.users(id) on delete set null,
  note      text default '',
  created_at timestamptz not null default now()
);
create index on access.people (role_key);

create table access.content (
  path       text primary key,
  level      int not null references access.levels(id),
  area       text references access.areas(key),
  title      text default '',
  why        text default '',
  manual     boolean not null default false,
  updated_at timestamptz not null default now(),
  constraint no_level_4_on_server check (level <= 3)
);
create index on access.content (level);

create table access.log (
  id     bigint generated always as identity primary key,
  at     timestamptz not null default now(),
  actor  uuid default auth.uid(),
  what   text not null,
  detail jsonb not null default '{}'::jsonb
);

-- ── توابع کمکی ───────────────────────────────────────────────
create or replace function access.me() returns access.people
  language sql stable security definer set search_path = access, public as $$
  select * from access.people where user_id = auth.uid() and status = 'active' limit 1 $$;

create or replace function access.my_levels() returns int[]
  language sql stable security definer set search_path = access, public as $$
  select coalesce((select r.levels from access.people p join access.roles r on r.key = p.role_key
                   where p.user_id = auth.uid() and p.status = 'active' limit 1), '{}'::int[]) $$;

create or replace function access.my_max_level() returns int
  language sql stable security definer set search_path = access, public as $$
  select coalesce((select max(l) from unnest(access.my_levels()) l), -1) $$;

create or replace function access.is_owner() returns boolean
  language sql stable security definer set search_path = access, public as $$
  select coalesce((select p.role_key = 'owner' from access.people p
                   where p.user_id = auth.uid() and p.status = 'active' limit 1), false) $$;

create or replace function access.can(a text) returns boolean
  language sql stable security definer set search_path = access, public as $$
  select coalesce((select a = any(r.actions) from access.people p join access.roles r on r.key = p.role_key
                   where p.user_id = auth.uid() and p.status = 'active' limit 1), false) $$;

-- ── RLS ──────────────────────────────────────────────────────
alter table access.levels  enable row level security;
alter table access.areas   enable row level security;
alter table access.actions enable row level security;
alter table access.roles   enable row level security;
alter table access.people  enable row level security;
alter table access.content enable row level security;
alter table access.log     enable row level security;

-- جدول‌های پایه: هر کسی که حسابش فعال است می‌خواند؛ فقط مدیر می‌نویسد
create policy read_levels  on access.levels  for select to authenticated using (access.my_max_level() >= 0);
create policy read_areas   on access.areas   for select to authenticated using (access.my_max_level() >= 0);
create policy read_actions on access.actions for select to authenticated using (access.my_max_level() >= 0);
create policy read_roles   on access.roles   for select to authenticated using (access.my_max_level() >= 0);
create policy admin_levels  on access.levels  for all to authenticated using (access.is_owner()) with check (access.is_owner());
create policy admin_areas   on access.areas   for all to authenticated using (access.is_owner()) with check (access.is_owner());
create policy admin_actions on access.actions for all to authenticated using (access.is_owner()) with check (access.is_owner());
create policy admin_roles   on access.roles   for all to authenticated using (access.is_owner()) with check (access.is_owner());

-- آدم‌ها: هر کس فقط ردیف خودش را می‌بیند؛ مدیر همه را
create policy read_own_person on access.people for select to authenticated
  using (user_id = auth.uid() or access.is_owner());
create policy admin_people on access.people for all to authenticated
  using (access.is_owner()) with check (access.is_owner());

-- محتوا: فقط تا سطحی که رول اجازه می‌دهد
create policy read_content on access.content for select to authenticated
  using (level = any(access.my_levels()));
create policy admin_content on access.content for all to authenticated
  using (access.is_owner()) with check (access.is_owner());

-- دفتر: هر کس می‌تواند کار خودش را ثبت کند، فقط مدیر می‌خواند
create policy write_log on access.log for insert to authenticated with check (actor = auth.uid());
create policy read_log  on access.log for select to authenticated using (access.is_owner());

revoke all on schema access from anon;
grant usage on schema access to authenticated;
grant select on all tables in schema access to authenticated;
grant insert, update, delete on access.levels, access.areas, access.actions,
      access.roles, access.people, access.content to authenticated;
grant insert on access.log to authenticated;
