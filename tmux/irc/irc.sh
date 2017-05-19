#!/bin/bash
s_name='irc'

tmux kill-session -t $s_name

tmux new -d -c $HOME/DotFiles/tmux/irc -s $s_name 'exec irssi --connect=Rizon'
tmux rename-window -t $s_name:0 $s_name
tmux splitw -h -t $s_name:0 'exec irssi --connect=PPNL'

tmux neww -n 'nickserv' -t $s_name:1 #'cd ~/DotFiles/tmux/irc'
sleep 1
tmux send './nickserv_dismiss'

#tmux neww -n 'config' -t $s_name:1 'exec vim ~/.irssi/config'
#tmux selectw -t $s_name:0
tmux selectw -t $s_name:0
tmux selectp -t 0
#echo "loading..."
#sleep 2
#tmux send -t irc:0.1 M-2 "/wc" C-m # dismiss nickserv
#tmux send -t irc:0.1 M-2 M-3       # check activity and goto ##math
#tmux send -t irc:0.0 M-2 "/wc" C-m # dismiss nickserv
#tmux send -t irc:0.0 M-2           # goto #thehappening
tmux attach -t $s_name

