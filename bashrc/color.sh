#!/bin/bash

# syntax:
# color.sh [foreground][[background]]
# 
# examples:
# color.sh 	--> reset color
# color.sh r	--> red foreground
# color.sh cy	--> cyan foreground, yellow background (ew)
# color.sh cry	--> same as above
# color.sh grB	--> green on red, bold
# color.sh bU	--> blue text, underlined

animals=( ["moo"]="cow" ["woof"]="dog")
colors=(["z"]="0"
	["r"]="1"
	["g"]="2"
	["y"]="3"
	["b"]="4"
	["m"]="5"
	["c"]="6"
	["w"]="7" )


ARGV=("$@")
echo $ARGV
