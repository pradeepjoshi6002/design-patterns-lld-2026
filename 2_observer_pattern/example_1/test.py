from WeatherStation import WeatherStation
from TVDisplay import TVDisplay
from MobileDisplay import MobileDisplay

ws=WeatherStation()

mobD=MobileDisplay(ws)

tvD=TVDisplay(ws)

ws.add(mobD)
ws.add(tvD)

ws.set_data(temperature=20)

