import requests

host = 'http://127.0.0.1:8000/'


def get_login_token():
    credentials = {
        'username': 'aseem',
        'password': 'password123'
    }
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
                             data=credentials)
    print(f'status code = {response.status_code}')
    print(f'response = {response.json()}')


def get_profiles_list():
    headers = {'Authorization': 'Token 04b8a888019d199bb8073e8490334dd23e60d357'}
    response = requests.get(host + 'api/profiles/',
                            headers=headers)
    print(f'status = {response.status_code}')
    print(f'data = {response.json()}')


def register_user():
    """
    4536f704b1d5e3d5680e1079714bb8148e80a405
    """
    credentials = {
        'username': 'kavita',
        'email': 'kav@gmail.com',
        'password1': 'asdlkjasdlkj',
        'password2': 'asdlkjasdlkj'
    }
    response = requests.post(host+'api/rest-auth/registration/',
                             data=credentials)
    print(f'status={response.status_code}')
    print(f'data={response.json()}')



if __name__ == '__main__':
    get_login_token()
    get_profiles_list()
    register_user()
