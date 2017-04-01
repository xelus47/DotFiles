#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## OS/software-specific configurations
source ~/.bash_configs

## Aliases
source ~/DotFiles/aliases.sh
#PS1='\W \033[32m\$\033[0m\033[?25h '
PS1=''
#PS1+='\[\e[33m\]➞ '
PS1+='\[\e[0m\]'
PS1+='\W'
PS1+='\[\e[0m\]'
PS1+='\[\e[34m\]'
PS1+='\[\e[0m\] '
PS1+='$($HOME/DotFiles/git-prompt)'
PS1+='\[\033[1m\033[32m\]\$\[\033[0m\033[?25h\] '
