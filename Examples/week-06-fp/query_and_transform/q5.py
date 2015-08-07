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
#  Q5: create a query that selects {id, title, boxart}
#  for every video in the 'movie_lists_5'.
#  This time though, the boxarts property in the result will be the url
#  of the boxarts object with dimensions of 150x200px
#
match =  []
print match
assert match == [{'boxart': {'url': 'http://cdn-0.nflximg.com/images/2891/DieHard150.jpg', 'width': 150, 'height': 200}, 'id': 70111470, 'title': 'Die Hard'}]

