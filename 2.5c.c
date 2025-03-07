/*
 for loop sum
 */

 #include <stdio.h>
 #include <stdlib.h>
 
 int main(int argc, char *argv[]) {
     if (argc < 2) {
         printf("Usage: %s num1 num2 ...\n", argv[0]);
         return 1;
     }
 
     int sum = 0;
     
     // sum
     for (int i = 1; i < argc; i++) {
         sum += atoi(argv[i]);  // add
     }
 
     // print
     printf("Sum: %d\n", sum);
 
     return 0;
 }
 