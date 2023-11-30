#!/bin/bash
# Sends a post request to the provided ip
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for pld" "$1"
