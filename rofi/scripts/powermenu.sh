#!/bin/bash

# Options with Rose Pine-themed icons (Unicode, assuming Nerd Fonts or similar)
options=(" Shutdown" " Reboot" " Suspend" " Logout")

# Format options for Rofi
menu=$(printf "%s\n" "${options[@]}")

# Show Rofi menu with your rose.rasi theme
selected=$(echo -e "$menu" | rofi -dmenu -i -p "Power Menu" -theme ~/.config/rofi/themes/rose.rasi)

# Confirmation prompt for destructive actions
confirm() {
    echo -e "Yes\nNo" | rofi -dmenu -i -p "Confirm $1?" -theme ~/.config/rofi/themes/rose.rasi
}

# Execute the selected action
case "$selected" in
    " Shutdown")
        if [[ $(confirm "Shutdown") == "Yes" ]]; then
            systemctl poweroff
        fi
        ;;
    " Reboot")
        if [[ $(confirm "Reboot") == "Yes" ]]; then
            systemctl reboot
        fi
        ;;
    " Suspend")
        systemctl suspend
        ;;
    " Logout")
        qtile cmd-obj -o cmd -f shutdown  # Logout command for Qtile
        ;;
esac
