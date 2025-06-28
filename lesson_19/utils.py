import requests


def photo_extractor(data):
    for addr in data['photos']:
        ph_addr = addr['img_src']
        photo_name = ph_addr.split("/")[-1]
        res = requests.get(ph_addr)
        if res.status_code == 200:
            with open(photo_name, "wb") as file:
                file.write(res.content)
            print(f"Фото: {photo_name} збережено успішно!")
        else:
            print(f"Помилка при завантаженні: {ph_addr} (Код: {res.status_code})")
