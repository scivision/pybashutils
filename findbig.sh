#!/bin/bash

du -hs "$1"* | sort -rh | head --lines=20
