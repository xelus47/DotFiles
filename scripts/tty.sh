#!/bin/bash


_tty="$(tty)"
device=$(echo $_tty| cut -d'/' -f 3)
if [ $device != "pts" ]
	then
		printf '\e[30m\e[47m'
		printf $device
		printf '\e[0m'		
fi
