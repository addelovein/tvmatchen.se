# tvmatchen.se
Home Assistant component for Swedish sports on tv.

The component will give Home Assistant information about when games that you have specified are airing and on what channel.


To setup component copy the script to: YOURCONFIGDIRECTORY/custom_components/sensor/

And add following to your configuration.yaml

IMPORTANT: scan_interval may not be less than: 21600 (we have been approved to scrape site 4 times / day)
```
sensor:
  - platform: tvmatchen
    widget_url: "READ BELOW FOR URL"
    scan_interval: 21600
```
To retrieve your widget url got to the following page and create the widget of your preference:
http://www.tvmatchen.nu/page/widget/

Enter your email and info then you will receive the following:
<iframe src="http://widget.tvmatchen.nu/597238e1a8566?heading=TV-matcher&border_color=blue&autoscroll=1" frameborder="0" style="width: 300px; height: 200px; border: none"></iframe>

Copy the url:
http://widget.tvmatchen.nu/597238e1a8566?heading=TV-matcher&border_color=blue&autoscroll=1

And paste it in your config at widget_url


I have only tested selecting one team in soccer. However it should not be any difference with other configs. (I hope)
 
 
``` I have no association with the owners of TVMatchen.se, I have asked permission to create this script and been granted as long as scripts parse max 4 times a day ```
