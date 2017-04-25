#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## OS/software-specific configurations
source ~/.bash_configs

## Aliases
source ~/DotFiles/aliases.sh

P_PS1=''
P_PS1+="$($HOME/DotFiles/scripts/tty.sh)"
P_PS1+="$($HOME/DotFiles/scripts/pwd.py)"
P_PS1+=' $'
export P_PS1

length=${#P_PS1}


PS1=''
PS1+='\[\e[0m\]'               # clear styling (from possible stdout from before PS1)

PS1+='$($HOME/DotFiles/scripts/tty.sh)' 	# show tty message
PS1+='\[\e[1m\e[34m\]'
	PS1+='$($HOME/DotFiles/scripts/pwd.py)'
PS1+='\[\e[0m '
PS1+='\e[33m\]' # yellow
	PS1+='$($HOME/DotFiles/scripts/git-prompt.py)'  # git information
PS1+='\[\e[0m\]'
# if [ $length -ge 300 ]
# then
# PS1+='\n'
# PS1+='$($HOME/DotFiles/scripts/pwd.py -bs) '  # dir basename
# fi
PS1+='\[\e[1m\e[32m\]'
	PS1+='\$'
PS1+='\[\e[0m'
PS1+='\e[?25h\] '



