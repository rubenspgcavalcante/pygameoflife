PyGame of Life
===========

##About

This game is based in the 'Game of Life' or simply 'Life' proposed by John Conway in a scientific [article](http://ddi.cs.uni-potsdam.de/HyFISCH/Produzieren/lis_projekt/proj_gamelife/ConwayScientificAmerican.htm) in 1970.  
It's a celular automaton wich follows a few rules

###The Rules

*For a space that is 'populated':
    *Each cell with one or no neighbors dies, as if by loneliness. 
    *Each cell with four or more neighbors dies, as if by overpopulation. 
    *Each cell with two or three neighbors survives.

*For a space that is 'empty' or 'unpopulated'
    *Each cell with three neighbors becomes populated. 

##Dependeces
*python >= 2.6.x
*pygame
*zip

To download just do *make setup* (need user to be root or have sudo privileges)

#Building and installing
To build just do *make*, and install do *make install*

##Author

Rubens Pinheiro Gonçalves Cavalcante  
email: [rubenspgcavalcante@gmail.com](mailto:rubenspgcavalcante@gmail.com)

##License & Rights

Using GNU LESSER GENERAL PUBLIC LICENSE *Version 3, 29 June 2007*  
[gnu.org](http://www.gnu.org/copyleft/gpl.html,"GPLv3")  