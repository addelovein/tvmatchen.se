# tvmatchen.se
Home Assistant component for Swedish sports on tv.

The component will give Home Assistant information about when games that you have specified are airing and on what channel.


To setup component copy the script to: YOURCONFIGDIRECTORY/custom_components/sensor/

And add following to your configuration.yaml

IMPORTANT: scan_interval may not be less than: 21600 (we have been approved to scrape site 4 times / day)

sensor:
  - platform: tvmatchen
    widget_url: "READ BELOW FOR URL"
    scan_interval: 21600
  
To retrieve your widget url got to the following page and create the widget of your preference:
http://www.tvmatchen.nu/page/widget/

I have only tested selecting one team in soccer. However it should not be any difference with other configs. (I hope)
 
 
