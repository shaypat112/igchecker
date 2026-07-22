import json



with open("followers.json") as f:
    followers = set(json.load(f))

with open("following.json") as f:
    following = set(json.load(f))

not_following_back = following - followers

print(not_following_back)
