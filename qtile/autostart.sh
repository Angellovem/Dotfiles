!/bin/sh
xrandr --output HDMI-1-0 --mode 1920x1080 --rate 120 --right-of eDP-1
picom &
feh --bg-scale ~/Wallpapers/pixelart_pokemon_rayquaza_forest_16x9.png ~/Wallpapers/pixelart_pokemon_rayquaza_forest_16x9.png &
pkill polybar
sleep 1
polybar primary & 
polybar secondary &
