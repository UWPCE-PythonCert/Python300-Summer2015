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
create_pairs = lambda obj: {'title':obj['title'],'id':obj['id']}
ratings_et_5 = lambda obj: obj['rating'] == 5.0
matches = filter(ratings_et_5, new_releases)
pairs = map(create_pairs,matches)

pairs = [{'title':obj['title'],'id':obj['id']}
         for obj in new_releases
         if obj['rating'] == 5.0]
print pairs
assert pairs == [{'id': 654356453, 'title': 'Bad Boys'}, {'id': 675465, 'title': 'Fracture'}]