#!/bin/sh

# gets public IP address and displays in Terminal

url='https://ident.me'

curl -6 -s -m 2 $url
echo
curl -4 -s -m 2 $url
echo

# Note: if you get error message curl: (77) error setting certificate verify locations, it's because curl can't find your certificates. Fix this by:
#
# mkdir -p /etc/pki/tls/certs
# ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
#
# Ref: http://stackoverflow.com/questions/3160909/how-do-i-deal-with-certificates-using-curl-while-trying-to-access-an-https-url
