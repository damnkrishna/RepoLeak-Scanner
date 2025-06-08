#!/bin/bash

echo "Starting installation of Gitleaks and TruffleHog on Kali Linux..."

# Update package list
sudo apt update -y

# Install pip3 if not installed (needed for trufflehog)
if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found. Installing pip3..."
    sudo apt install python3-pip -y
else
    echo "pip3 already installed"
fi

# Install trufflehog using pip3 if not installed
if ! command -v trufflehog &> /dev/null
then
    echo "Installing TruffleHog..."
    pip3 install trufflehog
else
    echo "TruffleHog already installed"
fi

# Install wget if missing (needed for gitleaks download)
if ! command -v wget &> /dev/null
then
    echo "wget not found. Installing wget..."
    sudo apt install wget -y
else
    echo "wget already installed"
fi

# Install gitleaks if not installed
if ! command -v gitleaks &> /dev/null
then
    echo "Installing Gitleaks..."
    wget https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64.tar.gz -O gitleaks.tar.gz
    tar -xzf gitleaks.tar.gz
    sudo mv gitleaks /usr/local/bin/
    rm gitleaks.tar.gz
else
    echo "Gitleaks already installed"
fi

echo "Installation completed! You can now use trufflehog and gitleaks."
