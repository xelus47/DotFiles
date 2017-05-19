#!/bin/sh

echo '{ "version": 1 }'

echo '['

echo '[],'

readonly PRE='{ "full_text": "'
readonly COL='", "color": "'
readonly CER='" }'

KERNELV=$PRE"K: $(uname -sr)"$COL'#bbaacc'$CER

i=5

while :
do

if [ "$i" -eq "5" ]; then 
BATERIA=$PRE"B: $(acpi -b | awk '{print $NF}')"$COL'#ccbbaa'$CER
DISK=$PRE"D: $(df -h | awk '/sda1/ {print $5 " ("$4" Disp.)" }')"$COL'#ccaabb'$CER
UPTIME=$PRE"🕐: $(awk  '{printf "%.2f", $0/3600;}' /proc/uptime)h"$COL'#ccaabb'$CER
let i=0
fi

let i="$i+1"
CALOR=$PRE"T: $(acpi -t | awk '{print $(NF-2)}')°C"$COL'#ccbbaa'$CER

LOAD=$PRE"L: $(cat /proc/loadavg)"$COL'#ccbbaa'$CER
VOL=$PRE"♪: $(pactl list sinks | awk '/Volume: 0:/{print $NF}')"$COL'#bbccaa'$CER
FECHA=$PRE"$(date +'%A,%_d %B %Y  %H:%M:%S')"$COL'#aaccbb'$CER

echo "[$KERNELV,$UPTIME,$CALOR,$BATERIA,$LOAD,$DISK,$VOL,$FECHA]," || exit 1
sleep 5s;
done

