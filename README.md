PyGame of Life 
===========

<p align="center">
  <img src="resources/static/icon.png"/>
</p>

##Build status
Last build in Travis continuous integration  
[![Build Status](https://travis-ci.org/rubenspgcavalcante/pygameoflife.png?branch=master)](https://travis-ci.org/rubenspgcavalcante/pygameoflife)

##About

This game is based in the 'Game of Life' or simply 'Life' proposed by John Conway in a scientific [article](http://ddi.cs.uni-potsdam.de/HyFISCH/Produzieren/lis_projekt/proj_gamelife/ConwayScientificAmerican.htm) in 1970.  
It's a celular automaton wich follows a few rules

#Download
To execute just run the "run-pygameoflife" executable.  
The current releases are:

*    [Windows i686](https://sourceforge.net/projects/pygame-of-life/files/pygame-of-life_Win_i686.zip/download)
*    [Linux x86-64](http://sourceforge.net/projects/pygame-of-life/files/pygame-of-life_Linux_x86_64.zip/download)

###The Rules

*    For a space that is 'populated':
    *    Each cell with one or no neighbors dies, as if by loneliness. 
    *    Each cell with four or more neighbors dies, as if by overpopulation. 
    *    Each cell with two or three neighbors survives.  
  
*    For a space that is 'empty' or 'unpopulated'
    *   Each cell with three neighbors becomes populated. 

***

##Download
Just unzip and then execute "run-pygameoflife" binary.  
  
###Current Releases
*    [Linux amd64](https://raw.github.com/rubenspgcavalcante/pygameoflife/master/releases/pygame-of-life_Linux_x86_64.zip)

*    [Windows i686](https://raw.github.com/rubenspgcavalcante/pygameoflife/master/releases/pygame-of-life_Win_i686.zip)

***

#Compiling by the source
##Dependeces
Tested in Ubuntu 12.10 LTS 64 wich the following versions
*    python >= 2.6.x
*    pygame >= 1.9.x
*    pyqt >= 4.x
*    pyrcc4-dev-tools >= 4.8.x
*    PIL >= 1.1.x
*    zip >= 3.x
*    unzip >= 5.51.x
*    cx-Freeze >= 4.3.x

##Building Installing
The first command will download and install all dependeces. (Needs apt)  
Then, will build and compile the code using cx-Freeze.  
Finnally will be installed
```
sudo make setup
make
sudo make install
```

to unistall, just run
```
sudo make unistall
```

##Author

Rubens Pinheiro Gonçalves Cavalcante  
email: [rubenspgcavalcante@gmail.com](mailto:rubenspgcavalcante@gmail.com)

##License & Rights

Using GNU LESSER GENERAL PUBLIC LICENSE *Version 3, 29 June 2007*  
[gnu.org](http://www.gnu.org/copyleft/gpl.html,"GPLv3")  