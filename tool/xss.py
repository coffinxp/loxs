try:    
    import os
    import time
    import sys
    import logging
    import asyncio
    from urllib.parse import urlsplit, parse_qs, urlencode, urlunsplit
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
    from webdriver_manager.chrome import ChromeDriverManager
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    from colorama import Fore
    from rich.console import Console
    from rich.panel import Panel
    import urllib3
    from report import generate_html_report, save_html_report

except ImportError as e:
    pass


def run_xss_scanner(scan_state=None):
    logging.basicConfig(level=logging.ERROR)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    logging.getLogger('WDM').setLevel(logging.ERROR)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    console = Console()

    def load_payloads(payload_file):
        try:
            with open(payload_file, "r") as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(Fore.RED + f"[!] Error loading payloads: {e}")
            sys.exit(0)

    def generate_payload_urls(url, payload):
        url_combinations = []
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
        return url_combinations

    async def check_vulnerability(url, payloads, vulnerable_urls, total_scanned, driver):
        for payload in payloads:
            payload_urls = generate_payload_urls(url, payload)
            if not payload_urls:
                continue
            for payload_url in payload_urls:
                print(Fore.YELLOW + f"[→] Scanning payload: {payload}")
                try:
                    driver.get(payload_url)
                    total_scanned[0] += 1
                    try:
                        WebDriverWait(driver, 1).until(EC.alert_is_present())
                        alert = driver.switch_to.alert
                        alert_text = alert.text

                        if alert_text:
                            result = Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable:{Fore.GREEN} {payload_url} {Fore.CYAN} - Alert Text: {alert_text}"
                            print(result)
                            vulnerable_urls.append(payload_url)
                        else:
                            result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}"
                            print(result)

                        alert.accept()
                    except TimeoutException:
                        result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}"
                        print(result)

                except UnexpectedAlertPresentException as e:
                    continue

    async def scan(urls, payloads, vulnerable_urls, total_scanned, concurrency, driver):
        semaphore = asyncio.Semaphore(concurrency)
        tasks = []
        for url in urls:
            tasks.append(bound_check(url, semaphore, payloads, vulnerable_urls, total_scanned, driver))
        await asyncio.gather(*tasks)

    async def bound_check(url, semaphore, payloads, vulnerable_urls, total_scanned, driver):
        async with semaphore:
            await check_vulnerability(url, payloads, vulnerable_urls, total_scanned, driver)

    def run_scan(urls, payload_file, concurrency, timeout):
        payloads = load_payloads(payload_file)
        vulnerable_urls = []
        total_scanned = [0]
        start_time = time.time()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        logging.getLogger('urllib3').setLevel(logging.CRITICAL)

        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)

        try:
            asyncio.run(scan(urls, payloads, vulnerable_urls, total_scanned, concurrency, driver))
        except Exception as e:
            print(Fore.RED + f"[!] Error during scan: {e}")
        finally:
            driver.quit()

        return vulnerable_urls, total_scanned[0], start_time


    def print_scan_summary(total_found, total_scanned, start_time):
        summary = [
            "→ Scanning finished.",
            f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
            f"• Total scanned: {total_scanned}",
            f"• Time taken: {int(time.time() - start_time)} seconds"
        ]
        for line in summary:
            print(Fore.YELLOW + line)

    def save_results(vulnerable_urls, total_found, total_scanned, start_time):
        action = input(Fore.CYAN + "[?] Do you want to generate an HTML report? (y/n): ").strip().lower()
        if action == 'y':
            html_content = generate_html_report("Cross-Site Scripting (XSS)", total_found, total_scanned, int(time.time() - start_time), vulnerable_urls)
            
            filename = input(Fore.CYAN + "[?] Enter the filename for the HTML report (e.g., report.html) or press Enter to use 'xss_report.html': ").strip()
            if not filename:
                filename = 'xss_report.html'
                print(Fore.YELLOW + "[i] No filename provided. Using 'xss_report.html'.")

            print(f"DEBUG: Chosen filename: '{filename}'")
            
            report_file = save_html_report(html_content, filename)
        else:
            print(Fore.RED + "[!] Invalid option. Exiting the program.")
            sys.exit(0)

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_file_path(prompt_text):
        completer = PathCompleter()
        return prompt(prompt_text, completer=completer).strip()

    def prompt_for_urls():
        while True:
            try:
                url_input = get_file_path("[?] Enter the path to the input file containing URLs (or press Enter to enter a single URL): ")
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
                        print(Fore.GREEN + "Welcome to the XSS Scanner!\n")
            except Exception as e:
                print(Fore.RED + f"[!] Error reading the input file. Exception: {str(e)}")
                input(Fore.YELLOW + "[i] Press Enter to try again...")
                clear_screen()
                print(Fore.GREEN + "Welcome to the XSS Scanner!\n")

    def prompt_for_valid_file_path(prompt_text):
        while True:
            file_path = get_file_path(prompt_text).strip()
            if os.path.isfile(file_path):
                return file_path
            else:
                print(Fore.RED + "[!] Error reading the input file.")
                input(Fore.YELLOW + "[i] Press Enter to try again...")
                clear_screen()
                print(Fore.GREEN + "Welcome to the XSS Scanner!\n")

    def main():
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

        console.print(panel, "\n")
        print(Fore.GREEN + "Welcome to the XSS Testing Tool!\n")
        
        urls = prompt_for_urls()
        payload_file = prompt_for_valid_file_path("[?] Enter the path to the payloads file: ")

        clear_screen()
        print(Fore.CYAN + "[i] Starting scan...\n")


        total_scanned = 0
        start_time = time.time()

        all_vulnerable_urls = []
        try:
            for url in urls:
                box_content = f" → Scanning URL: {url} "
                box_width = max(len(box_content) + 2, 40)
                print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")

                vulnerable_urls, scanned, start_time = run_scan([url], payload_file, concurrency=10, timeout=1)

                all_vulnerable_urls.extend(vulnerable_urls)
                total_scanned += scanned
        except KeyboardInterrupt:
            print(Fore.RED + "\nScan interrupted by user. Generating report...\n")

        print_scan_summary(len(all_vulnerable_urls), total_scanned, start_time)
        save_results(all_vulnerable_urls, len(all_vulnerable_urls), total_scanned, start_time)

    if __name__ == "__main__":
        main()

run_xss_scanner()