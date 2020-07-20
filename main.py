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

print(f'{count} photos in total')

for i, photo in enumerate(fr.walk_set(photoset_id), start=1):
    sizes = fr.photos_getSizes(photo_id=photo.get('id'))
    photo_uri = sizes.find('sizes').findall('size')[-1].attrib['source']  # 'Original' is always the last size

    extension = photo_uri.split('.')[-1]
    filename = f'flickr.com_{owner_nsid}-{photoset_id}-{str(i).zfill(index_len)}.{extension}'

    urllib.request.urlretrieve(photo_uri, f"images\\{filename}")
    print(f"Saved photo {i} of {count}: {photo_uri}")
