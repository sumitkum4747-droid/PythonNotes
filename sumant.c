#include <stdio.h>
int main(){
    int i,j;
    printf("Enter the no. of row :");
    scanf("%d", &i);
    printf("Enter the no. of column :");
    scanf("%d", &j);
    int arr[i][j];
    int a,b;
    // taking input
    for(a=0;a<i;a++){
        for(b=0;b<j;b++){
            printf("Enter the Number :");
            scanf("%d", &arr[a][b]);
        }
    }
    // printing the output
    for(a=0;a<i;a++){
        for(b=0;b<j;b++){
            printf("%d", arr[a][b]);
        }
        printf("\n");
    }
    
    
    printf("Printing the corner elements\n");
    for(a=0;a<i;a++){
        if(a==0 || a==i-1){
            for(b=0;b<j;b++){
                printf("%d", arr[a][b]);
            }
            printf("\n");
        }
        else{
            for(b=0;b<j;b++){
                if(b==0 || b==j-1){
                    printf("%d", arr[a][b]);
                }
                else{
                    printf(" ");
                }
            }
            printf("\n");
        }
    }

return 0;
}