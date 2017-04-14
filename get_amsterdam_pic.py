import string
import os
from random import randint
from googleplaces import GooglePlaces, types, lang
import keys

AUTH_KEY = keys.AUTH_KEY

def get_amsterdam_place():
    google_places = GooglePlaces(AUTH_KEY)
    places = google_places.nearby_search(location="Amsterdam", radius=500)
    place = places.places[randint(0, len(places.places)-1)]
    place.get_details()
    photo = place.photos[0]
    str = string.Template("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=$ref&key=$key")
    photo.url = str.substitute(key=AUTH_KEY, ref=photo.photo_reference)

    return { 'name': place.name, 'website': place.website, 'rating': place.rating, 'image': photo.url}

