import requests
from lesson_19.utils import photo_extractor


def mr_curiosity_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        photo_extractor(data)
    else:
        print('Помилка. Статус-код:', response.status_code)


if __name__ == "__main__":
    mr_curiosity_photos()

