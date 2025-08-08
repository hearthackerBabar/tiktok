#!/bin/bash

# Quick Install Script for TikTok Login Tool
# This script can be run directly to install the tool

echo "🚀 TikTok Login Tool - Quick Install"
echo "===================================="
echo ""

# Check if we're in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "❌ This tool is designed for Termux only!"
    echo "Please install Termux from F-Droid and run this script there."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "🐍 Installing Python..."
    pkg update -y
    pkg install python python-pip -y
fi

# Install required packages
echo "📦 Installing required packages..."
pip install requests colorama

# Check if the main script exists
if [ ! -f "tiktok_login_tool.py" ]; then
    echo "❌ tiktok_login_tool.py not found!"
    echo "Please make sure all files are in the same directory."
    exit 1
fi

# Make scripts executable
echo "🔐 Setting permissions..."
chmod +x tiktok_login_tool.py

# Create launcher
echo "🚀 Creating launcher..."
cat > tiktok-login << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 tiktok_login_tool.py
EOF

chmod +x tiktok-login

echo ""
echo "✅ Installation completed!"
echo ""
echo "🎯 To start the tool, run:"
echo "   python3 tiktok_login_tool.py"
echo "   or"
echo "   ./tiktok-login"
echo ""
echo "📱 Enjoy your TikTok Login Tool!" 