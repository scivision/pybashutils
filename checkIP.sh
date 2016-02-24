#!/bin/bash
# Michael Hirsch
# sends an email when an IP address change is detected (use with cron)
# https://scivision.co/get-email-upon-change-of-ip-address/
#
# prereq:
# -------
# sudo apt-get install mailutils
# echo "PATH=$HOME/pybashutils:$PATH" >> $HOME/.bashrc
#
# add to top of your crontab: 
# SHELL=/bin/bash
# PATH=/sbin:/bin:/usr/sbin:/usr/bin
#
YOUREMAIL="you@youremail"

#-------- program below -------------
#IPADDRESS=$(hostname -I | tr -d [:space:]) #doesn't give public IP if youre on NAT
CurIP=$(getIP) #gives public IPv4 and IPv6 separated by space
OldIP=$(tr ' ' '\n' < ~/.current_ip) #space to \n for consistency

if [[ ${CurIP} != ${OldIP} ]]; then
echo -e "IP change detected\n $CurIP \n $OldIP"
echo "Your new IP address is ${CurIP} (old address was ${OldIP} )" | mail -s "IP address change" "$YOUREMAIL"
echo -e "${CurIP}" > ~/.current_ip
fi
