import folium
import itertools
import threading
import time
import sys
import phonenumbers
from phonenumbers import geocoder

from myphone import number


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
Corexital = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if Corexital:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rCorexital Data Results!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(3)
Corexital = True

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
print('Corexital Data Phone Tracer 2022 - Results Vary Depending on Conditions. Results May Be 50 Metres to 100KM in Rare Cases.')
myMap = folium.Map
folium.Marker([lat, lng])
