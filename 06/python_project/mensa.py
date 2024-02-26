import requests

def check_in_mensa(keywords):
    response = requests.get('https://www.studierendenwerk-pb.de/gastronomie/speiseplaene/mensa-basilica-hamm/')
    if response.status_code == 200:
        text = response.text.lower()
        for word in keywords:
            if word.lower() in text:
                yield word


if __name__ == '__main__':
    keywords = ['Gyros', 'Pommes', 'Bolognese']
    for dish in check_in_mensa(keywords):
        print(f'Es gibt {dish}!')

