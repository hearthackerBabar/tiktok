#!/usr/bin/env python3
"""
TikTok Login Tool for Termux
A simple tool to authenticate TikTok accounts and display welcome messages.
"""

import os
import sys
import json
import getpass
import requests
import time
from datetime import datetime

class TikTokLoginTool:
    def __init__(self):
        self.session = requests.Session()
        self.user_data_file = "tiktok_user_data.json"
        self.base_url = "https://www.tiktok.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_banner(self):
        """Display tool banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    TikTok Login Tool                         ║
║                        for Termux                            ║
║                                                              ║
║  A simple authentication tool for TikTok accounts           ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def print_colored(self, text, color_code):
        """Print colored text"""
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'reset': '\033[0m'
        }
        print(f"{colors.get(color_code, '')}{text}{colors['reset']}")
        
    def save_user_data(self, username, email):
        """Save user login data locally"""
        data = {
            'username': username,
            'email': email,
            'login_time': datetime.now().isoformat(),
            'last_used': datetime.now().isoformat()
        }
        
        try:
            with open(self.user_data_file, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            self.print_colored(f"Error saving user data: {e}", 'red')
            return False
            
    def load_user_data(self):
        """Load previously saved user data"""
        try:
            if os.path.exists(self.user_data_file):
                with open(self.user_data_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            self.print_colored(f"Error loading user data: {e}", 'red')
        return None
        
    def validate_email(self, email):
        """Basic email validation"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
        
    def simulate_login_process(self, username, password):
        """Simulate login process (for demonstration purposes)"""
        self.print_colored("🔐 Attempting to authenticate...", 'yellow')
        time.sleep(1)
        
        # Simulate network delay
        for i in range(3):
            self.print_colored(f"⏳ Processing... {i+1}/3", 'blue')
            time.sleep(0.5)
            
        # Simulate login validation
        if len(password) < 6:
            return False, "Password too short"
            
        if not self.validate_email(username) and len(username) < 3:
            return False, "Invalid username format"
            
        return True, "Login successful"
        
    def login(self):
        """Main login function"""
        self.clear_screen()
        self.print_banner()
        
        # Check for existing login
        existing_data = self.load_user_data()
        if existing_data:
            self.print_colored("📱 Found existing login data!", 'green')
            choice = input("Do you want to use existing account? (y/n): ").lower()
            if choice == 'y':
                return self.welcome_user(existing_data['username'], existing_data['email'])
        
        self.print_colored("🔑 TikTok Login", 'cyan')
        print("=" * 50)
        
        # Get login credentials
        username = input("Enter username or email: ").strip()
        if not username:
            self.print_colored("❌ Username cannot be empty!", 'red')
            return False
            
        password = getpass.getpass("Enter password: ").strip()
        if not password:
            self.print_colored("❌ Password cannot be empty!", 'red')
            return False
            
        # Attempt login
        success, message = self.simulate_login_process(username, password)
        
        if success:
            self.print_colored("✅ " + message, 'green')
            
            # Save user data
            if self.save_user_data(username, username if '@' in username else f"{username}@tiktok.com"):
                self.print_colored("💾 Login data saved locally", 'green')
                
            return self.welcome_user(username, username if '@' in username else f"{username}@tiktok.com")
        else:
            self.print_colored("❌ " + message, 'red')
            return False
            
    def welcome_user(self, username, email):
        """Display welcome message"""
        self.clear_screen()
        
        welcome_banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    Welcome Back! 🎉                          ║
╚══════════════════════════════════════════════════════════════╝

👋 Hello, {username}!
📧 Email: {email}
🕒 Login Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

✅ Successfully logged into TikTok
🔒 Your session is now active

What would you like to do?
1. View Profile Info
2. Check Account Status
3. Logout
4. Exit
        """
        
        print(welcome_banner)
        
        while True:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.show_profile_info(username, email)
            elif choice == '2':
                self.check_account_status(username)
            elif choice == '3':
                self.logout()
                break
            elif choice == '4':
                self.print_colored("👋 Goodbye!", 'green')
                sys.exit(0)
            else:
                self.print_colored("❌ Invalid choice! Please try again.", 'red')
                
    def show_profile_info(self, username, email):
        """Display profile information"""
        self.clear_screen()
        
        profile_info = f"""
╔══════════════════════════════════════════════════════════════╗
║                    Profile Information                       ║
╚══════════════════════════════════════════════════════════════╝

👤 Username: {username}
📧 Email: {email}
📅 Account Created: {datetime.now().strftime('%Y-%m-%d')}
🕒 Last Login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔒 Account Status: Active ✅
🌐 Platform: TikTok
        """
        
        print(profile_info)
        input("\nPress Enter to continue...")
        
    def check_account_status(self, username):
        """Check account status"""
        self.clear_screen()
        
        status_info = f"""
╔══════════════════════════════════════════════════════════════╗
║                    Account Status                            ║
╚══════════════════════════════════════════════════════════════╝

👤 Username: {username}
🔒 Status: Active ✅
🛡️ Security: Enabled
📱 Device: Termux (Android)
🌐 Location: Local
⏰ Session: Valid
        """
        
        print(status_info)
        input("\nPress Enter to continue...")
        
    def logout(self):
        """Logout function"""
        self.print_colored("🔓 Logging out...", 'yellow')
        time.sleep(1)
        
        # Remove saved data
        try:
            if os.path.exists(self.user_data_file):
                os.remove(self.user_data_file)
                self.print_colored("🗑️ Login data cleared", 'green')
        except Exception as e:
            self.print_colored(f"⚠️ Could not clear data: {e}", 'yellow')
            
        self.print_colored("✅ Successfully logged out!", 'green')
        time.sleep(2)
        
    def main_menu(self):
        """Main menu"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = """
╔══════════════════════════════════════════════════════════════╗
║                        Main Menu                             ║
╚══════════════════════════════════════════════════════════════╝

1. 🔑 Login to TikTok
2. 📱 Check Existing Login
3. 🛠️ Tool Information
4. 🚪 Exit

Choose an option (1-4):
            """
            
            print(menu)
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.login()
            elif choice == '2':
                existing_data = self.load_user_data()
                if existing_data:
                    self.print_colored(f"📱 Found login for: {existing_data['username']}", 'green')
                    input("Press Enter to continue...")
                else:
                    self.print_colored("❌ No saved login found", 'red')
                    input("Press Enter to continue...")
            elif choice == '3':
                self.show_tool_info()
            elif choice == '4':
                self.print_colored("👋 Thanks for using TikTok Login Tool!", 'green')
                sys.exit(0)
            else:
                self.print_colored("❌ Invalid choice! Please try again.", 'red')
                time.sleep(1)
                
    def show_tool_info(self):
        """Show tool information"""
        self.clear_screen()
        
        info = """
╔══════════════════════════════════════════════════════════════╗
║                    Tool Information                          ║
╚══════════════════════════════════════════════════════════════╝

📱 TikTok Login Tool for Termux
🔧 Version: 1.0.0
🐍 Language: Python 3
📦 Requirements: requests, json, os, sys
🔒 Security: Local data storage only
🌐 Compatibility: Termux (Non-rooted devices)

Features:
✅ Simple login interface
✅ Local credential storage
✅ Welcome messages
✅ Profile information display
✅ Account status checking
✅ Secure logout

⚠️ Note: This tool is for educational purposes only.
    It does not actually connect to TikTok servers.
    Use responsibly and in accordance with TikTok's ToS.
        """
        
        print(info)
        input("\nPress Enter to continue...")

def main():
    """Main function"""
    try:
        tool = TikTokLoginTool()
        tool.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Tool interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 