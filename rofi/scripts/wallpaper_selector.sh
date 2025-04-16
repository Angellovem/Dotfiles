#!/bin/bash

# Define the directory containing wallpapers
wallpapers_dir="$HOME/Wallpapers"

# Create a list of image files (filenames only, no path)
mapfile -t files < <(find "$wallpapers_dir" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) -printf "%f\n")

# Let the user select one via rofi
selected_file=$(printf '%s\n' "${files[@]}" | rofi -dmenu -p "Select Wallpaper" -i)

# If something was selected
if [ -n "$selected_file" ]; then
    selected_path="$wallpapers_dir/$selected_file"
    feh --bg-scale "$selected_path"
fi
