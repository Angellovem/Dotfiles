!/bin/sh
xrandr --output HDMI-1-0 --mode 1920x1080 --rate 120 --right-of eDP-1
picom &
wallpaper=$(python3 -c "import sys; sys.path.append('/home/angelem/.config/qtile'); from config import wallpaper; print(wallpaper)")
wallpaper2=$(python3 -c "import sys; sys.path.append('/home/angelem/.config/qtile'); from config import wallpaper2; print(wallpaper2)")
feh --bg-scale "$wallpaper" "$wallpaper2" &
pkill polybar
sleep 1
polybar primary & 
polybar secondary &
