import json
from pathlib import Path
items=[]
for p in Path('games').glob('*/info.json'):
    if not (p.parent/'index.html').is_file():
        raise SystemExit(f'Missing game: {p.parent}/index.html')
    g=json.loads(p.read_text(encoding='utf-8'))
    for key in ('title','lesson','topic','description'):
        if key not in g: raise SystemExit(f'{p}: missing {key}')
    g['url']=p.parent.as_posix()+'/'
    items.append(g)
items.sort(key=lambda g:(int(g['lesson']),g['title']))
Path('catalogue.json').write_text(json.dumps(items,indent=2),encoding='utf-8')
