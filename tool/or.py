    
def openredirect():    

    try:
        from report import generate_html_report, save_html_report
        import os
        import requests
        from git import Repo
        import yaml
        import shutil
        from flask import session
        import sys
        from urllib.parse import urlsplit
        import subprocess
        from urllib.parse import urlunsplit
        import asyncio
        from selenium.webdriver.chrome.service import Service
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from curses import panel
        import random
        import re
        from wsgiref import headers
        from colorama import Fore, Style, init
        from time import sleep
        from rich import print as rich_print
        from rich.panel import Panel
        from rich.table import Table
        from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, quote
        from bs4 import BeautifulSoup
        import urllib3
        from prompt_toolkit import prompt
        from prompt_toolkit.completion import PathCompleter
        import logging
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        import argparse
        import concurrent.futures
        import time
        import aiohttp
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.common.exceptions import TimeoutException
        from concurrent.futures import ThreadPoolExecutor
        from urllib.parse import urlsplit, parse_qs, urlencode, urlunsplit
        from rich.console import Console
        from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
        import signal
        from functools import partial
        from packaging import version
        from rich.console import Console
        from rich.panel import Panel
        from rich.progress import Progress
        from rich.text import Text

    except ImportError as e:
        print(f"Error: Required module is missing: {e.name}. Please install it using 'pip install {e.name}'")
        sys.exit(0)
        
    def run_or_scanner(scan_state=None):
        init(autoreset=True)

        def get_chrome_driver():
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            options.add_argument("--window-size=1920,1080")
            from selenium.webdriver.chrome.service import Service

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.set_page_load_timeout(10)
            return driver

        def check_payload_with_selenium(url, payload):
            target_url = f"{url}{payload.strip()}"
            driver = None
            try:
                driver = get_chrome_driver()
                print(Fore.YELLOW + f"[→] {Fore.CYAN}Testing payload: {Fore.YELLOW}{payload.strip()} {Fore.CYAN}on {Fore.YELLOW}{target_url} ")
                driver.get(target_url)
                current_url = driver.current_url

                if current_url == "https://www.google.com/":
                    if scan_state:
                        scan_state['vulnerability_found'] = True
                        scan_state['vulnerable_urls'].append(target_url)
                        scan_state['total_found'] += 1
                    return Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN} {target_url} {Fore.CYAN}", True
                else:
                    return Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN}", False

            except TimeoutException:
                return Fore.RED + f"[✗]{Fore.CYAN} Timeout occurred while testing payload: {Fore.RED} {payload.strip()} {Fore.CYAN} on {target_url}", False

            except Exception as e:
                return Fore.RED + f"[✗]{Fore.CYAN} Error for payload {Fore.RED} {payload}: {str(e)}", False
            finally:
                if driver:
                    driver.quit()
                if scan_state:
                    scan_state['total_scanned'] += 1

        def test_open_redirect(url, payloads, max_threads=5):
            found_vulnerabilities = 0
            vulnerable_urls = []

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_payload_with_selenium, url, payload): payload for payload in payloads}
                try:
                    for future in as_completed(future_to_payload):
                        payload = future_to_payload[future]
                        try:
                            result, is_vulnerable = future.result()
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + payload.strip())
                        except Exception as e:
                            print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
                except KeyboardInterrupt:
                    executor.shutdown(wait=False)
                    raise

            return found_vulnerabilities, vulnerable_urls

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        def prompt_for_urls():
            while True:
                try:
                    url_input = get_file_path("[?] Enter the path to the input file containing the URLs (or press Enter to input a single URL): ")
                    if url_input:
                        if not os.path.isfile(url_input):
                            raise FileNotFoundError(f"File not found: {url_input}")
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(Fore.BLUE + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(Fore.RED + "[!] You must provide either a file with URLs or a single URL.")
                            input(Fore.YELLOW + "\n[i] Press Enter to try again...")
                            clear_screen()
                            print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

        def prompt_for_payloads():
            while True:
                try:
                    payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                    if not os.path.isfile(payload_input):
                        raise FileNotFoundError(f"File not found: {payload_input}")
                    with open(payload_input, 'r', encoding='utf-8') as f:
                        payloads = [line.strip() for line in f if line.strip()]
                    return payloads
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

        def print_scan_summary(total_found, total_scanned, start_time):
            summary = [
                "→ Scanning finished.",
                f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                f"• Total scanned: {total_scanned}",
                f"• Time taken: {int(time.time() - start_time)} seconds"
            ]
            max_length = max(len(line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')) for line in summary)
            border = "┌" + "─" * (max_length + 2) + "┐"
            bottom_border = "└" + "─" * (max_length + 2) + "┘"

            print(Fore.YELLOW + f"\n{border}")
            for line in summary:
                padded_line = line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')
                padding = max_length - len(padded_line)
                print(Fore.YELLOW + f"│ {line}{' ' * padding} │{Fore.YELLOW}")
            print(Fore.YELLOW + bottom_border)

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            if total_scanned > 0:
                generate_report = input(f"{Fore.CYAN}\n[?] Do you want to generate an HTML report? (y/n): ").strip().lower()
                if generate_report == 'y':
                    html_content = generate_html_report("Open Redirect (OR)", total_found, total_scanned, int(time.time() - start_time), vulnerable_urls)
                    filename = input(f"{Fore.CYAN}[?] Enter the filename for the HTML report: ").strip()
                    report_file = save_html_report(html_content, filename)
            else:
                print(Fore.RED + "[!] No URLs were scanned, skipping report generation.")

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')

        clear_screen()

        panel = Panel(r"""
   ____  ___    ____________   _  ___  __________
  / __ \/ _ \  / __/ ___/ _ | / |/ / |/ / __/ _  |
 / /_/ / , _/ _\ \/ /__/ __ |/    /    / _// , _/
/____//_/|_| /___/\___/_/ |_/_/|_/_/|_/___/_/|_| 
        
                        """,
            style="bold green",
            border_style="blue",
            expand=False
        )
        rich_print(panel, "\n")
        print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

        try:
            urls = prompt_for_urls()
            payloads = prompt_for_payloads()

            max_threads = 10

            print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
            clear_screen()
            print(Fore.CYAN + "[i] Starting scan...\n")

            total_found = 0
            total_scanned = 0
            start_time = time.time()
            vulnerable_urls = []

            if scan_state is None:
                scan_state = {
                    'vulnerability_found': False,
                    'vulnerable_urls': [],
                    'total_found': 0,
                    'total_scanned': 0
                }

            if payloads:
                for url in urls:
                    box_content = f" → Scanning URL: {url} "
                    box_width = max(len(box_content) + 2, 40)
                    print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                    print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                    print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n\n")
                    found, urls_with_payloads = test_open_redirect(url, payloads, max_threads)
                    total_found += found
                    total_scanned += len(payloads)
                    vulnerable_urls.extend(urls_with_payloads)

            print_scan_summary(total_found, total_scanned, start_time)
            save_results(vulnerable_urls, total_found, total_scanned, start_time)

            if scan_state['vulnerability_found']:
                print(Fore.GREEN + f"\n[+] Vulnerabilities found: {scan_state['total_found']}")
                print(Fore.GREEN + f"[+] Vulnerable URLs:")
                for url in scan_state['vulnerable_urls']:
                    print(Fore.GREEN + f"    {url}")
            else:
                print(Fore.YELLOW + "\n[-] No vulnerabilities found.")

            print(Fore.CYAN + f"\n[i] Total URLs scanned: {scan_state['total_scanned']}")

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Scan interrupted by user. Generating HTML report...")
            save_results(vulnerable_urls, total_found, total_scanned, start_time)
            if scan_state and scan_state['vulnerability_found']:
                print(Fore.GREEN + f"\n[+] Vulnerabilities found: {scan_state['total_found']}")
                print(Fore.GREEN + f"[+] Vulnerable URLs:")
                for url in scan_state['vulnerable_urls']:
                    print(Fore.GREEN + f"    {url}")
            else:
                print(Fore.YELLOW + "\n[-] No vulnerabilities found.")
                print(Fore.CYAN + f"\n[i] Total URLs scanned: {scan_state['total_scanned']}")
            os._exit(1)

    run_or_scanner()
openredirect()