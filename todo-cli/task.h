#ifndef TASK_H
#define TASK_H

typedef struct task{
    int id;
    char title[100];
    int completed;
    struct task* next;
} Task;

void addTask(char *title);
void listTasks();
void markDone(int id);
void deleteTask(int id);
void cleanup();

#endif