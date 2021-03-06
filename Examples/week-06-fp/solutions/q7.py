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
#  Q7: combine 'videos' and 'bookmarks' by index
#  to create an array of
#  [ ( {video_id:<id>}, {bookmark_id:<id>} ),... ]
#
video_ids = map(lambda obj: { 'video_id': obj['id'] }, videos )
bookmark_ids = map(lambda obj: { 'bookmark_id': obj['id'] }, bookmarks )
interleaved = zip(video_ids,bookmark_ids)
print interleaved
assert interleaved == [({'video_id': 70111470}, {'bookmark_id': 470}), ({'video_id': 654356453}, {'bookmark_id': 453}), ({'video_id': 65432445}, {'bookmark_id': 445})]
