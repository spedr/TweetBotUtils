import json

input_file = 'data\\data.json'
output_fname = 'data_abreu.json'

with open(input_file, encoding='utf8') as f:
    data = json.load(f)

user_list = []

for user in data:
    usr = {}
    
    usr['statuses_count'] = user['statuses_count']
    usr['followers_count'] = user['followers_count']
    usr['friends_count'] = user['friends_count']
    usr['favourites_count'] = user['favourites_count']
    usr['listed_count'] = user['listed_count']

    user_list.append(usr)

with open(output_fname, 'w', encoding='utf8') as fout:
    json.dump(user_list, fout, ensure_ascii=False)