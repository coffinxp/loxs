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

# Create an output directory if it doesn't exist
output_dir="output"
mkdir -p "$output_dir"

# Step 1: Run katana with passive sources and save output to a unified file (output/output.txt)
echo "Running katana with passive sources (waybackarchive, commoncrawl, alienvault)..."
echo "$website_url" | katana -ps -pss waybackarchive,commoncrawl,alienvault -f qurl | uro > "$output_dir/output.txt"

# Step 2: Run katana actively with depth 5 and append results to output/output.txt
echo "Running katana actively with depth 5..."
katana -u "$website_url" -d 5 -f qurl | uro | anew "$output_dir/output.txt"

# Step 3: Filter output/output.txt for different vulnerabilities

# XSS
echo "Filtering URLs for potential XSS endpoints..."
cat "$output_dir/output.txt" | Gxss | kxss | grep -oP '^URL: \K\S+' | sed 's/=.*/=/' | sort -u > "$output_dir/xss_output.txt"
echo "Extracting final filtered URLs to $output_dir/xss_output.txt..."

# Open Redirect
echo "Filtering URLs for potential Open Redirect endpoints..."
cat "$output_dir/output.txt" | gf or | sed 's/=.*/=/' | sort -u > "$output_dir/open_redirect_output.txt"

# LFI
echo "Filtering URLs for potential LFI endpoints..."
cat "$output_dir/output.txt" | gf lfi | sed 's/=.*/=/' | sort -u > "$output_dir/lfi_output.txt"

# SQLi
echo "Filtering URLs for potential SQLi endpoints..."
cat "$output_dir/output.txt" | gf sqli | sed 's/=.*/=/' | sort -u > "$output_dir/sqli_output.txt"

# Remove the intermediate file output/output.txt
rm "$output_dir/output.txt"

# Notify the user that all tasks are complete
echo "Filtered URLs have been saved to the respective output files in the 'output' directory:"
echo "  - XSS: $output_dir/xss_output.txt"
echo "  - Open Redirect: $output_dir/open_redirect_output.txt"
echo "  - LFI: $output_dir/lfi_output.txt"
echo "  - SQLi: $output_dir/sqli_output.txt"
