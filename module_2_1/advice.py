import requests

response = requests.get('https://api.adviceslip.com/advice')

if response.status_code == 200:
    data = response.json()
    print(data)
    print('\nDaily advice for you:\n\n', data['slip']['advice'])

else:
    print('fetch Error!')
