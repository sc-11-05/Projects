# CLI To-Do Manager (C)

A simple command-line To-Do list manager implemented in C using a singly linked list with head and tail optimization.


## Features

- Add tasks
- List tasks
- Mark tasks as done
- Delete tasks
- Auto-renumbering after deletion
- O(1) insertion using tail pointer
- Modular multi-file architecture
- Proper memory cleanup


## Data Structure

This project uses a singly linked list with:

- Head pointer
- Tail pointer (for O(1) insertion)
- Dynamic memory allocation (malloc/free)
- Encapsulation via static variables


## Project Structure

main.c  → CLI interface and input handling  
task.c  → Linked list implementation  
task.h  → Public interface (function declarations)


## Compilation

Using GCC:

```
gcc main.c task.c -o todo
```
To run:
```
./todo
```

## What I Learned

- Dynamic memory management in C
- Linked list operations (insert, delete, traverse)
- Tail pointer optimization (O(1) insertion)
- Multi-file C project structure
- Header files and encapsulation
- Separate compilation and linking
