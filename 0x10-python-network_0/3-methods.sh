#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | awk '/^Allow:/ {gsub(/^Allow: /, ""); print}'
