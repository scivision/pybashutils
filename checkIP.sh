#!/bin/bash
# Michael Hirsch
# sends an email when an IP address change is detected (use with cron)
# https://scivision.co/get-email-upon-change-of-ip-address/
#
# prereq:
# -------
# sudo apt-get install sendmail
# echo "PATH=$HOME/pybashutils:$PATH" >> $HOME/.bashrc
#
YOUREMAIL="you@youremail"

#-------- program below -------------
#IPADDRESS=$(hostname -I | tr -d [:space:]) #doesn't give public IP if youre on NAT
CurIP=$(getIP.sh) #gives public IP
OldIP=$(<~/.current_ip)

if [[ ${CurIP} != ${OldIP} ]]; then
echo "Your new IP address is ${CurIP} (old address was ${OldIP} )" | mail -s "IP address change" $YOUREMAIL
echo ${CurIP} > ~/.current_ip
fi
