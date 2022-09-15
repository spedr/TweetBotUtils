import json
import tweepy
from selenium import webdriver
from time import sleep

output_fname = 'data.json'

op = webdriver.ChromeOptions()
#op.add_argument('headless')
driver = webdriver.Chrome(options=op)

input_file = 'data\\bracrc_fullgame.json'
with open(input_file, encoding='utf8') as f:
    data = json.load(f)

# get only first 20 entries
data = data[:1]

# fill user domain with gibberish so we get a proper redirect
base_url = 'https://twitter.com/zzzzzzzzzzz55555/status/'
screen_names = []

for item in data:
    get_url = base_url + str(item['id'])
    driver.get(get_url)
    sleep(4)

    screen_name = driver.current_url.split('/')[3]
    print(screen_name)

    if screen_name != 'zzzzzzzzzzz55555':
        screen_names.append(screen_name)

with open('config\config.json') as f:
    token = json.load(f)

auth = tweepy.OAuth1UserHandler(token['api_key'], token['api_secret'], token['access_token'], token['access_secret'])
api = tweepy.API(auth)
  
users = []

for sname in screen_names:
    usr = {}
    user = api.get_user(screen_name=sname)

    usr['id'] = user._json['id_str']
    usr['screen_name'] = sname
    usr['name'] = user._json['name']
    usr['url'] = user._json['url']
    usr['description'] = user._json['description']
    usr['created_at'] = user._json['created_at']
    usr['followers_count'] = user._json['followers_count']
    usr['favourites_count'] = user._json['favourites_count']
    usr['statuses_count'] = user._json['statuses_count']
    usr['friends_count'] = user._json['friends_count']
    usr['listed_count'] = user._json['listed_count']

    users.append(usr)

with open(output_fname, 'w', encoding='utf8') as fout:
    json.dump(users, fout, ensure_ascii=False)