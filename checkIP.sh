#!/bin/bash

# Michael Hirsch, Ph.D.
# sends an email when an IP address change is detected (use with cron)
# https://scivision.dev/get-email-upon-change-of-ip-address/
#
# Note: Most home ISPs block port 25 STMP, you would need to use port 587.
# Check /var/log/mail.log to see if you're getting blocked from a simple
#   echo "testing" | mail -s test my@email.address
#
# Setup:
# -------
# 1. install a simple mail server:
# apt install mailutils
#
# 2. add to top of your crontab by "crontab -e":
# SHELL=/bin/bash
# PATH=/sbin:/bin:/usr/sbin:/usr/bin
#
# 3. add via "crontab -e" this script. I choose to run at reboot and hourly by:
#    @reboot ~/code/pybashutils/checkIP.sh my@email.address
#    @hourly ~/code/pybashutils/checkIP.sh my@email.address

set -u
emailaddr=$1

CurIP=$(hostname -I | tr -d [:space:])

OldIP=$(tr ' ' '\n' < ~/.current_ip) #space to \n for consistency

if [[ ${CurIP} != ${OldIP} ]]; then
  echo -e "IP change detected\n $CurIP \n $OldIP"
  echo "New IP address: ${CurIP} (old address: ${OldIP} )" | mail -s "IP address change: $(hostname)" "$emailaddr"
  echo -e "${CurIP}" > ~/.current_ip
fi
