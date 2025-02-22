facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

# TODO: write code...
except Exception, e:
    raise e
else:
# TODO: write code...
finally:


# TODO: write code...

def count_likes(posts):
    total_likes = 0
    for post in posts:
        total_likes = total_likes + post['Likes']
        return total_likes

count_likes(facebook_posts)

