#!/bin/bash

# Adjust display to not blank / not activate screensaver / disable display pm
xset s noblank
xset s off
xset -dpms

# Hide Mouse
unclutter -idle 0.5 -root &

# Disable warnings on bad exit from Chromium
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

# Start Grafana
#chromium-browser -noerrdialogs --no-sandbox --disable-infobars --kiosk "http://192.168.20.7:3000/d/e8pYJFzgk/home-power-dashboard?orgId=1&kiosk&refresh=5s" &


#grafana-kiosk --URL http://192.168.20.7:3000 --username admin --password grafana --kiosk-mode tv
