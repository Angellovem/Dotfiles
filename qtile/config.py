# Color dictionary
colors = {
    "bg0": "#191724",  # base
    "bg1": "#1f1d2e",  # surface
    "fg0": "#e0def4",  # text
    "accent_color": "#eb6f92",  # love
    "urgent_color": "#f6c177",  # gold
    "bg": "#232136",  # background
    "red": "#eb6f92",  # accent
    "accent": "#c4a7e7",  # accent
    "subtle": "#393552"  # subtle
}

# Global settings
font = "RobotoMono Nerd Font Mono 16"
background_color = "transparent"
text_color = colors["fg0"]
margin = 0
padding = 0
spacing = 0

# Import Qtile libraries
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import os
import subprocess

# Autostart hook
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home, shell=True)

mod = "mod4"
terminal = guess_terminal()
wallpaper = os.path.expanduser("/home/angelem/Wallpapers/pixelart_pokemon_rayquaza_forest_16x9.png")
wallpaper2 = os.path.expanduser("/home/angelem/Wallpapers/pixelart_pokemon_rayquaza_forest_16x9.png")

# Key bindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Moving windows around layouts
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Managing windows sizes
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Volume Handlers
    Key([mod], "F7", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([mod], "F6", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([mod], "F5", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Knob Volume Hanlder
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Screen brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -d amdgpu_bl1 set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -d amdgpu_bl1 set 10%-")),
    # Screenshots
    Key([mod], "s", lazy.spawn("bash -c 'maim -s | tee ~/Pictures/Screenshots/screenshot_$(date +%Y-%m-%d-%H%M%S).png | xclip -selection clipboard -t image/png'")),
    # Rofi
    Key([mod], "d", lazy.spawn("rofi -show drun -theme ~/.config/rofi/themes/rose.rasi"), desc="Open Rofi app launcher"),
    Key([mod], "p", lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/powermenu.sh")), desc="Open Rofi power menu"),
    Key([mod], "w", lazy.spawn(os.path.expanduser("~/.config/rofi/scripts/wallpaper_selector.sh")), desc="Open Rofi wallpaper selector"),
    # Toggle between split and unsplit sides of stack.
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Groups 
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
        ]
    )

# Layout theme
layout_theme = {
    "border_width": 0,
    "margin": 5,
    "border_focus": colors["accent_color"],
    "border_normal": "#44415a"
}

# Layout
layouts = [
    layout.Bsp(**layout_theme),
]



# Drag floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


# Screens configuration
screens = [
    Screen(), 
    Screen()
]

# Floating layout settings
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Qtile configurations
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "Qtile"

