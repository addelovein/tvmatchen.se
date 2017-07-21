"""
    Hämta data från TV Matchen.
"""
import logging
import datetime
import voluptuous as vol
from homeassistant.helpers.entity import Entity
from datetime import datetime as dt
from bs4 import BeautifulSoup
from urllib.request import urlopen
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA

_LOGGER = logging.getLogger(__name__)
REQUIREMENTS = ['beautifulsoup4==4.6.0']

GAME = "match"
GAME_TIME = "start_time"
GAME_CHAN = "chan"
GAME_SPORT = "sport"
GAME_DATE = "gamedate"
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required('widget_url'): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    widgeturl = config.get('widget_url')
    add_devices([TVMatchenSensor(widgeturl, hass)])

class TVMatchenSensor(Entity):
    def __init__(self, widgeturl,hass):
        self.hass = hass
        self.match = ""
        self.start_time = ""
        self.chan = ""
        self.sport = ""
        self.gamedate = ""
        self._state = ""
        self._widgeturl = widgeturl
        self.update()

    @property
    def name(self):
        return "TVMatchen.se"

    @property
    def state(self):
        return self._state

    @property
    def state_attributes(self):
        return {
            GAME: self.match,
            GAME_TIME: self.start_time,
            GAME_CHAN: self.chan,
            GAME_DATE: self.gamedate,
            GAME_SPORT: self.sport,
        }

    def update(self):
        _LOGGER.info("Current Data: " + self.match + " " + self.gamedate  + " " + self.start_time)
        _LOGGER.info("Fetching data")
        content = urlopen(self._widgeturl + "&REF=HA")      
        soup = BeautifulSoup(content, "html.parser")

        self.match = soup.select("#matches .details h3")[0].text
        self.start_time = soup.select("#matches time")[0].text
        self.chan = soup.select("#matches .details .channels a")[0]['title']
        self.sport = soup.select("#matches i.sicon")[0]['title']
        self.gamedate = soup.select("#matches li")[0]['data-hash']
        a = dt.strptime(self.gamedate, "%Y-%m-%d").date()
        b = datetime.datetime.now().date()
        self._state = (a-b).days