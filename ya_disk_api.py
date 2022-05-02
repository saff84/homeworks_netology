from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = 'https://cloud-api.yandex.net'

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_link(self,file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path':file_path, 'overwrite': True}
        response = requests.get(url, params = params, headers=headers)
        return response.json().get('href')

    def upload_file(self, path, file_name):
        up_link = self.upload_link(path)
        headers = self.get_headers()
        response = requests.put(up_link, data=open(file_name,'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Очень интересно, но ничего не понятно')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file = input('введите путь до файла: ').replace('"','')
    path_to_file = f'/{os.path.split(file)[1]}'
    # print(path_to_file)
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file(path_to_file,file)