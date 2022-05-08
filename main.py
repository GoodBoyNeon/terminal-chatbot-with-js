import requests
import json
import os

def get_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def get_env(path):
    with open(path, 'r') as file:
        data = file.read()
    return data
    

url = os.environ.get('URL') or get_env('env.txt')

content = ''

print("\n--------------You can chat with the bot from the terminal------------------\n")

while content.lower() != 'bye':
    content = input('🤠 > ')
    res = get_data( url + content )
    print("🤖 > " + res['cnt'] )