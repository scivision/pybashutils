#!/bin/bash

du . --max-depth=1 | sort --numeric-sort --reverse | head --lines=20
