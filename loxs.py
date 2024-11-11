#!/usr/bin/python3

VERSION = 'v1.3'

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'
    UNBOLD = '\033[22m'
    ITALIC = '\033[3m'
    UNITALIC = '\033[23m'

try:
    import os
    from git import Repo
    from flask import session
    import sys
    import subprocess
    from colorama import Fore, Style, init
    from time import sleep
    from rich import print as rich_print
    from rich.panel import Panel
    from rich.table import Table
    import urllib3
    from rich.panel import Panel

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu():
        title = r"""
     ____           ____  ___                
    |    |    _____ \   \/  /  ______
    |    |   /     \ \     /  /  ___/
    |    |__(   O  / /     \  \___  \
    |_______/\____/ /___/\  \ /_____/ 
                          \_/                 
    """
        print(Color.ORANGE + Style.BRIGHT + title.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        border_color = Color.CYAN + Style.BRIGHT
        option_color = Fore.WHITE + Style.BRIGHT  
        
        print(border_color + "┌" + "─" * 61 + "┐")
        
        options = [
            "1] LFi Scanner",
            "2] OR Scanner",
            "3] SQLi Scanner",
            "4] XSS Scanner",
            "5] CRLF Scanner",
            "6] tool Update",
            "7] Exit"
        ]
        
        for option in options:
            print(border_color + "│" + option_color + option.ljust(61) + border_color + "│")
        
        print(border_color + "└" + "─" * 61 + "┘")
        authors = "Created by: Coffinxp, 1hehaq, HexSh1dow, Naho, AnonKryptiQuz"
        instructions = "Select an option by entering the corresponding number:"
        
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        print(Fore.WHITE + Style.BRIGHT + authors.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)
        print(Fore.WHITE + Style.BRIGHT + instructions.center(63))
        print(Fore.WHITE + Style.BRIGHT + "─" * 63)

    def print_exit_menu():
        clear_screen()

        panel = Panel(r"""
 ______               ______              
|   __ \.--.--.-----.|   __ \.--.--.-----.
|   __ <|  |  |  -__||   __ <|  |  |  -__|
|______/|___  |_____||______/|___  |_____|
        |_____|              |_____|      
   
  Credit: Coffinxp - 1hehaq - HexSh1dow - AnonKryptiQuz - Naho
            """,
            style="bold green",
            border_style="blue",
            expand=False
        )

        rich_print(panel)
        print(Color.RED + "\n\nSession Off..\n")
        sys.exit(0)

    def run_update():
        from packaging import version
        import requests
        from rich.console import Console
        from rich.panel import Panel
        from rich.progress import Progress
        
        console = Console()
        def display_update_intro():
            panel = Panel(
                r"""
██    ██ ███████ ███████  ███████ ████████ ███████ 
██    ██ ██   ██ ██    ██ ██   ██    ██    ██      
██    ██ ███████ ██    ██ ███████    ██    █████   
██    ██ ██      ██    ██ ██   ██    ██    ██      
████████ ██      ███████  ██   ██    ██    ███████ 
        """,
                title="LOXS UPDATER",
                expand=False,
                border_style="blue",
                style="bold green",
            )
            console.print(panel)
            console.print("[cyan] Welcome to the loxs updater![/cyan]\n")

        def get_latest_release(repo_owner, repo_name):
            url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
            try:
                response = requests.get(url)
                response.raise_for_status()
                release_data = response.json()
                return release_data['tag_name'], release_data
            except requests.exceptions.RequestException as e:
                console.print(f"[red][!] Error fetching release information: {e}[/red]")
                return None, None

        def get_current_version():
            try:
                with open(__file__, 'r') as file:
                    for line in file:
                        if line.startswith('VERSION ='):
                            return line.split('=')[1].strip().strip("'\"")
            except IOError as e:
                console.print(f"[red][!] Error reading current version: {e}[/red]")
            return None

        def download_update(download_url, file_path):
            try:
                with Progress() as progress:
                    task = progress.add_task("[cyan]Downloading update...", total=100)
                    response = requests.get(download_url, stream=True)
                    response.raise_for_status()
                    total_size = int(response.headers.get('content-length', 0))
                    block_size = 1024
                    with open(file_path, 'wb') as file:
                        for data in response.iter_content(block_size):
                            size = file.write(data)
                            progress.update(task, advance=(size/total_size)*100)
                console.print("[green][✓] Update downloaded successfully.[/green]")
                return True
            except requests.exceptions.RequestException as e:
                console.print(f"[red][!] Error downloading update: {e}[/red]")
                return False

        def normalize_version(v):
            # Remove 'v' prefix if present
            # v = v.lstrip('v')

            # Three components (major.minor.patch)
            parts = v.split('.')
            while len(parts) < 3:
                parts.append('0')
            return '.'.join(parts)

        display_update_intro()

        repo_owner = "coffinxp"
        repo_name = "loxs"
        current_version = get_current_version()

        if current_version is None:
            console.print("[yellow][!] Unable to find current version.[/yellow]")
            input("\nPress Enter to return to the main menu...")
            return

        console.print(f"[cyan][i] Current version: {current_version}[/cyan]")
        console.print("[cyan][i] Checking for updates...[/cyan]")

        latest_version, release_data = get_latest_release(repo_owner, repo_name)

        if latest_version is None:
            console.print("[yellow][!] Unable to check for updates.[/yellow]")
            input("\nPress Enter to return to the main menu...")
            return

        current_v = version.parse(normalize_version(current_version))
        latest_v = version.parse(normalize_version(latest_version))

        if latest_v > current_v:
            console.print(f"[green][✓] New version available: {latest_version}[/green]")
            update_choice = console.input("[cyan][?] Do you want to update? (y/n): [/cyan]").lower().strip()
            
            if update_choice == 'y':
                try:
                    download_url = release_data['assets'][0]['browser_download_url']
                    
                    if download_update(download_url, __file__):
                        console.print("[green][✓] Update completed. Please restart loxs..!![/green]")
                    else:
                        console.print("[red][!] Update failed.[/red]")
                except (KeyError, IndexError) as e:
                    console.print(f"[red][!] Error fetching release assets: {e}[/red]")
            else:
                console.print("[yellow][i] Update cancelled.[/yellow]")
        else:
            console.print("[green][✓] You are already using the latest version.[/green]")
            console.print(f"[cyan][i] Current version: {current_version}[/cyan]")
            console.print(f"[cyan][i] Latest version: {latest_version}[/cyan]")

        input("\nPress Enter to return to the main menu...")


    def handle_selection(selection):
        try:
            if selection == '1':
                clear_screen()
                os.system("python3 tool/lfi.py")

            elif selection == '2':
                clear_screen()
                os.system("python3 tool/or.py")

            elif selection == '3':
                clear_screen()
                os.system("python3 tool/sqli.py")

            elif selection == '4':
                clear_screen()
                os.system("python3 tool/xss.py")

            elif selection == '5':
                clear_screen()
                os.system("python3 tool/crlf.py")

            elif selection == '6':
                clear_screen()
                run_update()
                clear_screen()

            elif selection == '7':
                clear_screen()
                sys.exit(0)

        except KeyboardInterrupt:
            sys.exit(0)


    def main():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        clear_screen()        
        while True:
            try:
                display_menu()
                choice = input(f"\n{Fore.CYAN}[?] Select an option (0-7): {Style.RESET_ALL}").strip()
                handle_selection(choice)
                
            except KeyboardInterrupt:
                print_exit_menu()
                sys.exit(0)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print_exit_menu()
            sys.exit(0)

            
except KeyboardInterrupt:
    print_exit_menu()
