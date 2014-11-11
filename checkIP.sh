#!/bin/bash

YOUREMAIL="you@youremail"

IPADDRESS=$(hostname -I | tr -d [:space:])
OldIP=$(<~/.current_ip)

if [[ ${IPADDRESS} != ${OldIP} ]]; then
echo "Your new IP address is ${IPADDRESS} (old address was ${OldIP} )" | mail -s "IP address change" $YOUREMAIL
echo ${IPADDRESS} > ~/.current_ip
fi
