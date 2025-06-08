#!/bin/bash

echo "Starting Kali Linux setup for Security Leak Scanner project..."

# Update system package list
sudo apt update -y

# Install Python3 and pip3 if not installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found, installing..."
    sudo apt install python3 -y
else
    echo "Python3 already installed"
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found, installing..."
    sudo apt install python3-pip -y
else
    echo "pip3 already installed"
fi

# Install trufflehog via pip if not installed
if ! command -v trufflehog &> /dev/null
then
    echo "Installing trufflehog..."
    pip3 install trufflehog
else
    echo "trufflehog already installed"
fi

# Install gitleaks (via apt or manual if preferred)
if ! command -v gitleaks &> /dev/null
then
    echo "Installing gitleaks..."
    # You might want to update this to the latest installation method
    # Here's an example for installing from GitHub release
    wget https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks-linux-amd64.tar.gz
    tar -xzf gitleaks-linux-amd64.tar.gz
    sudo mv gitleaks /usr/local/bin/
    rm gitleaks-linux-amd64.tar.gz
else
    echo "gitleaks already installed"
fi

echo "Setup completed! You can now run simleaks.py on Kali Linux."
