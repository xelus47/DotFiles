#!/bin/bash

p="$(pwd)"
shortp="${p/$HOME/"~"}"
printf "$shortp"
