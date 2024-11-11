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


except KeyboardInterrupt:
    sys.exit(0)