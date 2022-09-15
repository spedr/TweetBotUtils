import json
import tweepy

output_fname = 'data.json'
input_file = 'data\\bracrc_fullgame.json'

with open('config\config.json') as f:
    token = json.load(f)

auth = tweepy.OAuth1UserHandler(token['api_key'], token['api_secret'], token['access_token'], token['access_secret'])
api = tweepy.API(auth)

with open(input_file, encoding='utf8') as f:
    data = json.load(f)

uid_list = []
users = []

for tweet in data:
    uid_list.append(tweet['user_id'])

# make uids unique
uid_list = list(set(uid_list))

for uid in uid_list:
    usr = {}
    user = api.get_user(user_id=uid)

    usr['id'] = user._json['id_str']
    usr['screen_name'] = user._json['scree_name']
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