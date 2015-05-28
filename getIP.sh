#!/bin/bash
# gets public IP address and displays in Terminal
# Michael Hirsch
# https://scivision.co

url=('https://api.ipify.org' 'http://v4.ident.me' 'http://ipecho.net/plain' 'http://wtfismyip.com/text')

for u in ${url[@]}; do
 if curl -m 4 $u; then echo; break
 fi
done






