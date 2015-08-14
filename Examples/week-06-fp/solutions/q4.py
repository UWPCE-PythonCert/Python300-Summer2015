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
#  Q4: write a function that flattens
#  the 'movie_lists_1' tree
#  into an array of video id(s)
#
#  HINT: think about how flatten
#  a lists of lists, for example:
#  [ [0,1,2], [3,4,5], [6,7,8] ]
#
videos_only = map(lambda obj: obj['videos'],movie_lists_1)
category_ids = map(lambda sublist: map(lambda video: video['id'], sublist), videos_only)

# v1
flatten = lambda list_of_lists: [j for i in list_of_lists for j in i]
print flatten(category_ids)
assert flatten(category_ids) == [70111470, 654356453, 65432445, 675465]

# v2
import itertools
print list(itertools.chain(*category_ids))
assert list(itertools.chain(*category_ids)) == [70111470, 654356453, 65432445, 675465]

# v3
results = [ video['id']
            for category in movie_lists_1
            for video in category['videos'] ]
assert results == [70111470, 654356453, 65432445, 675465]
