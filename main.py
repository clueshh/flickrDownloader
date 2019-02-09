import flickrapi
import urllib.request

api_key = u'api_key'
api_secret = u'api_secret'
photoset_id = u'photoset_id'

fr = flickrapi.FlickrAPI(api_key, api_secret)

photoset = fr.photosets_getInfo(photoset_id=photoset_id).find('photoset')
owner_nsid = photoset.attrib['owner']
count = photoset.attrib['photos']
index_len = len(count)

print('%s photos in total' % count)

processes = []
counter = 0

for photo in fr.walk_set(photoset_id):
    counter += 1
    label = 'flickr.com_' + owner_nsid + '-' + photoset_id + '-' + str(counter).zfill(index_len)
    photo_id = photo.get('id')
    sizes = fr.photos_getSizes(photo_id=photo_id)
    photo_uri = sizes.find('sizes').findall('size')[-1].attrib['source']  # 'Original' is always the last size
    extension = photo_uri.split('.')[-1]
    filename = label + '.' + extension

    urllib.request.urlretrieve(photo_uri, "images\\%s" % filename)
    print("Saved photo %i of %s: %s" % (counter, count, photo_uri))
