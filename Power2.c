#include <stdio.h>
int main(){
    int n;
    printf("Enter the Number :");
    scanf("%d", &n);
    if (n%2 == 0){
        float divf=n;
        int divi;
        for(int i=0;i<n;i++){
            divf =divf/2;
            divi=divf;
            if(divf != divi){
                printf("NO");
                return 0;
            }
            else if(divf == 1){
                printf("YES");
                return 0;
            }
        }
    }
    else{
    printf("NO");
    }
    return 0;
}