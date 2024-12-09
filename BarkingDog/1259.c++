#include <cstdio>

int revInt(int n){
    int m = 0;
    while(n){
        m *= 10;
        m += n%10;
        n /= 10;
    }
    return m;
}
int main(){
    int n;
    while(true){
        scanf("%d", &n);
        if(!n) return 0;
        if(revInt(n) == n) printf("yes\n");
        else printf("no\n");
    }
}