#!/bin/bash

# Define the directory containing wallpapers
wallpapers_dir="$HOME/Wallpapers"
qtile_config="$HOME/.config/qtile/config.py"

# Create a list of image files (filenames only, no path)
mapfile -t files < <(find "$wallpapers_dir" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) -printf "%f\n")

# Let the user select one via rofi
selected_file=$(printf '%s\n' "${files[@]}" | rofi -dmenu -p "Select Wallpaper" -i)

# If something was selected
if [ -n "$selected_file" ]; then
    selected_path="$wallpapers_dir/$selected_file"

    # Change the wallpaper using feh
    feh --bg-scale "$selected_path"

    # Escape slashes for sed replacement
    escaped_path=$(printf '%s\n' "$selected_path" | sed 's/[\/&]/\\&/g')

    # Update both 'wallpaper =' and 'wallpaper2 =' lines in config.py
    sed -i -E "s|^(wallpaper[0-9]? = )os\.path\.expanduser\(\"[^\"]+\"\)|\1os.path.expanduser(\"$escaped_path\")|g" "$qtile_config"

    # Reload Qtile to apply config (optional)
    qtile cmd-obj -o cmd -f reload_config
fi
