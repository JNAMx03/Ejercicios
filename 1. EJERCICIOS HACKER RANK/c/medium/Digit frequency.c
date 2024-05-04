#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(){

    printf("xdxd: ");
    char s[30];
    scanf("%s", s);
    int xd[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    for(int i = 0; i < sizeof(s); i++){
        if(s[i] == i){
            xd[0] += 1 ;
        }
    }

    for(int j = 0; j < sizeof(xd); j++){
        printf("%d", xd[j]);
    }

    return 0;
}