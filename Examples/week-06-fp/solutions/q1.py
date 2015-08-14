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
#  Q1: transform the array 'new_releases' of videos
#  into an array of {id,title} pairs
#  using the map function
#
create_pairs = lambda obj: {'title':obj['title'],'id':obj['id']}
pairs = map(create_pairs, new_releases)

pairs = [{'title':obj['title'],'id':obj['id']} for obj in new_releases]
print pairs
assert pairs == [{'id': 70111470, 'title': 'Die Hard'},
                 {'id': 654356453, 'title': 'Bad Boys'},
                 {'id': 65432445, 'title': 'The Chamber'},
                 {'id': 675465, 'title': 'Fracture'}]