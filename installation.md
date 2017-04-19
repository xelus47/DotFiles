# How to install

0. List of key programs
- i3-gaps: fork of i3 (https://github.com/Airblader/i3)
- compton: window compositor to make it look not ugly
- termite: terminal designed for tiling window managers

1. Clone the repository. It is advised to download it straight into your home directory to make the installation easier
```bash
~ $ git clone http://github.com/xelus47/DotFiles.git
```

2. After download, to complete the installation you have to symlink the relevant files and directories. To do so, run the following commands
```bash
  $ cd ~ # cd into your home directory
# skip any of these steps if the structure already exists
~ $ mkdir .config
~ $ mkdir .config/i3 & mkdir .config/termite
```
In `DotFiles/config/gtk-3.0`, the only relevant file is
`gtk.css`, which gives `termite` its padding.
furthermore, it demonstrates the use of bookmarks that will
show up in `nautilus` the file explorer. How you install
this part is up to you. If you're me reading this, then the
the answer is almost always yes.
```bash
~ $ rm -r ~/.config/gtk-3.0 & ln -s ~/DotFiles/config/gtk-3.0 ~/.config/

# link rc files
~ $ rm ~/.vimrc
~ $ rm ~/.bashrc
~ $ ln -s DotFiles/.bashrc .
~ $ ln -s DotFiles/.vimrc .

# link config files
~ $ rm .config/i3/config
~ $ rm .config/termite/config 
~ $ ln -s ~/DotFiles/config/i3 ~/.config/i3/config
~ $ ln -s ~/DotFiles/config/gtk-3.0 ~/.config/termite/config

# link fonts
~ $ rm .fonts
~ $ ln -s DotFiles/fonts .fonts
```

3. Done!
