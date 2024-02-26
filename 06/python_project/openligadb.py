import requests
import json

def lade_spiel(lige, saison, spieltag):
    url = f"https://api.openligadb.de/getmatchdata/{lige}/{saison}/{spieltag}"
    request = requests.get(url)
    if request.status_code == 200:
        return json.loads(request.content)
    return []

if __name__ == "__main__":
    spiele = lade_spiel("bl1", 2023, 23)
    for spiel in spiele:
        print(spiel)