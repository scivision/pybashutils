#!/bin/bash

du . --max-depth=1 2>/dev/null | sort --numeric-sort --reverse | head --lines=20
