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
#  Q3: filter the array 'new_releases' of videos
#  into a new array of videos if a video has a rating equal to 5.0
#  and then transform it into an array of {id,title} pairs
#  using the map function
#
pairs = []
print pairs
assert pairs == [{'id': 654356453, 'title': 'Bad Boys'}, {'id': 675465, 'title': 'Fracture'}]