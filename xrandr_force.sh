#!/bin/sh


    # RESOLUTION SETTINGS
    # This sets your VGA1 monitor to its best resolution.
    xrandr --output DVI-I-1 --mode 1440x900 --rate 60
    # This sets your laptop monitor to its best resolution.
    xrandr --output LVDS-0 --mode 1920x1028 --rate 60

    # MONITOR ORDER
    # Put the Laptop right, VGA1 monitor left
     xrandr --output DVI-I-1 --left-of LVDS-0
    # Put the Laptop left, VGA1 monitor right
    #xrandr --output LVDS --left-of VGA-0

    # PRIMARY MONITOR
    # This sets your laptop monitor as your primary monitor.
    xrandr --output LVDS-0 --primary
    # This sets your VGA monitor as your primary monitor.
    # xrandr --output VGA1 --primary
