#ifndef __GAMEOFLIFEALGOH
#define __GAMEOFLIFEALGOH

typedef char bool;
bool** make2DArrayBool(int i, int j);
void clean2DArray(bool** array, int ncols);
bool** arrayCopy(bool** array, int width, int height);
void nextGeneration(bool** array, int i, int j);

#endif