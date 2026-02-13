#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include "task.h"

int main(){
    printf("Welcome to To-Do list CLI\n");
    printf("--------------------------\n");

    while(1){
        char input[100];

        printf("Todo> ");
        if (fgets(input, sizeof(input), stdin) == NULL){
            break;
        };

        // removing the new line character
        input[strcspn(input, "\n")] = '\0';

        // add command
        if(strncmp(input, "add ", 4) == 0){
            addTask(input + 4);
        }

        // list printing

        else if (strcmp(input, "list") == 0){
            listTasks();
        }

        // task mark as done

        else if (strncmp(input, "done ", 5) == 0){
            char *idStr = input + 5;

            if (strlen(idStr) == 0){
                printf("Enter the task ID\n");
                continue;
            }

            int id = atoi(idStr);
            
            if (id <= 0) {
                printf("Invalid task ID\n");
                continue;
            }
            markDone(id);
            
            
        }

        // deleting the task
        else if (strncmp(input, "delete ", 7) == 0){
            char *idStr = input + 7;

            if (strlen(idStr) == 0){
                printf("Enter the task ID\n");
                continue;
            }

            int id = atoi(idStr);
            
            if (id <= 0) {
                printf("Invalid task ID\n");
                continue;
            }
            
            deleteTask(id);
            
            
        }


        // exit command
        else if (strcmp(input , "exit") == 0){
            break;
        }

        // handling the unknown command
        else{
            printf("Unknown command\n");
        }
    }
    cleanup();
    

    return 0;
}