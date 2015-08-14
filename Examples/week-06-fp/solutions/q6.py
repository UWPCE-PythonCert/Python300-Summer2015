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
#  Q6: find the largest box art width form 'boxarts'
#
def widthiest(accum,current):
    if current['width'] > accum:
        return current['width']
    return accum
print reduce(widthiest,boxarts)
assert reduce(widthiest,boxarts) == {'url': 'http://cdn-0.nflximg.com/images/2891/Fracture200.jpg', 'width': 200, 'height': 200}
