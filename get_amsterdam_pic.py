import string
from random import randint
from googleplaces import GooglePlaces, types, lang
from PIL import Image


def get_amsterdam_place():
    # image = Image.open('e
    AMSTERDAM_COORDS = (52.371009, 4.892595)
    AUTH_KEY = '***REMOVED***'
    google_places = GooglePlaces(AUTH_KEY)

    places = google_places.nearby_search(location="Amsterdam", radius=500, type=types.TYPE_MUSEUM)

    place = places.places[randint(0, len(places.places))]
    place.get_details()
    photo = place.photos[0]
    str = string.Template("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=$ref&key=$key")
    photo.url = str.substitute(key=AUTH_KEY, ref=photo.photo_reference)

    return { 'name': place.name, 'website': place.website, 'rating': place.rating, 'image': photo.url}

print get_amsterdam_place()
