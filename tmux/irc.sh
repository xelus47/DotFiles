#!/bin/bash
s_name='irc'

tmux kill-session -t $s_name

tmux new -d -c $HOME -s $s_name 'exec irssi --connect=Rizon'
tmux rename-window -t $s_name:0 chat
#tmux splitw -h -t $s_name:0 'exec irssi --connect=Freenode'
#tmux neww -n 'config' -t $s_name:1 'exec vim ~/.irssi/config'
#tmux selectw -t $s_name:0
#tmux selectp -t 0
#echo "loading..."
#sleep 2
#tmux send -t irc:0.1 M-2 "/wc" C-m # dismiss nickserv
#tmux send -t irc:0.1 M-2 M-3       # check activity and goto ##math
#tmux send -t irc:0.0 M-2 "/wc" C-m # dismiss nickserv
#tmux send -t irc:0.0 M-2           # goto #thehappening
tmux attach -t $s_name

