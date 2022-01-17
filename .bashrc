# this line makes sure to not list untracked files, only the dot files we track, when we run config status 
alias config='/usr/bin/git --git-dir=/Users/Raffles/dotfiles/ --work-tree=/Users/Raffles'

# alias tree='tree --dirsfirst -F'
alias g='git'

alias nv='nvim'

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


# just for fun commands
# View the calender by typing the first three letters of the month.

alias jan='cal -m 01'
alias feb='cal -m 02'
alias mar='cal -m 03'
alias apr='cal -m 04'
alias may='cal -m 05'
alias jun='cal -m 06'
alias jul='cal -m 07'
alias aug='cal -m 08'
alias sep='cal -m 09'
alias oct='cal -m 10'
alias nov='cal -m 11'
alias dec='cal -m 12'
