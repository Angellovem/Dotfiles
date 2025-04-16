#=================================================================================================
#       d8888                            888 d8b               .d88888b.  888    d8b 888          
#      d88888                            888 88P              d88P" "Y88b 888    Y8P 888          
#     d88P888                            888 8P               888     888 888        888          
#    d88P 888 88888b.   .d88b.   .d88b.  888 "  .d8888b       888     888 888888 888 888  .d88b.  
#   d88P  888 888 "88b d88P"88b d8P  Y8b 888    88K           888     888 888    888 888 d8P  Y8b 
#  d88P   888 888  888 888  888 88888888 888    "Y8888b.      888 Y8b 888 888    888 888 88888888 
# d8888888888 888  888 Y88b 888 Y8b.     888         X88      Y88b.Y8b88P Y88b.  888 888 Y8b.     
#d88P     888 888  888  "Y88888  "Y8888  888     88888P'       "Y888888"   "Y888 888 888  "Y8888  
#                           888                                      Y8b                          
#                      Y8b d88P                                                                   
#                       "Y88P"                                                                    
#=================================================================================================
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

# .d8888b.  888                     888    
#d88P  Y88b 888                     888    
#Y88b.      888                     888    
# "Y888b.   888888  8888b.  888d888 888888 
#    "Y88b. 888        "88b 888P"   888    
#      "888 888    .d888888 888     888    
#Y88b  d88P Y88b.  888  888 888     Y88b.  
# "Y8888P"   "Y888 "Y888888 888      "Y888 

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home, shell=True)

mod = "mod4"
terminal = guess_terminal()

#888    d8P                             
#888   d8P                              
#888  d8P                               
#888d88K      .d88b.  888  888 .d8888b  
#8888888b    d8P  Y8b 888  888 88K      
#888  Y88b   88888888 888  888 "Y8888b. 
#888   Y88b  Y8b.     Y88b 888      X88 
#888    Y88b  "Y8888   "Y88888  88888P' 
#                          888          
#                     Y8b d88P          
#                      "Y88P"           

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
    # Rofi App launcher
    Key([mod], "d", lazy.spawn("rofi -show drun -theme ~/.config/rofi/themes/rose.rasi"), desc="Launch Rofi"),
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

#888                                          888    
#888                                          888    
#888                                          888    
#888       8888b.  888  888  .d88b.  888  888 888888 
#888          "88b 888  888 d88""88b 888  888 888    
#888      .d888888 888  888 888  888 888  888 888    
#888      888  888 Y88b 888 Y88..88P Y88b 888 Y88b.  
#88888888 "Y888888  "Y88888  "Y88P"   "Y88888  "Y888 
#                       888                          
#                  Y8b d88P                          
#                   "Y88P"                           

layout_theme = {
    "border_width": 3,
    "margin": 15,
    "border_focus": "#ebbcba",
    "border_normal": "#44415a"
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



#888       888 d8b      888                   888    
#888   o   888 Y8P      888                   888    
#888  d8b  888          888                   888    
#888 d888b 888 888  .d88888  .d88b.   .d88b.  888888 
#888d88888b888 888 d88" 888 d88P"88b d8P  Y8b 888    
#88888P Y88888 888 888  888 888  888 88888888 888    
#8888P   Y8888 888 Y88b 888 Y88b 888 Y8b.     Y88b.  
#888P     Y888 888  "Y88888  "Y88888  "Y8888   "Y888 
#                                888                 
#                           Y8b d88P                 
#                            "Y88P"                  

widget_defaults = dict(
    font="RobotoMono Nerd Font Mono",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colors = {
    "bg": "#232136",
    "fg": "#e0def4",
    "red": "#eb6f92",
    "accent": "#c4a7e7",
    "subtle": "#393552"
}

def left_widgets():
    return [
        widget.GroupBox(
            highlight_method="line",
            active=colors["fg"],
            inactive=colors["subtle"],
            this_current_screen_border=colors["accent"],
            other_screen_border=colors["red"],
            padding=5,
            disable_drag=True,
        ),
    ]

def center_widgets():
    return [
        widget.Spacer(length=bar.STRETCH),
        widget.Clock(
            format="%Y-%m-%d (%a) %I:%M %p",
            foreground=colors["fg"]
        ),
        widget.Spacer(length=bar.STRETCH),
    ]

def right_widgets():
    return [
        widget.CPU(
            format="CPU {load_percent}%",
            foreground=colors["accent"],
        ),
        widget.Sep(linewidth=0, padding=6),
        widget.GenPollText(
            update_interval=1800,
            func=lambda: "Bogotá~17°C",
            foreground=colors["fg"]
        ),
        widget.Sep(linewidth=0, padding=6),
        widget.Battery(
            format="Battery {percent:2.0%} {char}",
            charge_char="⚡",
            discharge_char="🔋",
            full_char="✔️",
            foreground=colors["fg"]
        ),
    ]

def default_widgets():
    return left_widgets() + center_widgets() + right_widgets()

screens = [
    Screen(
        top=bar.Bar(
            default_widgets(),
            24,
            background=colors["bg"],
            opacity=0.95,
            margin=[4, 8, 0, 8],
        )
    ), 
    Screen(
        top=bar.Bar(
            default_widgets(),
            24,
            background=colors["bg"],
            opacity=0.95,
            margin=[4, 8, 0, 8],
        )
    )
]
# .d8888b.  888          888               888 
#d88P  Y88b 888          888               888 
#888    888 888          888               888 
#888        888  .d88b.  88888b.   8888b.  888 
#888  88888 888 d88""88b 888 "88b     "88b 888 
#888    888 888 888  888 888  888 .d888888 888 
#Y88b  d88P 888 Y88..88P 888 d88P 888  888 888 
# "Y8888P88 888  "Y88P"  88888P"  "Y888888 888 

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
