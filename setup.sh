#!/bin/bash

# Angel's Arch Linux Dotfiles Setup Script
# Run this script after cloning the dotfiles repository on a fresh Arch installation

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running on Arch Linux
if ! command -v pacman &> /dev/null; then
    print_error "This script is designed for Arch Linux systems only!"
    exit 1
fi

# Check if script is run as root
if [[ $EUID -eq 0 ]]; then
    print_error "This script should not be run as root!"
    exit 1
fi

# Get the directory where the script is located
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

print_status "Starting Arch Linux dotfiles setup..."
print_status "Dotfiles directory: $DOTFILES_DIR"

# Update system
print_status "Updating system packages..."
sudo pacman -Syu --noconfirm

# Install essential packages
print_status "Installing essential packages..."
PACKAGES=(
    # Window Manager and compositor
    "qtile"
    "picom"
    
    # Terminal and shell
    "alacritty"
    "zsh"
    "zsh-completions"
    
    # System utilities
    "fastfetch"
    "btop"
    "ranger"
    "maim"  # Screenshots
    "xclip" # Clipboard
    "brightnessctl" # Brightness control
    "pulseaudio"
    "pavucontrol"
    
    # Application launcher
    "rofi"
    
    # Status bar
    "polybar"
    
    # File manager
    "thunar"
    
    # Fonts
    "ttf-roboto-mono-nerd"
    "noto-fonts"
    "noto-fonts-emoji"
    
    # Development
    "neovim"
    "git"
    "go"
    
    # Graphics and theming
    "gtk2"
    "gtk3"
    "gtk4"
    "papirus-icon-theme"
    
    # Network
    "firefox"
    
    # Xorg utilities
    "xorg-xrandr"
    "xorg-xset"
    "xorg-xsetroot"
    "xdg-user-dirs"
    
    # Media
    "feh" # Image viewer and wallpaper setter
)

for package in "${PACKAGES[@]}"; do
    if ! pacman -Qi "$package" &> /dev/null; then
        print_status "Installing $package..."
        sudo pacman -S --noconfirm "$package"
    else
        print_success "$package is already installed"
    fi
done

# Install AUR helper (yay) if not present
if ! command -v yay &> /dev/null; then
    print_status "Installing yay AUR helper..."
    cd /tmp
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd "$DOTFILES_DIR"
    print_success "yay installed successfully"
else
    print_success "yay is already installed"
fi

# Create necessary directories
print_status "Creating necessary directories..."
mkdir -p ~/.config
mkdir -p ~/Pictures/Screenshots
mkdir -p ~/Wallpapers

# Backup existing configs if they exist
backup_dir="$HOME/.config_backup_$(date +%Y%m%d_%H%M%S)"
if [[ -d ~/.config ]]; then
    print_status "Backing up existing configs to $backup_dir"
    cp -r ~/.config "$backup_dir"
fi

# Copy configuration files
print_status "Copying configuration files..."

# Copy config directories
config_dirs=("alacritty" "fastfetch" "nvim" "picom" "polybar" "qtile" "rofi" "btop" "gtk-2.0" "gtk-3.0")
for dir in "${config_dirs[@]}"; do
    if [[ -d "$DOTFILES_DIR/$dir" ]]; then
        print_status "Copying $dir configuration..."
        cp -r "$DOTFILES_DIR/$dir" ~/.config/
    fi
done

# Copy individual config files
if [[ -f "$DOTFILES_DIR/user-dirs.dirs" ]]; then
    print_status "Copying user directories configuration..."
    cp "$DOTFILES_DIR/user-dirs.dirs" ~/.config/
fi

if [[ -f "$DOTFILES_DIR/mimeapps.list" ]]; then
    print_status "Copying MIME applications configuration..."
    cp "$DOTFILES_DIR/mimeapps.list" ~/.config/
fi

# Make scripts executable
print_status "Making scripts executable..."
find ~/.config -name "*.sh" -exec chmod +x {} \;

# Update user directories
print_status "Updating user directories..."
xdg-user-dirs-update

# Set up wallpapers directory
if [[ ! -d ~/Wallpapers ]]; then
    mkdir -p ~/Wallpapers
    print_warning "Wallpapers directory created. Please add your wallpapers to ~/Wallpapers/"
fi

# Set zsh as default shell if not already set
if [[ "$SHELL" != "/usr/bin/zsh" ]]; then
    print_status "Setting zsh as default shell..."
    chsh -s /usr/bin/zsh
    print_success "Default shell changed to zsh (will take effect on next login)"
fi

# Install Oh My Zsh if not present
if [[ ! -d ~/.oh-my-zsh ]]; then
    print_status "Installing Oh My Zsh..."
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    print_success "Oh My Zsh installed"
fi

# Copy zsh configuration
if [[ -f "$DOTFILES_DIR/.zshrc" ]]; then
    print_status "Copying zsh configuration..."
    cp "$DOTFILES_DIR/.zshrc" ~/
    print_success "Zsh configuration copied"
fi

# Install NVM (Node Version Manager) if not present
if [[ ! -d ~/.nvm ]]; then
    print_status "Installing NVM (Node Version Manager)..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    print_success "NVM installed (restart shell to use)"
else
    print_success "NVM is already installed"
fi

# Set up git (if not already configured)
if ! git config --global user.name &> /dev/null; then
    print_status "Setting up git configuration..."
    read -p "Enter your git username: " git_username
    read -p "Enter your git email: " git_email
    git config --global user.name "$git_username"
    git config --global user.email "$git_email"
    print_success "Git configured successfully"
fi

# Final setup steps
print_status "Performing final setup steps..."

# Reload font cache
fc-cache -fv

print_success "Setup completed successfully!"
print_status "Please restart your shell or run 'source ~/.zshrc' to load the new configuration."
print_status "After that, you can start Qtile by running 'qtile start' or setting up a display manager."

echo
print_status "Quick start guide:"
echo "1. Restart your shell: 'exec zsh' or open a new terminal"
echo "2. Install Node.js: 'nvm install node' (after shell restart)"
echo "3. Start Qtile: 'qtile start' or configure a display manager"
echo "4. Use Mod+d to open application launcher"
echo "5. Use Mod+Return to open terminal"
echo "6. Check the README.md for complete key bindings"

echo
print_warning "Don't forget to:"
echo "- Add wallpapers to ~/Wallpapers/"
echo "- Install Node.js with 'nvm install node'"
echo "- Customize configurations in ~/.config/ and ~/.zshrc as needed"
echo "- Install additional software based on your needs" 