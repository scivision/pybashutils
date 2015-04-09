#!/bin/bash

du -hs "$1/" 2>/dev/null | sort -rh | head --lines=20
