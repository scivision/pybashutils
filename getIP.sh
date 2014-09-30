#!/bin/bash
#gets public IP address and displays in Terminal

IPurl3="wtfismyip.com/text"
IPurl2="ipecho.net/plain" #this one has become unreliable
IPurl="v4.ident.me"

if curl -m 4 $IPurl; then echo
elif curl -m 4 $IPurl2; then echo
else echo Could not connect to $IPurl, sorry
fi






