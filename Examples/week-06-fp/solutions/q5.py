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
videos_only = map(lambda obj: obj['videos'],movie_lists_5)
match =  [{'id':video['id'],'title':video['title'],'boxart':boxart}
              for video_list in videos_only
              for video in video_list
              for boxart in video['boxarts']
              if boxart['width'] == 150 and boxart['height'] == 200]
print match
assert match == [{'boxart': {'url': 'http://cdn-0.nflximg.com/images/2891/DieHard150.jpg', 'width': 150, 'height': 200}, 'id': 70111470, 'title': 'Die Hard'}]


