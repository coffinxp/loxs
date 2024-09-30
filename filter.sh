#!/bin/bash

# Ask the user for the website URL or domain
read -p "Enter the website URL or domain: " website_input

# Normalize the input: Add "https://" if the input is just a domain without protocol
if [[ ! $website_input =~ ^https?:// ]]; then
    website_url="https://$website_input"
else
    website_url="$website_input"
fi

# Inform the user of the normalized URL being used
echo "Normalized URL being used: $website_url"

# Step 1: Run katana with passive sources and save output to a unified file (output.txt)
echo "Running katana with passive sources (waybackarchive, commoncrawl, alienvault)..."
echo "$website_url" | katana -ps -pss waybackarchive,commoncrawl,alienvault -f qurl | uro > output.txt

# Step 2: Run katana actively with depth 5 and append results to output.txt
echo "Running katana actively with depth 5..."
katana -u "$website_url" -d 5 -f qurl | uro | anew output.txt

# Step 3: Filter output.txt for different vulnerabilities

# XSS
echo "Filtering URLs for potential XSS endpoints..."
cat output.txt | Gxss | kxss | grep -oP '^URL: \K\S+' > xss_output.txt
echo "Extracting final filtered URLs to xss_output.txt..."

# Open Redirect
echo "Filtering URLs for potential Open Redirect endpoints..."
cat output.txt | gf or > open_redirect_output.txt

# LFI
echo "Filtering URLs for potential LFI endpoints..."
cat output.txt | gf lfi > lfi_output.txt

# SQLi
echo "Filtering URLs for potential SQLi endpoints..."
cat output.txt | gf sqli > sqli_output.txt

# Remove the intermediate file output.txt
rm output.txt

# Notify the user that all tasks are complete
echo "Filtered URLs have been saved to the respective output files:"
echo "  - XSS: xss_output.txt"
echo "  - Open Redirect: open_redirect_output.txt"
echo "  - LFI: lfi_output.txt"
echo "  - SQLi: sqli_output.txt"
