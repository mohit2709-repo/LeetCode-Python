#!/bin/bash

threshold = 80

df -h | awk 'NR>1' {print $5 " " print$1}' | while read output
do
    usage = $(echo $output | awk '{print$1}' | cut -d'%' -f1)
    partition = $(echo $output | awk '{print$2}')

    if [$usage -gt threshold]; then
        echo "ALERT: $partition usage is ${usage}%"
    fi

done