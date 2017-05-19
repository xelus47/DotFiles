#!/bin/bash
sess_name='matrix-panel'

# make sure it's closed first...
tmux kill-session -t $sess_name

# create session
tmux new -d -c $HOME -s $sess_name 'exec cmatrix -B'
tmux rename-window -t $sess_name:0 matrix
tmux splitw -t $sess_name:0 -l 10 'exec clock -cD -C 2' # other cool colours: 1, 3 and 6
tmux splitw -t $sess_name:0 -l 8 'exec htop'
tmux selectp -t 0
tmux attach -t $sess_name
