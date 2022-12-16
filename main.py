import folium
import phonenumbers
from phonenumbers import geocoder

from myphone import number

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode

key = '7b5057c5d0594b948600eaf3affa261d'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print('lat_lng')
print('Traces only landlines to municpal location, Cell phone locallity trace not yet supported ')
myMap = folium.Map
folium.Marker([lat, lng])
