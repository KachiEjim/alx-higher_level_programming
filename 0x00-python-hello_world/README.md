0x00-python-hello_world tasks README.md file


TASK 0: Write a Shell script that runs a Python script.

PSEUDOCODE:
1. Add a shebang for the script.
	- Run the Python script using 'python3 filename'.

EXPLANATION:
- We start by adding a shebang (#!/bin/bash) at the beginning of the script.
  This informs the shell to treat the following lines as Bash commands.

- We then execute the Python script by running 'python3 filename', where 'filename' is
  the name of the Python script we want to run.

NOTE:
- When a script with a shebang is executed, it spawns a new process to execute the specified command.

- In this script, two processes are created: one to run the Bash script and another to run the Python script.
TASK 1: Write a Shell Script that Runs Python Code
OBJECTIVE:
	- Create a bash script to execute a single-line Python code using the -c flag.
	
EXPLANATION:  
	- When running a Python code using PYTHON3 <ourcode.py>, the interpreter attempts to open the file <ourcode.py> and execute the code line by line.
	
	- If the file isn't a Python script or doesn't exist, the interpreter will raise an error: < can't open file '/root/print("hello")': [Errno 2] No such file or directory>. 
	
	- To run a Python code in one line, use the -c flag along with the Python interpreter command. The -c flag instructs the interpreter to execute the provided code directly from the command line instead of reading it from a file.


TASK 2: Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

OBJECTIVE:
	- Demonstrate the use of the print built-in function to output text to the standard output.

	
TASK 3: Your mission is to complete this source code to print the integer stored in the 'number' variable, followed by 'Battery street', and then a new line.

OBJECTIVE:
	- Illustrate the usage of string formatting in the print function to display an integer.

NOTE:
	- F-strings, a relatively recent addition to Python, provide a concise and powerful way to format strings.
	- F-strings are not a string method but an inherent feature in Python designed to enhance string formatting.
	- Both the .format string method and the str.format method achieve the same goal, differing only in how they are invoked.

TASK 4: Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

OBJECTIVE:
	- demonstrates the use of f-strings or .format string method to format and display a floating-point number with specific formatting, making it useful for presenting numeric data with precision in output messages or reports.

TASK 5: Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

OBJECTIVE:
	- Demonstrate how strings works in python, and how string can be repeated with multiplication
	- Also show how string slicing is done

EXPLANATION:
	- In Python, a string can be repeated without the need for loops using simple multiplication. Multiplying a string by a specific number will replicate the string that number of times.
	- To achieve the desired outcome, you can slice a string to extract a specific portion of it. String slicing allows you to retrieve a substring by specifying the start and end positions within the original string.



TASK 6: Complete this source code to print Welcome to Holberton School!

OBJECTIVE:
	- Illustrate the concept of string concatenation in Python using the + operator.
	- Show how to combine or join two or more strings together to create a single, concatenated string.
EXPLANATION:
	- In Python, the + operator is used to concatenate or join two or more strings. When you use the + operator with strings, it combines them into a single string by joining them together.



TASK 7:

OBJECTIVE:
	- Showcase the concept of string slicing in Python.
	- Highlight how string slicing allows you to easily access and extract specific segments of a string.
	
EXPLANATION:
	- String slicing in Python is a powerful feature that enables us to extract specific parts of a string by specifying a starting and ending point.
	- In Python, we can use both positive and negative indices to slice strings. For example, using index -1 gives you the last element of the string. Additionally, you can specify a range to slice a portion of the string between two indices.

TASK 8: Complete this source code  to print object-oriented programming with Python, followed by a new line.

OBJECTIVE:
	- Demonstrate the use of string slicing in Python.
	- Illustrate the versatility of string slicing and its ability to extract specific portions of a string.


TASK 9: Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

OBJECTIVE:
	- Illustrate how to output "The Zen of Python" to the standard output.
	
EXPLANATION:
	- By running the command import this in a Python interpreter, "The Zen of Python" will be printed to the standard output, with each aphorism displayed line by line.


TASK 10: Write a function in C that checks if a singly linked list has a cycle in it.

OBJECTIVE:
	- The objective is to write a C function, check_cycle, that checks whether a given singly linked list has a cycle.
	- If yes the function returns 1, otherwise the function returns 0.

PUSEDOCODE:
1. Begin 
2. Create a function named check_cycle that takes a singly linked list (listint_t) as an argument and returns an int. 
3. Create two pointers, slow and fast, initially both pointing to the head of the linked list.
4. Check if the linked list is empty or has only one node (i.e., if list is null or list->next is null). 
	-  If yes, return 0 to indicate no cycle. 
5. Use a loop while slow and fast's next and fast's next's next are not null: 
	- Check if fast is equal to slow. 
		○ If yes, return 1 to indicate the presence of a cycle. 
	- Increment the slow pointer by one node (slow->next). 
	- Increment the fast pointer by two nodes (fast->next->next).
6. If the loop completes without finding a cycle, return 0. 7. End

EXPLANATION: 
	- The objective is to create a C function, check_cycle, that can determine the presence of a cycle within a singly linked list.
	- The function operates by using two pointers: slow and fast. The slow pointer advances one node at a time, while the fast pointer advances two nodes at a time.
	- Initially, the function checks if the linked list is empty or has only one node. If either of these conditions is met, there cannot be a cycle, so it returns 0.
	- If the list is not empty and contains at least two nodes, the function enters a loop. During each iteration, it checks if the fast pointer has caught up to the slow pointer. If this occurs, it indicates the presence of a cycle, and the function returns 1.
	- If the loop completes without detecting a cycle, it returns 0 to indicate no cycle is present.





TASK 11: Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

OBJECTIVE:
	- Illustrate how to write to the stderr output stream using the sys.stderr.write function in Python.
	- Demonstrate how to output data to the standard error stream in Python, which is similar to the unistd library function write in C but not equivalent, as write is a system call while stderr.write is a Python function.
	- Show how to exit a Python script using the sys module's exit() function.
	
	
EXPALANATION
	- This code snippet demonstrates how to utilize the sys.stderr.write function in Python to write to the standard error (stderr) stream.
	- Unlike the print function, sys.stderr.write does not automatically append a newline character at the end of each output.





TASK 12: Write a script that compiles a Python script file.

OBJECTIVE: 
	- Illustrate how to compile a python script

EXPLANATIONS:
python3 -m compileall -b "$PYFILE" > "${PYFILE}c":

	- python3: This is the command to start the Python interpreter.

	- m The -m option tells Python to run a specific module as a script, The -m option stands for “module name”. When you pass the -m flag followed by a module name to the Python interpreter, it will locate the module and execute its contents as the __main__ module. This allows you to run a module directly from the command line1. This is because python modules usually have the code if __name__ = "__main__", when this , of code is added a python script, it prevents the script from being executed when it is imported.
	
	-  compileall: a module used to compile Python source files into bytecode.
	- The -b option tells compileall to write the compiled bytecode files to their original directory.


TASK 13: Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
             0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE

OBJECTIVE: 
	- Understand python bytecode
	
	TERMS:
	- Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter.
	- Python, like many interpreted languages, actually compiles source code to a set of instructions for a virtual machine, and the Python interpreter is an implementation of that virtual machine.
	

	1. Python bytecode: A low-level, platform-independent representation of Python source code that is used by the Python virtual machine.
	2. Python virtual machine: A stack-based interpreter that executes Python bytecode instructions and manipulates data structures such as the call stack, the evaluation stack, and the block stack.
	3. Python dis module: A standard library module that provides a disassembler for Python bytecode, allowing users to inspect and understand the bytecode of their Python functions and modules.

EXPLANATION:

	- LOAD_CONST 1 (98): This instruction loads the constant value 98 onto the stack.

	- LOAD_FAST 0 (a): This instruction loads the local variable a onto the stack.

	- LOAD_FAST 1 (b): This instruction loads the local variable b onto the stack.

	- BINARY_POWER: This instruction pops the two topmost elements from the stack, performs exponentiation (a ** b), and pushes the result back onto the stack.

	- BINARY_ADD: This instruction pops the two topmost elements from the stack, adds them together (result + 98), and pushes the result back onto the stack.

	- RETURN_VALUE: This instruction pops the topmost element from the stack and returns it as the result of the function

	


int understood = 1
endif /* understood == 1 */