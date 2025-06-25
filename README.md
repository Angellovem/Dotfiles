# Angel's Arch Linux Dotfiles

This Qtile configuration is tailored to enhance my personal workflow, drawing inspiration from various configurations found online and customized to meet my needs. It's not designed to be a one-size-fits-all solution, but rather a reflection of my preferences for a more efficient and enjoyable desktop experience.

## 🚀 Quick Setup (Fresh Arch Installation)

For a fresh Arch Linux installation, simply run:

```bash
git clone https://github.com/your-username/dotfiles.git
cd dotfiles
./setup.sh
```

The setup script will:
- Install all necessary packages
- Configure your system with these dotfiles
- Set up essential directories
- Configure git and shell
- Install AUR helper (yay)

## 📦 What's Included

### Core Components
- **Window Manager**: Qtile with custom configuration
- **Terminal**: Alacritty with Rose Pine theme
- **Application Launcher**: Rofi with custom scripts
- **Status Bar**: Polybar configuration
- **Compositor**: Picom for transparency and effects
- **System Monitor**: btop with custom theme
- **File Manager**: Ranger configuration
- **Text Editor**: Neovim configuration

### Additional Configurations
- **Zsh**: Custom shell configuration with Oh My Zsh
- **Development**: Go language and NVM (Node.js) setup
- **GTK**: Theming and file chooser preferences
- **User Directories**: Custom XDG directory setup
- **MIME Types**: Default application associations
- **Fonts**: Nerd Font configuration

## 🎯 Essential Packages

The setup script installs these packages automatically:

### System Core
- `qtile` - Tiling window manager
- `picom` - Compositor
- `alacritty` - Terminal emulator
- `rofi` - Application launcher
- `polybar` - Status bar

### Utilities
- `fastfetch` - System information
- `btop` - System monitor
- `ranger` - File manager
- `maim` - Screenshots
- `brightnessctl` - Brightness control
- `feh` - Wallpaper setter

### Development Tools
- `go` - Go programming language
- `neovim` - Text editor
- `git` - Version control
- **NVM** - Node.js version manager (installed via script)

### Fonts & Theming
- `ttf-roboto-mono-nerd` - Main font
- `noto-fonts` - Unicode support
- `papirus-icon-theme` - Icon theme

## ⌨️ Key Bindings

This README provides a table of key bindings and their functionalities for the Qtile configuration.

| Command                     | Description                                           |
|-----------------------------|-------------------------------------------------------|
| `Mod + h`                   | Move focus to the left window                         |
| `Mod + l`                   | Move focus to the right window                        |
| `Mod + j`                   | Move focus to the window below                        |
| `Mod + k`                   | Move focus to the window above                        |
| `Mod + Space`               | Move window focus to the next window                  |
| `Mod + Shift + h`           | Move window to the left                               |
| `Mod + Shift + l`           | Move window to the right                              |
| `Mod + Shift + j`           | Move window down                                      |
| `Mod + Shift + k`           | Move window up                                        |
| `Mod + Control + h`         | Grow window to the left                               |
| `Mod + Control + l`         | Grow window to the right                              |
| `Mod + Control + j`         | Grow window down                                      |
| `Mod + Control + k`         | Grow window up                                        |
| `Mod + n`                   | Reset all window sizes                                |
| `Mod + F7`                  | Increase volume by 5%                                 |
| `Mod + F6`                  | Decrease volume by 5%                                 |
| `Mod + F5`                  | Toggle mute                                           |
| `XF86AudioRaiseVolume`      | Increase volume by 5%                                 |
| `XF86AudioLowerVolume`      | Decrease volume by 5%                                 |
| `XF86AudioMute`             | Toggle mute                                           |
| `Mod + s`                   | Take a screenshot and save it to ~/Pictures/Screenshots |
| `Mod + d`                   | Open Rofi application launcher                        |
| `Mod + p`                   | Open Rofi power menu                                  |
| `Mod + w`                   | Open Rofi wallpaper selector                          |
| `Mod + Shift + Return`      | Toggle between split and unsplit sides of stack       |
| `Mod + Return`              | Launch terminal                                       |
| `Mod + Tab`                 | Toggle between layouts                                |
| `Mod + q`                   | Kill focused window                                   |
| `Mod + f`                   | Toggle fullscreen on the focused window               |
| `Mod + t`                   | Toggle floating on the focused window                 |
| `Mod + Control + r`         | Reload the Qtile configuration                        |
| `Mod + Control + q`         | Shutdown Qtile                                        |
| `Mod + r`                   | Spawn a command using a prompt widget                 |
| `Mod + [1-9]`               | Switch to group [1-9]                                 |
| `Mod + Shift + [1-9]`       | Move focused window to group [1-9]                    |

**Note**: `Mod` refers to the `mod4` key (typically the Windows/Super key).

## 🎨 Customization

### Wallpapers
- Place your wallpapers in `~/Wallpapers/`
- Update wallpaper paths in `~/.config/qtile/config.py`
- Use `Mod + w` to open the wallpaper selector

### Colors & Theme
- Colors are defined in the qtile config using Rose Pine theme
- Modify the `colors` dictionary in `qtile/config.py` to change the color scheme

### Adding Applications
- Edit `~/.config/mimeapps.list` to set default applications
- Use `Mod + d` to launch applications via Rofi

## 🔧 Manual Installation (Alternative)

If you prefer manual setup or want to install specific components:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/dotfiles.git
   cd dotfiles
   ```

2. **Install required packages**:
   ```bash
   sudo pacman -S qtile picom alacritty rofi polybar fastfetch btop ranger
   ```

3. **Copy configurations**:
   ```bash
   cp -r alacritty fastfetch nvim picom polybar qtile rofi btop gtk-2.0 gtk-3.0 ~/.config/
   cp user-dirs.dirs mimeapps.list ~/.config/
   cp .zshrc ~/
   ```

4. **Make scripts executable**:
   ```bash
   chmod +x ~/.config/qtile/autostart.sh
   chmod +x ~/.config/rofi/scripts/*.sh
   ```

## 📁 Directory Structure

```
Dotfiles/
├── alacritty/          # Terminal configuration
├── btop/               # System monitor config
├── fastfetch/          # System info display
├── gtk-2.0/            # GTK2 theming
├── gtk-3.0/            # GTK3 theming
├── nvim/               # Neovim configuration
├── picom/              # Compositor settings
├── polybar/            # Status bar config
├── qtile/              # Window manager config
├── rofi/               # Application launcher
├── .zshrc              # Zsh shell configuration
├── mimeapps.list       # Default applications
├── user-dirs.dirs      # XDG directories
├── setup.sh           # Automated setup script
├── update.sh           # Configuration sync script
└── README.md          # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **Qtile won't start**: Ensure Python and qtile are properly installed
2. **Fonts not displaying**: Install nerd fonts: `sudo pacman -S ttf-roboto-mono-nerd`
3. **Audio controls not working**: Install pulseaudio: `sudo pacman -S pulseaudio pavucontrol`
4. **Screenshots not working**: Install maim and xclip: `sudo pacman -S maim xclip`

### Reset Configuration
If something goes wrong, the setup script creates backups in `~/.config_backup_TIMESTAMP/`

## 📋 Post-Installation

After running the setup script:

1. **Reboot your system**
2. **Add wallpapers** to `~/Wallpapers/`
3. **Start Qtile**: `qtile start` or configure a display manager
4. **Test key bindings** to ensure everything works
5. **Install Node.js**: Use `nvm install node` to install the latest Node.js
6. **Customize** configurations in `~/.config/` and `~/.zshrc` as needed

## 🤝 Contributing

Feel free to fork this repository and adapt it to your needs. If you find improvements or fixes, pull requests are welcome!

## 📄 License

This configuration is provided as-is for personal use. Feel free to modify and distribute according to your needs.
