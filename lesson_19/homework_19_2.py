import requests
base_url = 'http://127.0.0.1:8080'
file_name = 'FLB_486265257EDR_F0481570FHAZ00323M_.JPG'


def post_func():
    url = f'{base_url}/upload'
    with open(file_name, 'rb') as file:
        files = {'image': file}
        response = requests.post(url=url, files=files)
    if response.status_code == 201:
        created_data = response.json()
        print('Створено дані:', created_data)
    else:
        print('Помилка. Статус-код:', response.status_code)


def get_func():
    url = f'{base_url}/image/{file_name}'
    # response = requests.get(url, headers={"Content-Type": "image"})  # Тут я реализовал скачивание файла как картинку
    response = requests.get(url, headers={"Content-Type": "text"})
    if response.status_code == 200:
        # with open('downloaded_file.jpg', 'wb') as file:
        #     file.write(response.content)
        data = response.json()
        print('Файл успішно збережено!', data)
        # print('Файл успішно збережено!')
    else:
        print('Помилка. Статус-код:', response.status_code)


def delete_func():
    url = f'{base_url}/delete/{file_name}'
    response = requests.delete(url)
    if response.status_code == 200:
        data = response.json()
        print('Дані успішно видалено', data)
    else:
        print('Помилка. Статус-код:', response.status_code)


if __name__ == "__main__":
    post_func()
    # get_func()
    # delete_func()
