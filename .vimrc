echo ">^.^<"
:let mapleader = ",,"
:let maplocalleader = "\\"
:set number
:set relativenumber
:syntax on
:colo iceberg

:inoremap jk <Esc>
:vnoremap jk <Esc>

" select a word with space bar
:noremap <space> viw
" put a word in all caps
:inoremap <c-u>viwUi

" quick edit the .vimrc
" first open a new splint with the vimrc
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
" then source the vimrc
:nnoremap <leader>sv :source $MYVIMRC<cr>

" wrap a word in quotes
:nnoremap <leader>" viw<esc>a"<esc>bi"<esc>lel
:nnoremap <leader>' viw<esc>a'<esc>bi'<esc>lel
:vnoremap <leader>" <esc>`<i"<esc>`>ea" 
:vnoremap <leader>' <esc>`<i'<esc>`>ea'

" navigation mappings
:nnoremap L <End>
:nnoremap H <Home>

" deal with window navigation
:nnoremap <leader>l <c-w>l
:nnoremap <leader>h <c-w>h

:nnoremap <leader>j <c-w>j
:nnoremap <leader>k <c-w>l

" abbreviations are auto corrections 
:iabbrev waht what
:iabbrev tehn then
:iabbrev adn and

" autocommands
