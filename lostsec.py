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
    import requests
    from git import Repo
    import yaml
    import shutil
    import sys
    from urllib.parse import urlsplit
    import subprocess
    from urllib.parse import urlunsplit
    import asyncio
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

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.2 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.70",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
        ]

    WAF_SIGNATURES = {
        'Cloudflare': ['cf-ray', 'cloudflare', 'cf-request-id', 'cf-cache-status'],
        'Akamai': ['akamai', 'akamai-ghost', 'akamai-x-cache', 'x-akamai-request-id'],
        'Sucuri': ['x-sucuri-id', 'sucuri', 'x-sucuri-cache'],
        'ModSecurity': ['mod_security', 'modsecurity', 'x-modsecurity-id', 'x-mod-sec-rule'],
        'Barracuda': ['barra', 'x-barracuda', 'bnmsg'],
        'Imperva': ['x-cdn', 'imperva', 'incapsula', 'x-iinfo', 'x-cdn-forward'],
        'F5 Big-IP ASM': ['x-waf-status', 'f5', 'x-waf-mode', 'x-asm-ver'],
        'DenyAll': ['denyall', 'sessioncookie'],
        'FortiWeb': ['fortiwafsid', 'x-fw-debug'],
        'Jiasule': ['jsluid', 'jiasule'],
        'AWS WAF': ['awswaf', 'x-amzn-requestid', 'x-amzn-trace-id'],
        'StackPath': ['stackpath', 'x-sp-url', 'x-sp-waf'],
        'BlazingFast': ['blazingfast', 'x-bf-cache-status', 'bf'],
        'NSFocus': ['nsfocus', 'nswaf', 'nsfocuswaf'],
        'Edgecast': ['ecdf', 'x-ec-custom-error'],
        'Alibaba Cloud WAF': ['ali-cdn', 'alibaba'],
        'AppTrana': ['apptrana', 'x-wf-sid'],
        'Radware': ['x-rdwr', 'rdwr'],
        'SafeDog': ['safedog', 'x-sd-id'],
        'Comodo WAF': ['x-cwaf', 'comodo'],
        'Yundun': ['yundun', 'yunsuo'],
        'Qiniu': ['qiniu', 'x-qiniu'],
        'NetScaler': ['netscaler', 'x-nsprotect'],
        'Securi': ['x-sucuri-id', 'sucuri', 'x-sucuri-cache'],
        'Reblaze': ['x-reblaze-protection', 'reblaze'],
        'Microsoft Azure WAF': ['azure', 'x-mswaf', 'x-azure-ref'],
        'NAXSI': ['x-naxsi-sig'],
        'Wallarm': ['x-wallarm-waf-check', 'wallarm'],
        }
    
    init(autoreset=True)
    
    def check_and_install_packages(packages):
        for package, version in packages.items():
            try:
                __import__(package)
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu():
        title = r"""
.____                   __ ____  ___.__                
|    |    ____  _______/  |\   \/  /|  |   __________  
|    |   /  _ \/  ___/\   __\     / |  |  /  ___/  _ \ 
|    |__(  <_> )___ \  |  | /     \ |  |__\___ (  <_> )
|_______ \____/____  > |__|/___/\  \|____/____  >____/ 
        \/         \/            \_/          \/       
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
            "5] tool Update",
            "6] Exit"
        ]
        
        for option in options:
            print(border_color + "│" + option_color + option.ljust(59) + border_color + "│")
        
        print(border_color + "└" + "─" * 61 + "┘")
        authors = "Created by: Coffinxp, HexSh1dow, Naho and AnonKryptiQuz "
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
   
  Credit -  Coffinxp - HexSh1dow - AnonKryptiQuz - Naho
            """,
            style="bold green",
            border_style="blue",
            expand=False
        )

        rich_print(panel)
        print(Color.RED + "\n\nSession Off..\n")
        exit()

    def run_sql_scanner():
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

            def detect_waf(url, headers, cookies=None):
                session = get_retry_session()
                waf_detected = None

                try:
                    response = session.get(url, headers=headers, cookies=cookies, verify=False)
                    for waf_name, waf_identifiers in WAF_SIGNATURES.items():
                        if any(identifier in response.headers.get('server', '').lower() for identifier in waf_identifiers):
                            print(f"{Fore.GREEN}[+] WAF Detected: {waf_name}{Fore.RESET}")
                            waf_detected = waf_name
                            break
                except requests.exceptions.RequestException as e:
                    logging.error(f"Error detecting WAF: {e}")

                if not waf_detected:
                    print(f"{Fore.GREEN}[+] No WAF detected.{Fore.RESET}")
                
                return waf_detected

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
                return success, url_with_payload, response_time, error_message

            def get_file_path(prompt_text):
                completer = PathCompleter()
                return prompt(prompt_text, completer=completer).strip()

            def handle_exception(exc_type, exc_value, exc_traceback):
                if issubclass(exc_type, KeyboardInterrupt):
                    print(f"\n{Fore.YELLOW}Program terminated by the user!")
                    save_prompt()
                    sys.exit(0)
                else:
                    print(f"\n{Fore.RED}An unexpected error occurred: {exc_value}")
                    sys.exit(1)

            def save_prompt(vulnerable_urls=[]):
                save_choice = input(f"{Fore.CYAN}\n[?] Do you want to save the vulnerable URLs to a file? (y/n, press Enter for n): ").strip().lower()
                if save_choice == 'y':
                    output_file = input(f"{Fore.CYAN}[?] Enter the name of the output file (press Enter for 'vulnerable_urls.txt'): ").strip() or 'vulnerable_urls.txt'
                    with open(output_file, 'w') as f:
                        for url in vulnerable_urls:
                            f.write(url + '\n')
                    print(f"{Fore.GREEN}Vulnerable URLs have been saved to {output_file}")
                    os._exit(0)
                else:
                    print(f"{Fore.YELLOW}Vulnerable URLs will not be saved.")
                    os._exit(0)

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
                                print(f"{Fore.GREEN}Welcome to the Lostxlso SQL-Injector! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                        input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                        clear_screen()
                        print(f"{Fore.GREEN}Welcome to the Lostxlso SQL-Injector! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")

            def prompt_for_payloads():
                while True:
                    try:
                        payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                        if not os.path.isfile(payload_input):
                            raise FileNotFoundError(f"File not found: {payload_input}")
                        with open(payload_input) as file:
                            payloads = [line.strip() for line in file if line.strip()]
                        return payloads
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                        input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                        clear_screen()
                        print(f"{Fore.GREEN}Welcome to the Lostxlso SQL-Injector! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")

            def print_scan_summary(total_found, total_scanned, start_time):
                print(f"{Fore.YELLOW}\n[i] Scanning finished.")
                print(f"{Fore.YELLOW}[i] Total found: {total_found}")
                print(f"{Fore.YELLOW}[i] Total scanned: {total_scanned}")
                print(f"{Fore.YELLOW}[i] Time taken: {int(time.time() - start_time)} seconds")

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
                print(f"{Fore.CYAN}[i] Starting scan...")
                vulnerable_urls = []
                first_vulnerability_prompt = True

                single_url_scan = len(urls) == 1
                start_time = time.time()
                total_scanned = 0
                

                print(f"{Fore.CYAN}[i] Checking for WAF on target URLs...")
                for url in urls:
                    headers = {'User-Agent': get_random_user_agent()}
                    detect_waf(url, headers, cookies={'cookie': cookie} if cookie else None)

                try:
                    if threads == 0:
                        for url in urls:
                            for payload in payloads:
                                total_scanned += 1
                                success, url_with_payload, response_time, error_message = perform_request(url, payload, cookie)

                                if response_time >= 10:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for url in urls:
                                            list_stripped_payload = list_stripped_payload.replace(url, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.GREEN}Vulnerable: {Fore.WHITE}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                    vulnerable_urls.append(url_with_payload)
                                    if single_url_scan and first_vulnerability_prompt:
                                        continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                        if continue_scan != 'y':
                                            end_time = time.time()
                                            time_taken = end_time - start_time
                                            print(f"{Fore.YELLOW}\n[i] Scanning finished.")
                                            print(f"{Fore.YELLOW}[i] Total found: {len(vulnerable_urls)}")
                                            print(f"{Fore.YELLOW}[i] Total scanned: {total_scanned}")
                                            print(f"{Fore.YELLOW}[i] Time taken: {time_taken:.2f} seconds")
            
                                            save_prompt(vulnerable_urls)
                                            return
                                        first_vulnerability_prompt = False
                                else:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for url in urls:
                                            list_stripped_payload = list_stripped_payload.replace(url, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.RED}Not Vulnerable: {Fore.WHITE}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                    else:
                        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                            futures = []
                            for url in urls:
                                for payload in payloads:
                                    total_scanned += 1
                                    futures.append(executor.submit(perform_request, url, payload, cookie))

                            for future in concurrent.futures.as_completed(futures):
                                success, url_with_payload, response_time, error_message = future.result()

                                if response_time >= 10:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for url in urls:
                                            list_stripped_payload = list_stripped_payload.replace(url, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.GREEN}Vulnerable: {Fore.WHITE}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                    vulnerable_urls.append(url_with_payload)
                                    if single_url_scan and first_vulnerability_prompt:
                                        continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                        if continue_scan != 'y':
                                            end_time = time.time()
                                            time_taken = end_time - start_time
                                            print(f"{Fore.YELLOW}\n[i] Scanning finished.")
                                            print(f"{Fore.YELLOW}[i] Total found: {len(vulnerable_urls)}")
                                            print(f"{Fore.YELLOW}[i] Total scanned: {total_scanned}")
                                            print(f"{Fore.YELLOW}[i] Time taken: {time_taken:.2f} seconds")
            
                                            save_prompt(vulnerable_urls)
                                            return
                                        first_vulnerability_prompt = False

                                else:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:

                                        list_stripped_payload = url_with_payload
                                        for url in urls:
                                            list_stripped_payload = list_stripped_payload.replace(url, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}\n[i] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.RED}Not Vulnerable: {Fore.WHITE}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")

                    print_scan_summary(len(vulnerable_urls), total_scanned, start_time)
                    save_prompt(vulnerable_urls)

                except KeyboardInterrupt:
                    print(f"\n{Fore.YELLOW}Program terminated by the user!\n")
                    print(f"{Fore.YELLOW}[i] Total found: {len(vulnerable_urls)}")
                    print(f"{Fore.YELLOW}[i] Total scanned: {total_scanned}")
                    print(f"{Fore.YELLOW}[i] Time taken: {time_taken:.2f} seconds")
                    save_prompt(vulnerable_urls)
                    
                    sys.exit(0)

            if __name__ == "__main__":
                try:
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(main())
                except KeyboardInterrupt:
                    sys.exit(0)



    def run_xss_scanner():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        logging.getLogger('WDM').setLevel(logging.ERROR)
        init(autoreset=True)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        
        def detect_waf(url, headers, is_first_url=False):
            if not is_first_url:
                return

            session = get_retry_session()
            waf_detected = None
            try:
                response = session.get(url, headers=headers, verify=False)
                for waf_name, waf_identifiers in WAF_SIGNATURES.items():
                    if any(identifier in response.headers.get('server', '').lower() for identifier in waf_identifiers):
                        print(f"{Fore.GREEN}[+] WAF Detected: {waf_name}{Fore.RESET}")
                        waf_detected = waf_name
                        break
            except requests.exceptions.RequestException as e:
                logging.error(f"Error detecting WAF: {e}")

            if not waf_detected:
                print(f"{Fore.GREEN}[+] No WAF detected.{Fore.RESET}")

            return waf_detected

        class MassScanner:
            def __init__(self, urls, output, concurrency, timeout, payload_file, auto_continue=False):
                self.urls = urls
                self.output = output
                self.payloads = self.load_payloads(payload_file)
                self.concurrency = concurrency
                self.timeout = timeout
                self.auto_continue = auto_continue
                self.payload_file = payload_file
                self.injectables = []
                self.totalFound = 0
                self.totalScanned = 0
                self.t0 = time.time()
                self.first_vulnerability_prompt = True

            @staticmethod
            def load_payloads(payload_file):
                payloads = []

                if payload_file:
                    try:
                        with open(payload_file, "r") as file:
                            payloads = [line.strip() for line in file if line.strip()]
                            if not payloads:
                                raise ValueError("Payload file is empty.")
                            print(f"{Fore.YELLOW}\n[i] Payloads loaded from file.")
                    except Exception as e:
                        logging.error(f"Error loading payload file: {payload_file}. Exception: {str(e)}\n")
                        print(f"{Fore.RED}[!] Error loading payload file. Please check the file and try again.")
                        sys.exit(1)
                else:
                    print(f"{Fore.RED}[!] No payload file provided. Exiting.")
                    sys.exit(1)
                        
                return payloads

            def generate_payload_urls(self, url, payload):
                url_combinations = []
                try:
                    scheme, netloc, path, query_string, fragment = urlsplit(url)
                    if not scheme:
                        scheme = 'http'
                    query_params = parse_qs(query_string, keep_blank_values=True)
                    for key in query_params.keys():
                        modified_params = query_params.copy()
                        modified_params[key] = [payload]
                        modified_query_string = urlencode(modified_params, doseq=True)
                        modified_url = urlunsplit((scheme, netloc, path, modified_query_string, fragment))
                        url_combinations.append(modified_url)
                except Exception as e:
                    logging.error(f"Error generating payload URL for {url} with payload {payload}: {str(e)}")
                return url_combinations

            async def fetch(self, sem: asyncio.Semaphore, session: aiohttp.ClientSession, url: str):
                async with sem:
                    try:
                        response_text = ""
                        async with session.get(url, allow_redirects=True) as resp:
                            response_headers = resp.headers
                            content_type = response_headers.get("Content-Type", "")
                            content_length = int(response_headers.get("Content-Length", -1))

                            if "text/html" in content_type and (content_length < 0 or content_length <= 1000000):
                                content = await resp.read()
                                encoding = 'utf-8'
                                response_text = content.decode(encoding, errors="ignore")
                            else:
                                logging.info(f"Skipping URL due to content type or size: {url}")
                    except asyncio.TimeoutError:
                        logging.warning(f"Request timed out for {url}")
                    except Exception as e:
                        logging.error(f"Error fetching {url}: {str(e)}")
                            
                    await asyncio.sleep(1)
                    return (response_text, url)

            def process_tasks(self, done):
                for response_text, url in done:
                    self.totalScanned += 1
                    chrome_options = Options()
                    chrome_options.add_argument("--headless") 
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--disable-gpu")
                    service = ChromeService(executable_path=ChromeDriverManager().install())
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                    try:
                        driver.get(url)

                        try:
                            WebDriverWait(driver, 1).until(EC.alert_is_present())
                            alert = driver.switch_to.alert
                            print(Color.GREEN + f"Vulnerable URL : {url}")
                            alert.dismiss() 
                            self.injectables.append(url)
                        except:
                            print(Color.RED + "Not vulnerable")
                    finally:
                        driver.quit()

            async def scan(self):
                sem = asyncio.Semaphore(self.concurrency)
                timeout = aiohttp.ClientTimeout(total=self.timeout)

                async with aiohttp.ClientSession(timeout=timeout, connector=aiohttp.TCPConnector(ssl=False, limit=0, enable_cleanup_closed=True)) as session:
                    for payload in self.payloads:
                        print(f"{Fore.YELLOW}[i] Scanning with payload: {payload}\n")
                        pending = []
                        for url in self.urls:
                            urls_with_payload = self.generate_payload_urls(url.strip(), payload)
                            for payload_url in urls_with_payload:
                                pending.append(asyncio.ensure_future(self.fetch(sem, session, payload_url)))

                            if len(pending) >= self.concurrency:
                                done = await asyncio.gather(*pending)
                                self.process_tasks(done)
                                pending = []

                        if pending:
                            done = await asyncio.gather(*pending)
                            self.process_tasks(done)

                        if self.payload_file:
                            if self.totalFound > 0:
                                if self.first_vulnerability_prompt and not self.auto_continue:
                                    continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                    if continue_scan != 'y':
                                        break
                                    self.first_vulnerability_prompt = False
                                elif not self.auto_continue:
                                    self.first_vulnerability_prompt = False


            def save_injectables_to_file(self):
                if self.injectables:
                    with open(self.output, "w") as output_file:
                        for url in self.injectables:
                            output_file.write(url + "\n")
                    print(f"{Fore.GREEN}[+] Vulnerable URLs saved to {self.output}")


            def run(self):
                asyncio.run(self.scan())
                try:
                    print(f"{Fore.YELLOW}\n[i] Scanning finished.")
                    print(f"{Fore.YELLOW}[i] Total scanned: {self.totalScanned}")
                    print(f"{Fore.YELLOW}[i] Time taken: {int(time.time() - self.t0)} seconds\n")
                    print(f"{Fore.GREEN}[i] Vulnerabilities found: {len(self.injectables)}")

                    if self.injectables:  
                        save_option = input(f"{Fore.CYAN}[?] Do you want to save the vulnerable URLs to {self.output}? (y/n, press Enter for n): ").strip().lower()
                        if save_option == 'y':
                            self.save_injectables_to_file()
                            os._exit(0)
                        else:
                            print(f"{Fore.YELLOW}Vulnerable URLs will not be saved.")
                            os._exit(0)
                    else:
                        print(f"{Fore.YELLOW}No vulnerabilities found. No URLs to save.")
                        os._exit(0)

                except KeyboardInterrupt:
                    sys.exit(0)

                                    
            def save_injectables_to_file(self):
                with open(self.output, "w") as output_file:
                    for url in self.injectables:
                        output_file.write(url + "\n")

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
                        single_url = input(Fore.CYAN + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(Fore.RED + "[!] You must provide either a file with URLs or a single URL.")
                            input(Fore.YELLOW + "\n[i] Press Enter to try again...")
                            clear_screen()
                            print(Fore.GREEN + "Welcome to the Lostxlso XSS-Scanner! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the Lostxlso XSS-Scanner! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")

        def prompt_for_valid_file_path(prompt_text):
            while True:
                file_path = get_file_path(prompt_text).strip()
                if not file_path:
                    print(f"{Fore.RED}[!] You must provide a file containing the Payloads.")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the Lostxlso XSS-Scanner! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")
                    continue
                if os.path.isfile(file_path):
                    return file_path
                else:
                    print(f"{Fore.RED}[!] Error reading input file: {file_path}.")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the Lostxlso XSS-Scanner! - Coffinxp - HexSh1dow - AnonKryptiQuz - Naho\n")

        def main():
            clear_screen()
            time.sleep(1)
            clear_screen()
            panel = Panel(r"""
   _  __________  ____________   _  ___  __________
  | |/_/ __/ __/ / __/ ___/ _ | / |/ / |/ / __/ _  |
  >  <_\ \_\ \  _\ \/ /__/ __ |/    /    / _// , _/
/_/|_/___/___/ /___/\___/_/ |_/_/|_/_/|_/___/_/|_| 
                                                        
                                        """,
                style="bold green",
                border_style="blue",
                expand=False
            )
            
            rich_print(panel, "\n")

            print(Fore.GREEN + "Welcome to the XSS Testing Tool!\n")
            urls = prompt_for_urls()

            is_file_input = len(urls) > 1

            payload_file = prompt_for_valid_file_path("[?] Enter the path to the payload file: ")

            output_file = "vulnerable_urls.txt"
            concurrency = int(input("\n[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip() or 5)
            timeout = float(input("[?] Enter the request timeout in seconds (press Enter for 3): ").strip() or 3)
                                    
            print(f"\n{Fore.YELLOW}[i] Loading, Please Wait...")
            time.sleep(1)
            clear_screen()
            print(f"{Fore.CYAN}[i] Starting scan...")
            print(f"{Fore.CYAN}[i] Checking for WAF on target URLs...")

            detect_waf(urls[0], {'User-Agent': get_random_user_agent()}, is_first_url=True)

            scanner = MassScanner(
                urls=urls,
                output=output_file,
                concurrency=concurrency,
                timeout=timeout,
                payload_file=payload_file,
                auto_continue='n'
            )

            scanner.run()


        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                sys.exit(0)

    def run_or_scanner():

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
                print(Fore.YELLOW + f"[i] Testing payload: {payload.strip()} on {target_url}")
                driver.get(target_url)
                time.sleep(2)
                current_url = driver.current_url
                
                if current_url == "https://www.google.com/":
                    return Fore.GREEN + f"[+] Vulnerable: {target_url} redirects to {current_url}", True
                else:
                    return Fore.RED + f"[-] Not Vulnerable: {target_url} (redirects to {current_url})", False

            except TimeoutException:
                return Fore.RED + f"[-] Timeout occurred while testing payload: {payload.strip()} on {target_url}", False

            except Exception as e:
                return Fore.RED + f"[-] Error for payload {payload}: {str(e)}", False

            finally:
                if driver:
                    driver.quit()

        def test_open_redirect(url, payloads, max_threads=5):
            found_vulnerabilities = 0
            vulnerable_urls = []

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_payload_with_selenium, url, payload): payload for payload in payloads}
                for future in as_completed(future_to_payload):
                    payload = future_to_payload[future]
                    try:
                        result, is_vulnerable = future.result()
                        if result:
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + payload.strip())
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")

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
                    with open(payload_input) as file:
                        payloads = [line.strip() for line in file if line.strip()]
                    return payloads
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

        def print_scan_summary(total_found, total_scanned, start_time):
            print(Fore.YELLOW + "\n[i] Scanning finished.")
            print(Fore.YELLOW + f"[i] Total found: {total_found}")
            print(Fore.YELLOW + f"[i] Total scanned: {total_scanned}")
            print(Fore.YELLOW + f"[i] Time taken: {int(time.time() - start_time)} seconds")

        def save_results(vulnerable_urls):
            save_prompt(vulnerable_urls)

        def save_prompt(vulnerable_urls=[]):
            save_choice = input(Fore.CYAN + "\n[?] Do you want to save the vulnerable URLs to a file? (y/n, press Enter for n): ").strip().lower()
            if save_choice == 'y':
                output_file = input(Fore.CYAN + "Enter the name of the output file (press Enter for 'vulnerable_urls.txt'): ").strip() or 'vulnerable_urls.txt'
                with open(output_file, 'w') as f:
                    for url in vulnerable_urls:
                        f.write(url + '\n')
                print(Fore.GREEN + f"Vulnerable URLs have been saved to {output_file}")
                os._exit(0)
            else:
                print(Fore.YELLOW + "Vulnerable URLs will not be saved.")
                os._exit(0)

        def run_or_scanner():
            clear_screen()

            required_packages = {
                'requests': '2.28.1',
                'prompt_toolkit': '3.0.36',
                'colorama': '0.4.6'
            }
            check_and_install_packages(required_packages)

            time.sleep(1)
            clear_screen()

            panel = Panel(r"""
        ____  ___    ____________   _  ___  __________
       / __ \/ _ \  / __/ ___/ _ | / |/ / |/ / __/ _  |
      / /_/ / , _/ _\ \/ /__/ __ |/    /    / _// , _/
      \____/_/|_| /___/\___/_/ |_/_/|_/_/|_/___/_/|_| 
                                                        
                                                                
                            """,
            style="bold green",
            border_style="blue",
            expand=False
            )
            rich_print(panel, "\n")
            print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

            urls = prompt_for_urls()
            payloads = prompt_for_payloads()
            
            max_threads_input = input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip()
            max_threads = int(max_threads_input) if max_threads_input.isdigit() and 0 <= int(max_threads_input) <= 10 else 5

            print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
            time.sleep(1)
            clear_screen()
            print(Fore.CYAN + "[i] Starting scan...\n")
            print(f"{Fore.CYAN}[i] Checking for WAF on target URLs...")

            total_found = 0
            total_scanned = 0
            start_time = time.time()
            vulnerable_urls = []

            if payloads:
                for url in urls:
                    print(Fore.YELLOW + f"\n[i] Scanning URL: {url}\n")
                    found, urls_with_payloads = test_open_redirect(url, payloads, max_threads)
                    total_found += found
                    total_scanned += len(payloads)
                    vulnerable_urls.extend(urls_with_payloads)
            
            print_scan_summary(total_found, total_scanned, start_time)
            save_results(vulnerable_urls)

        if __name__ == "__main__":
            try:
                run_or_scanner()
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\nProgram terminated by the user!")
                exit(0)

    def run_lfi_scanner():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        import urllib.parse
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry

        init(autoreset=True)

        def get_random_user_agent():
            return random.choice(USER_AGENTS)
        
        def check_and_install_packages(packages):
            for package, version in packages.items():
                try:
                    __import__(package)
                except ImportError:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

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

        def detect_waf(url, headers, cookies=None):
            session = get_retry_session()
            waf_detected = None

            try:
                response = session.get(url, headers=headers, cookies=cookies, verify=False)
                for waf_name, waf_identifiers in WAF_SIGNATURES.items():
                    if any(identifier in response.headers.get('server', '').lower() for identifier in waf_identifiers):
                        print(f"{Fore.GREEN}[+] WAF Detected: {waf_name}{Fore.RESET}")
                        waf_detected = waf_name
                        break
            except requests.exceptions.RequestException as e:
                logging.error(f"Error detecting WAF: {e}")

            if not waf_detected:
                print(f"{Fore.GREEN}[+] No WAF detected.{Fore.RESET}")
            
            return waf_detected

        def test_lfi(url, payloads, success_criteria, max_threads=5):
            def check_payload(payload):
                encoded_payload = urllib.parse.quote(payload.strip())
                target_url = f"{url}{encoded_payload}"
                start_time = time.time()
                
                try:
                    response = requests.get(target_url)
                    response_time = round(time.time() - start_time, 2)
                    result = None
                    is_vulnerable = False
                    if response.status_code == 200:
                        is_vulnerable = any(re.search(pattern, response.text) for pattern in success_criteria)
                        if is_vulnerable:
                            result = Fore.GREEN + f"[+] Vulnerable: {Fore.WHITE} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                        else:
                            result = Fore.RED + f"[-] Not Vulnerable: {Fore.WHITE} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                    else:
                        result = Fore.RED + f"[-] Not Vulnerable: {Fore.WHITE} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"

                    return result, is_vulnerable
                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"[!] Error accessing {target_url}: {str(e)}")
                    return None, False

            found_vulnerabilities = 0
            vulnerable_urls = []
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_payload, payload): payload for payload in payloads}
                for future in as_completed(future_to_payload):
                    payload = future_to_payload[future]
                    try:
                        result, is_vulnerable = future.result()
                        if result:
                            print(Fore.YELLOW + f"\n[i] Scanning with payload: {payload.strip()}")
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + urllib.parse.quote(payload.strip()))
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
            return found_vulnerabilities, vulnerable_urls

        def save_results(vulnerable_urls):
            save_prompt(vulnerable_urls)

        def save_prompt(vulnerable_urls=[]):
            save_choice = input(Fore.CYAN + "\n[?] Do you want to save the vulnerable URLs to a file? (y/n, press Enter for n): ").strip().lower()
            if save_choice == 'y':
                output_file = input(Fore.CYAN + "Enter the name of the output file (press Enter for 'vulnerable_urls.txt'): ").strip() or 'vulnerable_urls.txt'
                with open(output_file, 'w') as f:
                    for url in vulnerable_urls:
                        f.write(url + '\n')
                print(Fore.GREEN + f"Vulnerable URLs have been saved to {output_file}")
            else:
                print(Fore.YELLOW + "Vulnerable URLs will not be saved.")

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
                        single_url = input(Fore.CYAN + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(Fore.RED + "[!] You must provide either a file with URLs or a single URL.")
                            input(Fore.YELLOW + "\n[i] Press Enter to try again...")
                            clear_screen()
                            print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the LFI Testing Tool! -AnonKryptiQuz x Coffinxp x Hexsh1dow x Naho\n")

        def prompt_for_payloads():
            while True:
                try:
                    payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                    if not os.path.isfile(payload_input):
                        raise FileNotFoundError(f"File not found: {payload_input}")
                    with open(payload_input) as file:
                        payloads = [line.strip() for line in file if line.strip()]
                    return payloads
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")

        def print_scan_summary(total_found, total_scanned, start_time):
            print(Fore.YELLOW + "\n[i] Scanning finished.")
            print(Fore.YELLOW + f"[i] Total found: {total_found}")
            print(Fore.YELLOW + f"[i] Total scanned: {total_scanned}")
            print(Fore.YELLOW + f"[i] Time taken: {int(time.time() - start_time)} seconds")
            exit()

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        def main():
            clear_screen()

            required_packages = {
                'requests': '2.28.1',
                'prompt_toolkit': '3.0.36',
                'colorama': '0.4.6'
            }
            check_and_install_packages(required_packages)

            time.sleep(1)
            clear_screen()

            panel = Panel(
            r"""
    __    __________   _____                                 
   / /   / ____/  _/  / ___/_________ _____  ____  ___  _____
  / /   / /_   / /    \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / /___/ __/ _/ /    ___/ / /__/ /_/ / / / / / / /  __/ /    
/_____/_/   /___/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                            
                                                      
                """,
            style="bold green",
            border_style="blue",
            expand=False
            )
            rich_print(panel, "\n")

            
            print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")

            urls = prompt_for_urls()
            payloads = prompt_for_payloads()
            success_criteria_input = input("[?] Enter the success criteria patterns (comma-separated, e.g: 'root:,admin:', press Enter for 'root:x:0:'): ").strip()
            success_criteria = [pattern.strip() for pattern in success_criteria_input.split(',')] if success_criteria_input else ['root:x:0:']
            
            max_threads_input = input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip()
            max_threads = int(max_threads_input) if max_threads_input.isdigit() and 0 <= int(max_threads_input) <= 10 else 5

            print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
            time.sleep(1)
            clear_screen()
            print(Fore.CYAN + "[i] Starting scan...\n")
            print(f"{Fore.CYAN}[i] Checking for WAF on target URLs...")

            for url in urls:
                headers = {'User-Agent': get_random_user_agent()}
                detect_waf(url, headers)

            total_found = 0
            total_scanned = 0
            start_time = time.time()
            vulnerable_urls = []

            if payloads:
                for url in urls:
                    print(Fore.YELLOW + f"\n[i] Scanning URL: {url}\n")
                    found, urls_with_payloads = test_lfi(url, payloads, success_criteria, max_threads)
                    total_found += found
                    total_scanned += len(payloads)
                    vulnerable_urls.extend(urls_with_payloads)


            print_scan_summary(total_found, total_scanned, start_time)
            
            save_results(vulnerable_urls)

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as e:
                print(Fore.RED + f"[!] An unexpected error occurred: {e}")
                sys.exit(1)

    def run_update():

        def load_config():
            config_path = "config.yml"
            if not os.path.isfile(config_path):
                print(Color.YELLOW + "[!] Configuration file not found.")
                exit()

            with open(config_path, "r") as file:
                try:
                    config = yaml.safe_load(file)
                except Exception as e:
                    print(Color.YELLOW + f"[!] Error loading configuration file: {e}")
                    exit()

            global appIdentifier, appRepo, appDir, appExecName
            try:
                appIdentifier = config['app']['identifier']
                appRepo = config['app']['repository']
                appDir = config['app']['directory']
                appExecName = config['app']['executable']
            except KeyError as e:
                print(Color.YELLOW + f"[!] Missing key in configuration file: {e}")
                exit()

            if not os.path.isdir(appDir):
                print(Color.YELLOW + f"[!] The directory specified in config.yml does not exist: {appDir}")
                exit()

        def get_remote_version(repo_url):
            try:
                repo = Repo.clone_from(repo_url, 'temp_repo', depth=1)
                latest_commit = repo.head.commit
                shutil.rmtree('temp_repo')
                return latest_commit.hexsha
            except Exception as e:
                print(Color.YELLOW + f"[!] Error accessing remote repository: {e}")
                exit()

        def get_local_version(file_path):
            if os.path.isfile(file_path):
                return os.popen(f"git log -1 --format=%H {file_path}").read().strip()
            return None

        def update_file():
            try:
                print(Color.GREEN + "[i] Updating file...")
                temp_repo_dir = 'temp_repo'
                if os.path.isdir(temp_repo_dir):
                    shutil.rmtree(temp_repo_dir)
                Repo.clone_from(appRepo, temp_repo_dir)
                source_file = os.path.join(temp_repo_dir, appExecName)
                if os.path.isfile(source_file):
                    shutil.copy(source_file, appDir)
                    print(Color.GREEN + "[i] Update completed.")
                    clear_screen()
                else:
                    print(Color.YELLOW + "[!] File to update not found in the repository.")
                shutil.rmtree(temp_repo_dir) 
            except Exception as e:
                print(Color.RED + f"[!] Error during update: {e}")
                exit()

        def run():
            load_config()
            local_version = get_local_version(os.path.join(appDir, appExecName))
            remote_version = get_remote_version(appRepo)

            if local_version != remote_version:
                print(Color.GREEN + "[i] An update is available.")
                update_file()
            else:
                print(Color.YELLOW + "[i] No update is needed.")

        if __name__ == "__main__":
            run()


    def handle_selection(selection):
        if selection == '1':
            clear_screen()
            run_lfi_scanner()

        elif selection == '2':
            clear_screen()
            run_or_scanner()

        elif selection == '3':
            clear_screen()
            run_sql_scanner()

        elif selection == '4':
            clear_screen()
            run_xss_scanner()
        elif selection == '5':
            clear_screen()
            run_update()

        elif selection == '6':
            clear_screen()
            print_exit_menu()

        else:
            print_exit_menu()

    def main():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        clear_screen()
        sleep(1)
        clear_screen()

        while True:
            display_menu()
            choice = input(f"\n{Fore.CYAN}[?] Select an option (0-6): {Style.RESET_ALL}").strip()
            handle_selection(choice)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print_exit_menu()
            
except KeyboardInterrupt:
    print_exit_menu()
