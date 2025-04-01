import requests

url = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json'

response = requests.get(url)
#print(response)

data = response.json()
#print(data)

for artist_dict in data['feed']['results']:
    artist_name = artist_dict['artistName']
    #album_name = artist_dict['im:collection']['im:name']['label']
    song_name = artist_dict['name']
    print(artist_name)
    print(song_name)
    print()
    


