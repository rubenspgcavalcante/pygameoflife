#include <stdio.h>
#include <stdlib.h>
#include "headers/game_of_life_algorithm.h"

#define true 1
#define false 0
typedef char bool;

int main(){

    bool** array = make2DArrayBool(3, 3);

    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            array[i][j] = 0;
        }
    }

    array[1][0] = 1;
    array[1][1] = 1;
    array[1][2] = 1;

    for(int iterations = 0; iterations < 10; iterations++){
        nextGeneration(array, 3, 3);

        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                printf("%d ", array[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    clean2DArray(array, 3);
    return 0;
}