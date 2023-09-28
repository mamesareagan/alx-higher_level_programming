#!/bin/bash
#sends a request to URL and display size of the response
curl -s "$1" | wc -c