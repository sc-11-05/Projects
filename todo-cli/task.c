#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "task.h"

static Task* head = NULL;
static Task* tail = NULL;
static int taskCount = 0;

// renumbering the task after deletion
void renumberTasks() {
    Task* curr = head;
    int id = 1;

    while (curr != NULL) {
        curr->id = id;
        id++;
        curr = curr->next;
    }

    taskCount = id - 1;
}

// Adding task
void addTask(char *title){
    
    if (strlen(title) == 0){
        printf("No task input was given\n\n");
        return;
    }
    
    Task* newTask = (Task* )malloc(sizeof(Task));
    if (newTask == NULL){
        printf("Memory Allocation failed!\n\n");
        return;
    }
    
    newTask-> id = taskCount + 1;
    strcpy(newTask-> title, title);
    newTask-> completed = 0;
    newTask-> next = NULL;
    
    if (head == NULL){
        head = newTask;
        tail = newTask;
    }

    else{
        tail->next = newTask;
        tail = newTask;
    }

    taskCount++;
    printf("Task Added succesfully\n\n");
    
}

// Listing tasks
void listTasks(){
    if (head == NULL){
        printf  ("No Task available\n\n");
        return;
    }

    else{
        Task* curr = head;

        while(curr != NULL){
            printf("%d. [%c] %s\n", curr->id,curr->completed? 'X': ' ', curr->title);
            curr = curr->next;
        }

    }
    printf("\n");
}

// Mark done
void markDone(int id){
    
    Task* curr = head;
    int found = 0;
    
    while(curr != NULL){
        if (curr->id == id){
            curr->completed = 1;
            found = 1;
            printf("Task Marked as done\n\n");
            break;
        }
        curr = curr->next;
    }

    if (!found){
        printf("Task not found\n\n");
    }
}

// Deleting the task


void deleteTask(int id){
    
    
    Task* curr = head;
    Task* prev = NULL;
    int found = 0;
    
    while(curr != NULL){
        if (curr->id == id){

            // Case 1: deleting head
            if (prev == NULL){
                head = curr->next;
            }
            else{
                prev->next = curr->next;
            }

            if (curr == tail){
                tail = prev;
            }

            free(curr);
            found = 1;
            printf("Task deleted successfully\n\n");
            renumberTasks();
            break;
        }

        prev = curr;
        curr = curr->next;
    }

    if (!found){
        printf("Task not found\n\n");
    }
}


// cleanup
void cleanup(){
    Task* curr = head;

    while (curr != NULL){
        Task* temp = curr;
        curr = curr->next;
        free(temp);
    }
}