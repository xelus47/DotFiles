#!/bin/bash

var=$(pactl list sinks|grep Volume|grep front-left)
var2=${var#*/}
echo ${var2:1:4}
exit 0
