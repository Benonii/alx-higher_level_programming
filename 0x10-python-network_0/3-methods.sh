#bin/bash
# Displays all HTTP methods the server will accept
curl -s -I "$1" | awk '/^Allow:/ {print $2, $3, $4}'
