import json
from datetime import datetime
from datetime import timedelta

input_file = 'data\\data.json'
output_fname = 'data_yang.json'
today = datetime.today()

with open(input_file, encoding='utf8') as f:
    data = json.load(f)

user_list = []

for user in data:
    created_at = datetime.strptime(user['created_at'], '%a %b %d %H:%M:%S %z %Y')
    created_at = created_at.replace(tzinfo=None)
    difference = today - created_at
    difference_in_days = difference / timedelta(days=1)

    user['tweet_freq'] = user['statuses_count'] / difference_in_days
    user['followers_growth_rate'] = user['followers_count'] / difference_in_days
    user['friends_growth_rate'] = user['friends_count'] / difference_in_days
    user['favourites_growth_rate'] = user['favourites_count'] / difference_in_days
    user['listed_growth_rate'] = user['listed_count'] / difference_in_days
    user['screen_name_length'] = len(user['screen_name'])
    user['num_digits_in_screen_name'] = sum(c.isdigit() for c in user['screen_name'])
    user['name_length'] = len(user['name'])
    user['num_digits_in_name'] = sum(c.isdigit() for c in user['name'])
    user['description_length'] = len(user['description'])

    user_list.append(user)

with open(output_fname, 'w', encoding='utf8') as fout:
    json.dump(user_list, fout, ensure_ascii=False)

