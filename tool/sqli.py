def sqli():
    try:
        from report import USER_AGENTS, clear_screen, generate_html_report, save_html_report

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
        exit()

    def run_sql_scanner(scan_state=None):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        init(autoreset=True)
        
        def get_random_user_agent():
            return random.choice(USER_AGENTS)
            
        def get_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
                session = requests.Session()
                retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
                )
                adapter = HTTPAdapter(max_retries=retry)
                session.mount('http://', adapter)
                session.mount('https://', adapter)
                return session

        def perform_request(url, payload, cookie):
            url_with_payload = f"{url}{payload}"
            start_time = time.time()
                
            headers = {
                'User-Agent': get_random_user_agent()
            }

            try:
                response = requests.get(url_with_payload, headers=headers, cookies={'cookie': cookie} if cookie else None)
                response.raise_for_status()
                success = True
                error_message = None
            except requests.exceptions.RequestException as e:
                success = False
                error_message = str(e)

            response_time = time.time() - start_time
            
            vulnerability_detected = response_time >= 10
            if vulnerability_detected and scan_state:
                scan_state['vulnerability_found'] = True
                scan_state['vulnerable_urls'].append(url_with_payload)
                scan_state['total_found'] += 1
            if scan_state:
                scan_state['total_scanned'] += 1
            
            return success, url_with_payload, response_time, error_message, vulnerability_detected

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        def handle_exception(exc_type, exc_value, exc_traceback, vulnerable_urls, total_found, total_scanned, start_time):
            if issubclass(exc_type, KeyboardInterrupt):
                print(f"\n{Fore.YELLOW}Program terminated by the user!")
                save_results(vulnerable_urls, total_found, total_scanned, start_time)
                os._exit(0)
            else:
                print(f"\n{Fore.RED}An unexpected error occurred: {exc_value}")
                os._exit(0)

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            generate_report = input(f"{Fore.CYAN}\n[?] Do you want to generate an HTML report? (y/n): ").strip().lower()
            if generate_report == 'y':
                html_content = generate_html_report("Structured Query Language Injection (SQLi)", total_found, total_scanned, int(time.time() - start_time), vulnerable_urls)
                filename = input(f"{Fore.CYAN}[?] Enter the filename for the HTML report: ").strip()
                report_file = save_html_report(html_content, filename)
                
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
                        single_url = input(f"{Fore.CYAN}[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(f"{Fore.RED}[!] You must provide either a file with URLs or a single URL.")
                            input(f"{Fore.YELLOW}\n[i] Press Enter to try again...")
                            clear_screen()
                            print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector! - Coffinxp - 1hehaq - HexSh1dow - AnonKryptiQuz - Naho\n")
                except Exception as e:
                    print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector! - Coffinxp - 1hehaq - HexSh1dow - AnonKryptiQuz - Naho\n")

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
                    print(f"{Fore.RED}[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector! - Coffinxp - 1hehaq - HexSh1dow - AnonKryptiQuz - Naho\n")

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

        def main():
            clear_screen()
            time.sleep(1)
            clear_screen()

            panel = Panel(r"""                                                       
                ___                                         
    _________ _/ (_)  ______________ _____  ____  ___  _____
   / ___/ __ `/ / /  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
  (__  ) /_/ / / /  (__  ) /__/ /_/ / / / / / / /  __/ /    
 /____/\__, /_/_/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
         /_/                                                

                    """,
            style="bold green",
            border_style="blue",
            expand=False
            )
            rich_print(panel, "\n")

            print(Fore.GREEN + "Welcome to the SQL Testing Tool!\n")

            urls = prompt_for_urls()
            payloads = prompt_for_payloads()
            
            cookie = input("[?] Enter the cookie to include in the GET request (press Enter if none): ").strip() or None

            threads = int(input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip() or 5)
            print(f"\n{Fore.YELLOW}[i] Loading, Please Wait...")
            time.sleep(1)
            clear_screen()
            print(f"{Fore.CYAN}[i] Starting scan...\n")
            vulnerable_urls = []
            first_vulnerability_prompt = True

            single_url_scan = len(urls) == 1
            start_time = time.time()
            total_scanned = 0
            total_found = 0
                
            get_random_user_agent()
            try:
                if threads == 0:
                    for url in urls:
                        box_content = f" → Scanning URL: {url} "
                        box_width = max(len(box_content) + 2, 40)
                        print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                        print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                        print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                        for payload in payloads:
                            success, url_with_payload, response_time, error_message, vulnerability_detected = perform_request(url, payload, cookie)

                            if vulnerability_detected:
                                stripped_payload = url_with_payload.replace(url, '')
                                encoded_stripped_payload = quote(stripped_payload, safe='')
                                encoded_url = f"{url}{encoded_stripped_payload}"
                                if single_url_scan:
                                    print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                    encoded_url_with_payload = encoded_url
                                else:
                                    list_stripped_payload = url_with_payload
                                    for u in urls:
                                        list_stripped_payload = list_stripped_payload.replace(u, '')
                                    encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                    encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                    print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                print(f"{Fore.GREEN}[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                vulnerable_urls.append(url_with_payload)
                                total_found += 1
                                
                            else:
                                stripped_payload = url_with_payload.replace(url, '')
                                encoded_stripped_payload = quote(stripped_payload, safe='')
                                encoded_url = f"{url}{encoded_stripped_payload}"
                                if single_url_scan:
                                    print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                    encoded_url_with_payload = encoded_url
                                else:
                                    list_stripped_payload = url_with_payload
                                    for u in urls:
                                        list_stripped_payload = list_stripped_payload.replace(u, '')
                                    encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                    encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                    print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                print(f"{Fore.RED}[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                            total_scanned += 1
                            
                else:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                        for url in urls:
                            box_content = f" → Scanning URL: {url} "
                            box_width = max(len(box_content) + 2, 40)
                            print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                            print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                            print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                            
                            futures = []
                            for payload in payloads:
                                futures.append(executor.submit(perform_request, url, payload, cookie))

                            for future in concurrent.futures.as_completed(futures):
                                success, url_with_payload, response_time, error_message, vulnerability_detected = future.result()

                                if vulnerability_detected:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for u in urls:
                                            list_stripped_payload = list_stripped_payload.replace(u, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.GREEN}[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                    vulnerable_urls.append(url_with_payload)
                                    total_found += 1
                                    if single_url_scan and first_vulnerability_prompt:
                                        continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                        if continue_scan != 'y':
                                            break
                                        first_vulnerability_prompt = False

                                else:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for u in urls:
                                            list_stripped_payload = list_stripped_payload.replace(u, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.RED}[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                total_scanned += 1

                print_scan_summary(total_found, total_scanned, start_time)
                save_results(vulnerable_urls, total_found, total_scanned, start_time)
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {str(e)}")
            finally:
                if 'executor' in locals():
                    executor.shutdown(wait=False)
                os._exit(0)

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                os._exit(0)
    run_sql_scanner()

sqli()