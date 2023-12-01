#!/bin/bash
# Sends a JSON request to a URL passed as the first argument
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
