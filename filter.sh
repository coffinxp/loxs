#!/bin/bash

banner="""
░█▀▀░▀█▀░█░░░▀█▀░█▀▀░█▀▄
░█▀▀░░█░░█░░░░█░░█▀▀░█▀▄
░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀
"""

command -v gum &> /dev/null || { echo "gum not installed"; exit 1; }
gum style --foreground 99 --align center "$banner"
website_input=$(gum input --header "Enter your target!" --placeholder "url or domain")
[ -z "$website_input" ] && { gum log -l error "no url"; exit 1; }
output_dir=$(gum input --header "Enter output folder's name!" --placeholder "output folder (default: output)" --value "output")
[ -z "$output_dir" ] && output_dir="output"
[[ ! $website_input =~ ^https?:// ]] && website_url="https://$website_input" || website_url="$website_input"
mkdir -p "$output_dir"
gum spin --spinner dot --title "passive scan" -- bash -c "echo '$website_url' | katana -ps -pss waybackarchive,commoncrawl,alienvault -f qurl | uro > $output_dir/output.txt"
gum spin --spinner dot --title "active scan" -- bash -c "katana -u '$website_url' -d 5 -f qurl | uro | anew $output_dir/output.txt"
gum spin --spinner dot --title "xss" -- bash -c "cat $output_dir/output.txt | Gxss | kxss | grep -oP '^URL: \K\S+' | sed 's/=.*/=/' | sort -u > $output_dir/xss.txt"
gum spin --spinner dot --title "open redirect" -- bash -c "cat $output_dir/output.txt | gf or | sed 's/=.*/=/' | sort -u > $output_dir/redirect.txt"
gum spin --spinner dot --title "lfi" -- bash -c "cat $output_dir/output.txt | gf lfi | sed 's/=.*/=/' | sort -u > $output_dir/lfi.txt"
gum spin --spinner dot --title "sqli" -- bash -c "cat $output_dir/output.txt | gf sqli | sed 's/=.*/=/' | sort -u > $output_dir/sqli.txt"
rm $output_dir/output.txt
gum log -l info "xss: $(wc -l < $output_dir/xss.txt)" && gum log -l info "redirect: $(wc -l < $output_dir/redirect.txt)" && gum log -l info "lfi: $(wc -l < $output_dir/lfi.txt)" && gum log -l info "sqli: $(wc -l < $output_dir/sqli.txt)"
gum confirm "view?" && gum pager < "$output_dir/$(gum choose "xss.txt" "redirect.txt" "lfi.txt" "sqli.txt")"
