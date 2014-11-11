#!/bin/bash
#gets public IP address and displays in Terminal
# Michael Hirsch

url=('v4.ident.me' 'ipecho.net/plain' 'wtfismyip.com/text')

for u in ${url[@]}; do
 if curl -m 4 $u; then echo; break
 fi
done






