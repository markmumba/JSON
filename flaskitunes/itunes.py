from views import app
from models import Music
import json


def get_data():
    music_result = []
    with open('itunes.json') as f:
        data = json.load(f)

    for result in data['results']:
        if result['wrapperType'] == 'track':
            artistId=result['artistId']
            artistName=result['artistName']
            trackName=result['trackName']
            artistViewUrl=result['artistViewUrl']
            trackPrice=result['trackPrice']
            music_object=Music(artistId,artistName,trackName,trackPrice,artistViewUrl)
            music_result.append(music_object)

    return music_result