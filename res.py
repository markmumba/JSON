import json

with open('res.json') as f:
    data = json.load(f)


for weather in data['dataseries']:
    del weather['cloudcover']
    
                

        
with open('new_res.json', 'w') as f:
    json.dump(data, f, indent=3)

