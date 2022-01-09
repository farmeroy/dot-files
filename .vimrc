

" BASIC SETTINGS -------------------------------------------------- {{{

" Colorscheme
" :colorscheme molokai
:colorscheme iceberg
  
" disable vi compatibility which can cause issues
:set nocompatible

" Enable file type detection
:filetype on

" Enable plugins and load plugin for the detected file type
:filetype plugin on
" Load an indent file for the detected fileType
:filetype indent on

"Highlight cursor line
:set cursorline
"Highlight cursor vertically
":set cursorcolumn

:syntax on
:set number
:set showmode

" Show partial command you type in last line
:set showcmd
:set title
:set expandtab
:set tabstop=2
:set shiftwidth=2
:set nobackup
:set list
" :set listchars=tab:➤\ 
" :set listchars=trail:・
" set command history 
:set scrolloff=8
:set history=1000
"AUTOCOMPLETION
" enable auto completetion after pressing TAB
:set wildmenu
" set wildmenu to behave like Bash completion
:set wildmode=list:longest


" }}}


" FOLDING SETTINGS --------------------------------------------------{{{
" fold when the code is indented
:set foldmethod=indent
"where to begin fold 
:set foldcolumn=1
:let javascript_fold=1
:let python_fold=1
"start file with all folds open
:set foldlevelstart=99

"}}}



" SEARCH SETTINGS ---------------------------------------------- {{{
" highlight characters as you search
:set incsearch
" ignore case during search
:set ignorecase
" Overrise ignore case if searcing for Capital letters
:set smartcase
" show matching words during a search
:set showmatch
" use highlighting during search
:set hlsearch

" }}}


" FILETYPE SPECIFIC FORMATTING ---------------------------------- {{{

"set python tabs
:autocmd Filetype python setlocal tabstop=4 shiftwidth=4 softtabstop=4 expandtab
:let g:python_host_prog = '/Library/Frameworks/Python.framework/Versions/3.9/bin/python'
" basic auto complete
" :autocmd Filetype javascript set omnifunc=javascriptcomplete#CompleteJS

au FileType javascript setlocal formatprg=prettier
au FileType javascript.jsx setlocal formatprg=prettier
au FileType typescript setlocal formatprg=prettier\ --parser\ typescript
au FileType html setlocal formatprg=js-beautify\ --type\ html
au FileType scss setlocal formatprg=prettier\ --parser\ css
au FileType css setlocal formatprg=prettier\ --parser\ css



let g:ale_linters = {
\   'javascript': ['eslint'],
\   'vue': ['eslint'],
\   'react': ['eslint']
\}
let g:ale_fixers = {
  \    'javascript': ['eslint'],
  \    'typescript': ['prettier', 'tslint'],
  \    'vue': ['eslint'],
  \    'scss': ['prettier'],
  \    'html': ['prettier'],
  \    'reason': ['refmt']
\}
let g:ale_fix_on_save = 1

let g:prettier#config#single_quotes = 'true'
" }}}


" PLUGINS -------------------------------------------------{{{

call plug#begin('~/.vim/plugged')
:packloadall

  Plug 'dense-analysis/ale'
  Plug 'vim-airline/vim-airline'
  Plug 'preservim/nerdtree'

  Plug 'prettier/vim-prettier'
  
  Plug 'othree/yajs.vim'

  " Plug 'yuezk/vim-js'
  " Plug 'maxmellon/vim-jsx-pretty'
  Plug 'pangloss/vim-javascript' 
  Plug 'chemzqm/vim-jsx-improve'

  Plug 'tpope/vim-commentary'
  Plug 'tpope/vim-fugitive'
  " auto complete
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'jiangmiao/auto-pairs'
  " colorscheme
  " Plug 'romgrl/doom-one.vim'
  " Plug 'whatyouhide/vim-gotham'
  Plug 'kamykn/spelunker.vim'
  Plug 'kamykn/popup-menu.nvim'
  call plug#end()
"}}}

"MAPPINGS -----------------------------------------{{{

" mappings go in here. 

" remap the escape key for insert mode
:inoremap jk <Esc>
" Pressing the letter o will open a new line below the current one.
" Exit insert mode after creating a new line above or below the current line.
:nnoremap o o<esc>
:nnoremap O O<esc>

" Yank from cursor to the end of line.
nnoremap Y $


" You can split the window in Vim by typing :split or :vsplit.
" Navigate the split view easier by pressing CTRL+j, CTRL+k, CTRL+h, or CTRL+l.
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l

" NERDTree specific mappings.
" Map the F3 key to toggle NERDTree open and close.
nnoremap <c-t> :NERDTreeToggle<cr>

" }}}


" VIMSCRIPT ------------------------------------------------------------ {{{

" This enables code volding
" Marker folding method
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END

" more vimscripts go here

" }}}
"
" SKELETONS
" ---------------------------------------------------------------{{{
autocmd BufNewFile *.jsx 0r ~/.vim/skeletons/react-func-comp.jsx
autocmd BufNewFile *.html 0r ~/.vim/skeletons/html-boilerplate.html
"  }}}

" Plugin Settings ---------------------------------------------{{{
" spelunker settings 
let g:spelunker_disable_uri_checking = 1
let g:spelunker_disable_email_checking = 1

" }}}

