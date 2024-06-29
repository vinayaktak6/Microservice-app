import requests

class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        response = requests.post(f'{self.base_url}/login', json={'username': username, 'password': password})
        if response.status_code == 200:
            self.token = response.json()['access_token']
        return response

    def get_items(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/items', headers=headers)
        return response

    def create_item(self, name, description):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(f'{self.base_url}/items', json={'name': name, 'description': description}, headers=headers)
        return response

    def get_status(self):
        response = requests.get(f'{self.base_url}/status')
        return response

    def get_health(self):
        response = requests.get(f'{self.base_url}/health')
        return response

if __name__ == '__main__':
    client = Client(base_url='http://localhost:5000')
    print(client.login('testuser', 'testpassword').json())
    print(client.get_items().json())
    print(client.create_item('item1', 'description1').json())
    print(client.get_status().json())
    print(client.get_health().json())
