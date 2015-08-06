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


#
#  Q6: find the largest box art width form 'boxarts'
#
def widthiest(accum,current):
    if current['width'] > accum:
        return current['width']
    return accum
print reduce(widthiest,boxarts)
assert reduce(widthiest,boxarts) == {'url': 'http://cdn-0.nflximg.com/images/2891/Fracture200.jpg', 'width': 200, 'height': 200}

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

