#!/bin/bash
sess_name='side-panel'

# make sure it's closed first...
tmux kill-session -t small_side_panel

# create session
tmux new -d -c $HOME -s $sess_name 'exec ranger'
tmux rename-window -t $sess_name:0 info
tmux splitw -t $sess_name:0 -l 8 'exec htop'
tmux selectp -t 0
tmux attach -t $sess_name
