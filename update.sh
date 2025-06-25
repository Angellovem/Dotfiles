#!/bin/bash

# Angel's Dotfiles Update Script
# Run this script to update your dotfiles repository with current system configurations

set -e

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

# Get the directory where the script is located
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

print_status "Updating dotfiles repository with current system configurations..."
print_status "Dotfiles directory: $DOTFILES_DIR"

# Check if we're in the right directory
if [[ ! -f "$DOTFILES_DIR/setup.sh" ]]; then
    print_error "This doesn't appear to be a dotfiles directory. Missing setup.sh"
    exit 1
fi

# Configuration directories to sync
config_dirs=("alacritty" "fastfetch" "nvim" "picom" "polybar" "qtile" "rofi" "btop" "gtk-2.0" "gtk-3.0")

# Update configuration directories
for dir in "${config_dirs[@]}"; do
    if [[ -d "$HOME/.config/$dir" ]]; then
        if [[ -d "$DOTFILES_DIR/$dir" ]]; then
            print_status "Updating $dir configuration..."
            # Create backup if there are differences
            if ! diff -r "$HOME/.config/$dir" "$DOTFILES_DIR/$dir" &>/dev/null; then
                print_warning "Changes detected in $dir configuration"
                # Update the dotfiles
                rm -rf "$DOTFILES_DIR/$dir"
                cp -r "$HOME/.config/$dir" "$DOTFILES_DIR/"
                print_success "$dir configuration updated"
            else
                print_status "$dir configuration is already up to date"
            fi
        else
            print_status "Adding new $dir configuration..."
            cp -r "$HOME/.config/$dir" "$DOTFILES_DIR/"
            print_success "$dir configuration added"
        fi
    else
        print_warning "$HOME/.config/$dir does not exist, skipping..."
    fi
done

# Update individual config files
config_files=("user-dirs.dirs" "mimeapps.list")

for file in "${config_files[@]}"; do
    if [[ -f "$HOME/.config/$file" ]]; then
        if [[ -f "$DOTFILES_DIR/$file" ]]; then
            if ! diff "$HOME/.config/$file" "$DOTFILES_DIR/$file" &>/dev/null; then
                print_status "Updating $file..."
                cp "$HOME/.config/$file" "$DOTFILES_DIR/"
                print_success "$file updated"
            else
                print_status "$file is already up to date"
            fi
        else
            print_status "Adding new $file..."
            cp "$HOME/.config/$file" "$DOTFILES_DIR/"
            print_success "$file added"
        fi
    else
        print_warning "$HOME/.config/$file does not exist, skipping..."
    fi
done

# Check for git repository and offer to commit changes
if [[ -d "$DOTFILES_DIR/.git" ]]; then
    cd "$DOTFILES_DIR"
    
    # Check if there are any changes
    if ! git diff --quiet || ! git diff --cached --quiet; then
        print_status "Git repository detected with changes."
        
        # Show the changes
        echo
        print_status "Changed files:"
        git status --porcelain
        
        echo
        read -p "Do you want to commit these changes? (y/N): " -n 1 -r
        echo
        
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            # Add all changes
            git add .
            
            # Get commit message
            read -p "Enter commit message (or press Enter for default): " commit_msg
            
            if [[ -z "$commit_msg" ]]; then
                commit_msg="Update dotfiles configurations $(date '+%Y-%m-%d %H:%M:%S')"
            fi
            
            # Commit changes
            git commit -m "$commit_msg"
            print_success "Changes committed successfully!"
            
            # Ask about pushing
            if git remote -v &>/dev/null; then
                echo
                read -p "Do you want to push changes to remote repository? (y/N): " -n 1 -r
                echo
                
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    git push
                    print_success "Changes pushed to remote repository!"
                fi
            fi
        else
            print_status "Changes not committed. You can commit them manually later."
        fi
    else
        print_success "No changes detected in git repository."
    fi
else
    print_warning "Not a git repository. Consider initializing git for version control:"
    echo "  git init"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
fi

print_success "Update completed successfully!"
print_status "Your dotfiles repository is now synchronized with your current system configuration." 