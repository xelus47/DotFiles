#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## OS/software-specific configurations
[ -f ~/.bash_configs ] && source ~/.bash_configs

## Aliases
[ -f ~/DotFiles/aliases.sh ] && source ~/DotFiles/aliases.sh


PS1=''
PS1+='\[\e[0m\]'               # clear styling (from possible stdout from before PS1)

#PS1+='\[\e[33m\]» \[\e[0m\]'

PS1+='$($HOME/DotFiles/bashrc/tty.sh)' 	# show tty message
PS1+='\[\e[1m\e[34m\]'
	PS1+='$($HOME/DotFiles/bashrc/pywd.py -t 30 10)' # show path in bright blue
	PS1+='\[\e[39m\]$($HOME/DotFiles/bashrc/pywd.py -w 30 10)'
PS1+='\[\e[0m '
PS1+='\e[33m\]' # yellow
	PS1+='$($HOME/DotFiles/bashrc/git-prompt.py)'  # git information
PS1+='\[\e[0m\]'
PS1+='\[\e[1m\e[32m\]'
	PS1+='\$' # bright green indicator
PS1+='\[\e[0m'
PS1+='\e[?25h\] '
