#!/bin/bash
sess_name='org'

# make sure it's closed first...
tmux kill-session -t $sess_name

# create session
tmux new -d -c $HOME -s $sess_name 'exec emacs -nw ~/org/projects.org'
tmux rename-window -t $sess_name:0 $sess_name
tmux splitw -h -t $sess_name:0 'exec ncmpcpp'
tmux selectp -t 0
tmux splitw -t $sess_name:0.0 -l 8  'exec htop'
tmux selectp -t 0
tmux attach -t $sess_name
