import json
from urllib.request import urlopen


with urlopen('https://archive.org/metadata/TheAdventuresOfTomSawyer_201303') as source_url:
    source=source_url.read()
    # print(source)

data =json.loads(source)
    # new_data = json.dumps(data, indent=3)
    
for one in data['files']:
    name = one['name']
    size = one['size']
    print(name , size)

