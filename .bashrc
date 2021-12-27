# this line makes sure to not list untracked files, only the dot files we track, when we run config status 
alias config='/usr/bin/git --git-dir=/Users/Raffles/dotfiles/ --work-tree=/Users/Raffles'

# add date/time to history
HISTTIMEFORMAT="%F %T "
# ignore duplicate commands in history
HISTCONTROL=ignoredups
# number lines in active history
HISTSIZE=2000
# number of lines saved in Bash
HISTFILESIZE=2000

# use vim commands on the command line
set -o vi

