import requests
import json
import keys
# print(keys.keys.accuKey)
def exec(lat,lng):
    # try:
        url='http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey='+keys.keys.accuKey+'&q='+str(lat)+','+str(lng)
        locKey=json.loads(requests.get(url).text)['Key']
        url2='http://dataservice.accuweather.com/currentconditions/v1/'+locKey+'?apikey='+keys.keys.accuKey+'&details=true'
        locDetais=json.loads(requests.get(url2).text)
        temp=locDetais[0]['Temperature']['Metric']['Value']
        humidity=locDetais[0]['RelativeHumidity']
        wind=locDetais[0]['Wind']['Speed']['Metric']['Value']
        return({'temp':temp,'humidity':humidity,'wind':wind})
    # except:
        return None
