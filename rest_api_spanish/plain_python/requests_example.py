import requests


def main():
    param = {'base': 'USD', 'symbols': 'EUR'}
    response = requests.get('https://api.exchangeratesapi.io/latest',
                            params=param)
    print(f'response= {response.cookies}')
    if response.status_code == 200:
        print(f'data={response.json()}')


def kwarg_func(kwargs):
    print(**kwargs)


if __name__ == '__main__':
    kwarg_func(kwargs={'x': 1, 'y': 2})
