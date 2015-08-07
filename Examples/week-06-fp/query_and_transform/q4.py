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
#  into an array of video id(s).
#  you'll have to use 'map' a bit too
#
#  HINT: think about how flatten
#  a lists of lists, for example:
#  [ [0,1,2], [3,4,5], [6,7,8] ]
#
flattened = []
assert flattened == [70111470, 654356453, 65432445, 675465]