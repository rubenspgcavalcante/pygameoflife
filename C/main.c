#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "headers/game_of_life_algorithm.h"

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define true 1
#define false 0

bool testState(bool** matrix, int iterations){
    bool flag = true;

    for(int i=0; i < 3; i++){
        if(iterations % 2 == 0){
            if(matrix[1][i] != 1){
                flag = false;
            }
        }
        else if(matrix[i][1] != 1){
            flag = false;
        }
    }

    return flag;
}

int main(int argc, char *argv[]){
    bool** array = make2DArrayBool(3, 3);
    int iterTimes = 10;
    int flag = true;

    if(argc > 1 && !strcmp(argv[1],"--iterations")){
        iterTimes = atoi(argv[2]);
    }

    for (int i = 0; i < 3; i++){    
        for (int j = 0; j < 3; j++){
            array[i][j] = 0;
        }
    }

    array[1][0] = 1;
    array[1][1] = 1;
    array[1][2] = 1;

    for (int iterations = 0; iterations < iterTimes; iterations++) {
        nextGeneration(array, 3, 3);

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                printf("%d ", array[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }

    if (testState(array, iterTimes)) {
        printf("%sTest passed!%s\n", KGRN, KNRM);
        clean2DArray(array, 3);
        return 0;
    }

    else {
        printf("%sTest error\n%s", KRED, KNRM);
        clean2DArray(array, 3);
        return 1;
    }
}
