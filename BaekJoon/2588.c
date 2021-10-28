    #include <stdio.h>

    int main(){
        int a,b;
        scanf("%d %d", &a,&b);

        int n3 = ("%d\n", a * b%10);
        int n4 = printf("%d\n", a * b%10 % 10);
        int n5 = printf("%d\n", a * b/ 100);

        printf("%d\n", n3);
        printf("%d\n", n4);
        printf("%d\n", n5);
        printf("%d", n3 * 100 + n4 * 10 + n3);

        return 0;
    }