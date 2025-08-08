#!/bin/bash

# TikTok Login Tool Installer for Termux
# This script installs the TikTok login tool on Termux

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                TikTok Login Tool Installer                  ║"
echo "║                        for Termux                           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if running on Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "❌ This installer is designed for Termux only!"
    echo "Please run this on a Termux environment."
    exit 1
fi

echo "🔧 Starting installation..."

# Update package list
echo "📦 Updating package list..."
pkg update -y

# Install Python and pip
echo "🐍 Installing Python and pip..."
pkg install python -y
pkg install python-pip -y

# Install required packages
echo "📚 Installing required packages..."
pip install requests colorama

# Make the script executable
echo "🔐 Setting permissions..."
chmod +x tiktok_login_tool.py

# Create a simple launcher script
echo "🚀 Creating launcher script..."
cat > tiktok-login << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 tiktok_login_tool.py
EOF

chmod +x tiktok-login

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "📱 To run the tool, use one of these commands:"
echo "   • python3 tiktok_login_tool.py"
echo "   • ./tiktok-login"
echo ""
echo "🔧 To uninstall, simply delete the files:"
echo "   • rm tiktok_login_tool.py"
echo "   • rm tiktok-login"
echo "   • rm requirements.txt"
echo "   • rm install.sh"
echo ""
echo "🎉 Enjoy using TikTok Login Tool!" 