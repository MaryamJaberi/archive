import json, hashlib, glob, os, re
R = '/home/claude/maryamjaberi.github.io/daneshsara'
SC = '/home/claude/work'
W = 'simorgh'
OUT = f'{R}/data/{W}/concepts'
os.makedirs(OUT, exist_ok=True)
S = json.load(open(f'{R}/core/sources.json'))
ALL_IDS = {json.load(open(p))['id'] for p in glob.glob(f'{R}/data/*/concepts/*.json')}
CREATED = {}   # id -> concept dict (this wiki)
PLAN = json.load(open(f'{SC}/vault_src/daneshsara/data/plan/plan.json'))
GAME = json.load(open(f'{SC}/sim/game_data.json'))
CLAIMS = json.load(open('/home/claude/simorgh/files/claims-dataset.json'))
PROBS = json.load(open('/home/claude/simorgh/files/problems-dataset.json'))


def src(prefix, cite=None, year=None, tier=2, url=None):
    """reuse an existing registry entry whose cite starts with prefix; else create from cite"""
    for k, v in S.items():
        if v['cite'].startswith(prefix):
            if W not in v['wikis']: v['wikis'].append(W)
            return k
    assert cite, 'missing source: ' + prefix
    k = 'src:' + hashlib.md5(cite.encode()).hexdigest()[:10]
    e = S.setdefault(k, {'id': k, 'cite': cite, 'year': year, 'tier': tier, 'wikis': []})
    if W not in e['wikis']: e['wikis'].append(W)
    if url: e['url'] = url
    return k


def T(fa, en=None, nl=None):
    en = en or fa
    return {'fa': fa, 'en': en, 'nl': nl or en}


def P(fa, en=None, s=(), flag=False):
    return {'text': T(fa, en), 'sources': list(s), 'flags': ['editor-note'] if flag else []}


def L(to, fa, en=None):
    return {'to': to, 'rel': 'see-also', 'note': T(fa, en)}


def new(slug, title, summary, points=(), links=(), parent='simorgh:simorgh', kind='concept', aliases=()):
    pts = list(points)
    d = {'id': f'{W}:{slug}', 'kind': kind, 'title': title, 'aliases': list(aliases),
         'parent': None if kind == 'root' else parent, 'field': parent if kind == 'concept' else None,
         'summary': summary, 'points': pts, 'links': list(links), 'people': [], 'sources': [], 'booklets': [],
         'origin': None, 'iran': None, 'wikidata': None, 'status': 'draft'}
    for p in pts:
        for k in p['sources']:
            if k not in d['sources']: d['sources'].append(k)
    CREATED[d['id']] = d
    return d


def finish():
    # drop links to concepts that do not exist (private-layer or typo) and report
    bad = []
    for d in CREATED.values():
        keep = []
        for l in d['links']:
            if l['to'] in CREATED or l['to'] in ALL_IDS: keep.append(l)
            else: bad.append((d['id'], l['to']))
        d['links'] = keep
    for p in glob.glob(OUT + '/*.json'): os.remove(p)
    for d in CREATED.values():
        json.dump(d, open(f"{OUT}/{d['id'].split(':')[1]}.json", 'w'), ensure_ascii=False, indent=1)
    json.dump(S, open(f'{R}/core/sources.json', 'w'), ensure_ascii=False, indent=1)
    return bad


def planlink(u):
    m = re.match(r'\.\./(\w+)/#(.+)', u or '')
    return f'{m.group(1)}:{m.group(2)}' if m else None
