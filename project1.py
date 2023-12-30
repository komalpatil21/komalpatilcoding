#include<stdio.h>
#include<stdio.h>
#include<time.h>

int main()
{
     int number, guess,nguesses=1;
     srand(time(0));

     number = rand()%100 + 1;

     do
     {
         printf("Guess the number between 1 to 100\n");
         scanf("%d",&guess);
       if(guess>number)
         {
             printf("you guess to high\n")

          }
         else if(guess<number)
         {
             printf("you guessd too low\n");

             }
         else
         {
             printf("You guessed the correct number");
             printf("attempts : %d\n", nguesses);

          }
         nguesses++;
         }while(guess!=number);
         return 0;
         
         


    }
