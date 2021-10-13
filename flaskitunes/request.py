import json
from models import Music



# def music() -> List:

#     music_result = []

#     with open('itunes.json') as f:
#         data = json.load(f)

#     for result in data['results']:
#         if result['wrapperType'] == 'track':
#             artistId=result['artistId']
#             artistName=result['artistName']
#             trackName=result['trackName']
#             artistViewUrl=result['artistViewUrl']
#             trackPrice=result['trackPrice']

#             music_object=Music(artistId,artistName,trackName,trackPrice,artistViewUrl)
#             music_result.append(music_object)

#     return music_result

def get_music(type):

    
    with open ('itunes.json') as f:
        collection = json.load(f)

        music_list = []
        for song in collection['results']:
            if song['wrapperType'] == type:
                artistId=song['artistId']
                artistName=song['artistName']
                trackName=song['trackName']
                artistViewUrl=song['artistViewUrl']
                trackPrice=song['trackPrice']

                song_object =Music(artistId,artistName,trackName,trackPrice,artistViewUrl)
                

                music_list.append(song_object)
    
    return music_list
    
                