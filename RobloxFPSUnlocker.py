import json
import os
import colorama
from colorama import Fore, Style

colorama.init(convert=True)

indent = Fore.RED + '____________________________________________________________________________________________________'

class FPSUnlockerApp:
    def __init__(self):
        self.target_fps = input(Fore.CYAN + "Enter the target FPS: " + Style.RESET_ALL)
        print(indent)
        self.roblox_versions = self.get_roblox_versions()
        if self.roblox_versions:
            print(Fore.GREEN + f"Detected Roblox versions: {self.roblox_versions}" + Style.RESET_ALL)
            print(indent)
        else:
            print(Fore.RED + "Failed to determine Roblox versions." + Style.RESET_ALL)

    def get_roblox_versions(self):
        roblox_versions_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Roblox", "Versions")
        if os.path.exists(roblox_versions_dir):
            versions = [version for version in os.listdir(roblox_versions_dir) if os.path.isdir(os.path.join(roblox_versions_dir, version))]
            return versions
        return None

    def save_settings(self):
        try:
            target_fps = int(self.target_fps)
            if target_fps <= 0:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Please enter a valid positive integer for Target FPS." + Style.RESET_ALL)
            print(indent)
            return

        settings = {"DFIntTaskSchedulerTargetFps": target_fps}

        if self.roblox_versions:
            for version in self.roblox_versions:
                settings_file_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Roblox", "Versions", version, "ClientSettings", "ClientAppSettings.json")
                if not os.path.exists(settings_file_path):
                    os.makedirs(os.path.dirname(settings_file_path), exist_ok=True)
                    with open(settings_file_path, 'w') as f:
                        json.dump(settings, f, indent=4)
                    print(Fore.GREEN + f"Settings saved to {settings_file_path}" + Style.RESET_ALL)
                    print(indent)
                else:
                    print(Fore.YELLOW + f"Client settings already exist for version {version}. Skipping..." + Style.RESET_ALL)
                    print(indent)
        else:
            print(Fore.RED + "Settings not saved. No Roblox versions found." + Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.RED + """
    
    
  █████▒██▓███    ██████     █    ██  ███▄    █  ██▓     ▒█████   ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓██   ▒▓██░  ██▒▒██    ▒     ██  ▓██▒ ██ ▀█   █ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒████ ░▓██░ ██▓▒░ ▓██▄      ▓██  ▒██░▓██  ▀█ ██▒▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▒  ░▒██▄█▓▒ ▒  ▒   ██▒   ▓▓█  ░██░▓██▒  ▐▌██▒▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ▒██▒ ░  ░▒██████▒▒   ▒▒█████▓ ▒██░   ▓██░░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░   ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░   ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░     ░▒ ░     ░ ░▒  ░ ░   ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░   ░░       ░  ░  ░      ░░░ ░ ░    ░   ░ ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░    ░     ░░   ░ 
                      ░        ░              ░     ░  ░    ░ ░  ░ ░      ░  ░      ░  ░   ░     
                                                                 ░                               
                            ROBLOX FPS UNLOCKER MADE BY DEVRENIX
""" + indent + Style.RESET_ALL)

    app = FPSUnlockerApp()
    app.save_settings()

input()
