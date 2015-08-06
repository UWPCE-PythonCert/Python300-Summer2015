from data import (
    new_releases,
    movie_lists_1,
)
#
#  RULES: no indexing or for loops allowed
#

#
#  Q1: transform the array 'new_releases' of videos
#  into an array of {id,title} pairs
#  using the map function
#
create_pairs = lambda obj: {'title':obj['title'],'id':obj['id']}
pairs = map(create_pairs, new_releases)
print pairs
assert pairs == [{'id': 70111470, 'title': 'Die Hard'},
                 {'id': 654356453, 'title': 'Bad Boys'},
                 {'id': 65432445, 'title': 'The Chamber'},
                 {'id': 675465, 'title': 'Fracture'}]

#
#  Q2: filter the array 'new_releases' of videos
#  into a new array of videos if a video has a rating equal to 5.0
#
ratings_et_5 = lambda obj: obj['rating'] == 5.0
matches = filter(ratings_et_5,new_releases)
print matches
assert matches == [{'rating': 5.0, 'title': 'Bad Boys', 'bookmark': [{'id': 432534, 'time': 65876586}], 'boxart': 'http://cdn-0.nflximg.com/images/2891/BadBoys.jpg', 'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 654356453}, {'rating': 5.0, 'title': 'Fracture', 'bookmark': [{'id': 432534, 'time': 65876587}], 'boxart': 'http://cdn-0.nflximg.com/images/2891/Fracture.jpg', 'uri': 'http://api.netflix.com/catalog/titles/movies/70111470', 'id': 675465}]


#
#  Q3: filter the array 'new_releases' of videos
#  into a new array of videos if a video has a rating equal to 5.0
#  and then transform it into an array of {id,title} pairs
#  using the map function
#
matches = filter(ratings_et_5, new_releases)
pairs = map(create_pairs,matches)
print pairs
assert pairs == [{'id': 654356453, 'title': 'Bad Boys'}, {'id': 675465, 'title': 'Fracture'}]

#
#  Q4: write a function that flattens
#  the 'movie_lists_1' tree
#  into an array of video id(s)
#  given input like this
#  [ [1,2,3], [4,5,6], [7,8,9] ]
#


#
#  Q5: retrieve id, title, and a 150x200
#  box art url for every video in 'movie_lists_5'
#


#
#  Q6: find the largest box art
#

#
#  Q7: combine videos and bookmarks by index
#


