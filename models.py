import requests
from config import config
import urllib.parse

locations = "Warsaw,Poland"
api = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timelinemulti"
params = {
    "key": config.api_key,
    "locations": urllib.parse.quote(locations),
}
res = requests.get(api, params=params)
pass









a = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY"




