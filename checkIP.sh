#!/bin/bash
# Michael Hirsch
# sends an email when an IP address change is detected (use with cron)
# https://scivision.co/get-email-upon-change-of-ip-address/
YOUREMAIL="you@youremail"

#-------- program below -------------
IPADDRESS=$(hostname -I | tr -d [:space:])
OldIP=$(<~/.current_ip)

if [[ ${IPADDRESS} != ${OldIP} ]]; then
echo "Your new IP address is ${IPADDRESS} (old address was ${OldIP} )" | mail -s "IP address change" $YOUREMAIL
echo ${IPADDRESS} > ~/.current_ip
fi
