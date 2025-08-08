# TikTok Login Tool for Termux

Simple TikTok login tool for Termux with welcome messages.

## Installation

### Method 1: Quick Install

```bash
chmod +x quick_install.sh
./quick_install.sh
```

### Method 2: Full Install

```bash
chmod +x install.sh
./install.sh
```

### Method 3: Manual Install

```bash
pkg update -y
pkg install python python-pip -y
pip install requests colorama
chmod +x tiktok_login_tool.py
```

## Usage

```bash
python3 tiktok_login_tool.py
```

or

```bash
./tiktok-login
```

## Uninstall

```bash
rm tiktok_login_tool.py
rm tiktok-login
rm requirements.txt
rm install.sh
rm quick_install.sh
rm tiktok_user_data.json
``` 