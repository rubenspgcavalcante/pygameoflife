Resources
===========

##Library
Will store shared objects and DLLs

##Qt directory
Will store all Qt related files

##Audio directory
Contains the music and sound fx

##Cache directory
Will store dinamic generated images from the src directory

##Static directory
Will store only static images

###Rules
The files in src will be builded with the command 'genimg', following the respective rules
In src

####Sprites
All the directories must be in the {entity}-frames name format, where entity is the respective entity. (see sample-frames example in src dir).  
The images must have the name as XX.png where XX is a number that indicates his order in the sprite.
All the images must have the same height and width.
