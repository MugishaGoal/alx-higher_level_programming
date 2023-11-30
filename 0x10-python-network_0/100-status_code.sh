#!/bin/bash
# A Bash script that sends a request to a URL passed as an argument
(echo -n $(curl -s -o /dev/null -w "%{http_code}" "$1"))
