Computer System: IPO (Input Process Output Cycle) in Python
Input -----> Process -----> Output
CPU
ALU: Handles arithmetic and logical operations.
CU: Coordinates tasks.
Storage: Used to Store Programs
On behalf of Accessibility by CPU

Primary Memory: Directly accessible to CPU
e.g., RAM, ROM, Cache
Secondary Memory: Not directly accessible to CPU
e.g., HDD, SSD, Pen Drive, CD, DVD, Blu-ray disk, Memory card
On behalf of Content Retention Capacity w.r.t. Power Supply

Volatile Memory: Content is lost when power is off
e.g., RAM
Non-Volatile Memory: Content remains regardless of power supply
e.g., HDD, SSD, Pen Drive, ROM
How a Program Executes
rust
Copy code
CPU <-------> Primary Storage <-----> Secondary Storage
              (Process)               (Program)
In Python, we write code (source code) using a high-level programming language. Ultimately, the computer understands only binary, i.e., machine code.

rust
Copy code
source code -----> Interpreter -----> Binary
What an Interpreter Does
Converts source code into machine code line by line, executing it as it goes.
Stops immediately if an error exists, prompting the user to correct it.
The generated machine code is one-time use; it must be re-interpreted for each execution.
Requires more memory for execution since the interpreter must always be in memory.
Generally slower than compilers.
More secure than compilers, as it performs checks for every execution.
Examples: Python, Java
Compiler Overview
In contrast, for languages like C or C++:

rust
Copy code
CPP ------> Compiler -------> Binary
Converts source code into machine code all at once.
Reports all errors in one go.
The generated machine code is stored in HDD, allowing multiple executions without recompilation.
Does not need to be in memory for execution after compilation, making it memory efficient.
Generally faster than interpreters.
Less secure since it does not check security for every execution.
Examples: C, C++
Memory Units
4 GB = 4 x 1024 MB
4 GB = 4 x 1024 x 1024 KB
4 GB = 4 x 1024 x 1024 x 1024 B
4 GB = 2² x 2¹⁰ x 2¹⁰ x 2¹⁰ B
4 GB = 2³² B
Every memory location (1 byte) is identified using a physical address, which is hard for humans to remember (e.g., 0xAFE2:585A). Instead, we use variable names to identify memory locations in a more human-friendly way.

Example of Variable Naming in Python
python
Copy code
# Example of variable naming
user_age = 25  # This is a human-friendly name for a memory location
Using variable names makes it easier to manage and understand our code!



