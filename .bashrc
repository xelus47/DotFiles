#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## OS/software-specific configurations
source ~/.bash_configs

## Aliases
source ~/DotFiles/aliases.sh
PS1=''
PS1+='\[\e[0m\]'               # clear styling (from possible stdout from before PS1)
PS1+='\e[47m'			# below: various status messages
# PS1+='\A'			# time

_tty="$(tty)"
device=$(echo $_tty| cut -d'/' -f 3)
if [ $device != "pts" ]
	then
		PS1+='\l'	# show ttyn (unless it's /dev/pts/n)
fi
PS1+='\e[0m'
PS1+='\e[1m\e[36m\w\e[0m '           # full path name
PS1+='$($HOME/DotFiles/scripts/git-prompt.py)'  # git information
PS1+='\n'
PS1+='\W '               # shorthand directory
PS1+='\[\033[1m\033[32m\]\$\[\033[0m\033[?25h\] '
