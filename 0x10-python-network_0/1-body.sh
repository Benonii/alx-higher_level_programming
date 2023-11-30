#!/bin/bash
# Sends a Get request tot the URL, and displays the body of the response
response=$(curl -s -w "%{http_code}" -o /dev/null $1); [ "$response" == "200" ] && curl -s "$1"
