#ifndef __GAMEOFLIFEALGO
#define __GAMEOFLIFEALGO
#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0
typedef char bool;

/**
 * Checks if a cell will die/birth based
 * on the 3x3 neightborhood with him in center
 * Rules:
 *  living cell -> 0, 1, 4 or more -> dies
 *  living cell -> 2 or 3 -> lives
 *  dead cell   -> 3 -> rebirth
 *
 * @param bool** array The 2D matrix of cells
 * @param int posx The x position of the cell to analyse
 * @param int posy The y position of the cell to analyse
 * @param int height The matrix height
 * @param int width The matrix width
 * @returns bool If a dead cell birth or a living cell dies
 */
bool liveOrDie(bool** array, int posx, int posy, int width, int height){
    int neightbors = 0;
    for(int i = posx - 1; i <= posx + 1; i++){
        for(int j = posy - 1; j <= posy + 1; j++){
            /*
             * Verify if there is a living cell in the (i, j) taking care
             * to not overflow the corners
             */ 
            if(!(i < 0 || i >= width || j < 0 || j >= height) && !(i == posx && j == posy) && array[i][j]){
                neightbors++;
            }         
        }
    }

    //Living cell
    if(array[posx][posy]){
        if(neightbors < 2 || neightbors > 3){
            return false; //die
        }
        else{
            return true; //still alive
        }
    }
    //Dead cell
    else{
        if(neightbors == 3){
            return true; //rebirth
        }
        else{
            return false; //still dead
        }
    }
}

bool** make2DArrayBool(int i, int j){
    bool** ArrayPointer;
    ArrayPointer = (bool**) malloc(i*sizeof(bool*));

    for(int x=0; x < i; x++){
        ArrayPointer[x] = malloc(j*sizeof(bool*));
    }

    return ArrayPointer;
}

void clean2DArray(bool** array, int ncols){
    for(int i=0; i < ncols; i++){
        free(array[i]);
    }
    free(array);
}

bool** arrayCopy(bool** array, int width, int height){
    bool** bckp = make2DArrayBool(width, height);

    for(int i=0; i < width; i++){
        for(int j=0; j < height; j++){
            bckp[i][j] = array[i][j];
        }
    }

    return bckp;
}

void nextGeneration(bool** array, int i, int j){
    bool** bckp = arrayCopy(array, i, j);

    for(int x=0; x < i; x++){
        for(int y=0; y < j; y++){
            array[x][y] = liveOrDie(bckp, x, y, i, j);
        }
    }
    clean2DArray(bckp, j);
}

#endif