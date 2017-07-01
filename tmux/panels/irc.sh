#!/bin/bash
sess_name='side-irc'

# make sure it's closed first...
tmux kill-session -t $sess_name

# create session
tmux new -d -c $HOME -s $sess_name 'exec irssi'
tmux rename-window -t $sess_name:0 $sess_name
tmux splitw -t $sess_name:0 -l 8 'exec htop'
#tmux selectp -t 0
#tmux splitw -t $sess_name:0 -l 8 'exec tty-clock -cBD -C 2'
tmux selectp -t 0
tmux attach -t $sess_name
