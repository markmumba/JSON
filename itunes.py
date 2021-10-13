import json

with open('itunes.json') as f:
    data = json.load(f)

    for result in data['results']:
        if result['wrapperType'] == 'track':
            artistId=result['artistId']
            artistName=result['artistName']
            trackName=result['trackName']
            artistViewUrl=result['artistViewUrl']
            trackPrice=result['trackPrice']
            print(f"The artistId:{artistId} , Artist name: {artistName} , Track : {trackName}, Price :{trackPrice}, View url : {artistViewUrl}")
