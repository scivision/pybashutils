#!/bin/bash
# gets public IP address and displays in Terminal
# Michael Hirsch
# https://scivision.co
#
# Note: if you get error message curl: (77) error setting certificate verify locations:
# curl can't find your certificates. Fix this by:
#
# sudo mkdir -p /etc/pki/tls/certs
# sudo ln /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
#
# Ref: http://stackoverflow.com/questions/3160909/how-do-i-deal-with-certificates-using-curl-while-trying-to-access-an-https-url
#

url=('https://api.ipify.org' 'http://v4.ident.me' 'http://ipecho.net/plain' 'http://wtfismyip.com/text')

for u in ${url[@]}; do
 if curl -s -m 4 $u; then echo; break
 fi
done






