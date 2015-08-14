from data import (
    new_releases,
    movie_lists_1,
    movie_lists_5,
    boxarts,
    videos,
    bookmarks
)
#
#  RULES: no indexing
#

#
#  Q2: filter the array 'new_releases' of videos
#  into a new array of videos if a video has a rating equal to 5.0
#
ratings_et_5 = lambda obj: obj['rating'] == 5.0
matches = filter(ratings_et_5,new_releases)
matches = [obj for obj in new_releases if obj['rating'] == 5.0]
print matches
assert matches == [{'rating': 5.0, 'title': 'Bad Boys', 'bookmark': [{'id': 432534, 'time': 65876586}], 'boxart': 'http://cdn-0.nflximg.com/images/2891/BadBoys.jpg', 'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 654356453}, {'rating': 5.0, 'title': 'Fracture', 'bookmark': [{'id': 432534, 'time': 65876587}], 'boxart': 'http://cdn-0.nflximg.com/images/2891/Fracture.jpg', 'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 675465}]
