# Computer System: IPO (Input Process Output Cycle) in Python

## Input -----> Process -----> Output

### CPU
- **ALU:** Handles arithmetic and logical operations.
- **CU:** Coordinates tasks.

### Storage: Used to Store Programs

1. **On behalf of Accessibility by CPU**
   - **Primary Memory:** Directly accessible to CPU  
     e.g., RAM, ROM, Cache
   - **Secondary Memory:** Not directly accessible to CPU  
     e.g., HDD, SSD, Pen Drive, CD, DVD, Blu-ray disk, Memory card

2. **On behalf of Content Retention Capacity w.r.t. Power Supply**
   - **Volatile Memory:** Content is lost when power is off  
     e.g., RAM
   - **Non-Volatile Memory:** Content remains regardless of power supply  
     e.g., HDD, SSD, Pen Drive, ROM

### How a Program Executes
```
CPU <-------> Primary Storage <-----> Secondary Storage
              (Process)               (Program)
```

In Python, we write code (source code) using a high-level programming language. Ultimately, the computer understands only binary, i.e., machine code.

```
source code -----> Interpreter -----> Binary
```

### What an Interpreter Does
- Converts source code into machine code line by line, executing it as it goes.
- Stops immediately if an error exists, prompting the user to correct it.
- The generated machine code is one-time use; it must be re-interpreted for each execution.
- Requires more memory for execution since the interpreter must always be in memory.
- Generally slower than compilers.
- More secure than compilers, as it performs checks for every execution.  
  **Examples:** Python, Java

### Compiler Overview
In contrast, for languages like C or C++:
```
CPP ------> Compiler -------> Binary
```
- Converts source code into machine code all at once.
- Reports all errors in one go.
- The generated machine code is stored in HDD, allowing multiple executions without recompilation.
- Does not need to be in memory for execution after compilation, making it memory efficient.
- Generally faster than interpreters.
- Less secure since it does not check security for every execution.  
  **Examples:** C, C++

### Memory Units
- 4 GB = 4 x 1024 MB  
- 4 GB = 4 x 1024 x 1024 KB  
- 4 GB = 4 x 1024 x 1024 x 1024 B  
- 4 GB = 2² x 2¹⁰ x 2¹⁰ x 2¹⁰ B  
- 4 GB = 2³² B  

Every memory location (1 byte) is identified using a physical address, which is hard for humans to remember (e.g., 0xAFE2:585A). Instead, we use variable names to identify memory locations in a more human-friendly way. 

### Example of Variable Naming in Python
```python
# Example of variable naming
user_age = 25  # This is a human-friendly name for a memory location
``` 

Using variable names makes it easier to manage and understand our code!

# What is a Variable?

## General Definition
A variable is a named memory location whose value can be changed.

## Python-Specific Definition
In Python, a variable is a reference to a memory location (called an object) that holds the value. This means that a variable does not store the value directly; instead, it stores the location of the object where the value is actually stored.

### Creating a Variable in Python
```python
variable_name = value
```

### Variable Naming Rules
1. Can consist of a combination of A-Z, a-z, 0-9, and the special symbol `_`.
2. Cannot start with a digit.
3. Cannot contain commas or spaces.
4. Must not be a reserved keyword.
5. **Convention:** Variable names should be meaningful.

### Naming Conventions
- **camelCaseNamingConvention:** Each word starts with a capital letter, and there are no spaces or underscores.
  - **Example:** `basicSalary`, `userAge`
  
- **snake_case_naming_convention:** Words are all lowercase and separated by underscores.
  - **Example:** `basic_salary`, `user_age`

### Examples of Valid Variable Names
- `a`
- `abc`
- `basic_salary`
- `gold9`
- `simple123_321`
- `basicSalary` (CamelCase)
- `userAge` (CamelCase)

### Examples of Invalid Variable Names
- `9gold` (cannot start with a digit)
- `basic salary` (cannot contain space)
- `basic,salary` (cannot contain comma)
- `if`, `elif`, `def` (reserved keywords)
- `123*123` (cannot contain special symbols other than `_`)

# Understanding Variables, Data Types, and Operators in Python

## Checking Data Types
In Python programming, the `type()` function is used to check the data type of a variable.

### Example
```python
age = 17
print(age, type(age))
percentage = 85.25
print(percentage, type(percentage))
st_name = "Om"
print(st_name, type(st_name))
gender = 'M'
print(gender, type(gender))
```

### Execution
```
stack          heap
|74859658|--->|___17___| (object)
    age        74859658

|74253698|--->|__85.25_| (object)
percentage     74253698

|74147859|--->|__Om_| (object)
  st_name     74147859

|74268952|--->|__M_| (object)
  gender     74268952
```

### Output
```
17 <class 'int'>
85.25 <class 'float'>
Om <class 'str'>
M <class 'str'>
```

## Memory Storage of Python Variables
During execution, every process occupies some space in the RAM called **address space**. The address has the following parts:

1. **Data Segment:** Contains values and variables. It includes:
   - **Stack:**
     - Memory can be given a human-friendly name.
     - Memory allocation is fast and cannot be resized (static).
   - **Heap:**
     - Memory cannot be named.
     - Memory allocation is slower and can be resized (dynamic).

2. **Code Segment:** Contains functions and statements.

### Print Function
The `print()` function is used to output text to the terminal.
```python
print(argument, sep=' ', end='\n')  # \n is for a new line
```
- The `end` parameter specifies what to print after the statement completes.
- The `sep` parameter specifies the default separator when multiple values are printed.

### Example of Print Function
```python
print("Masai")
print("School")
print("Masai", "School")
```

### Output
```
Masai
School
Masai School
```

You can change the values for `sep` and `end` parameters:
```python
print("Masai School", "Bengaluru", sep=', ')
print("Masai", end='-')
print("A tribe that survives by skills")
print("Masai", "Bengaluru", "Karnataka", sep=' : ', end=' # ')
print("859674")
```

### Output
```
Masai School, Bengaluru
Masai-A tribe that survives by skills
Masai : Bengaluru : Karnataka # 859674
```

### Variable Example
```python
name = 'Anuj'
age = 18
state = 'Gujarat'
print(name, "of age", age, "from", state, "will vote for the first time.")
print("name of age age from state will vote for first time.")
```

### Output
```
Anuj of age 18 from Gujarat will vote for the first time.
name of age age from state will vote for first time.
```

## Typecasting in Python
Typecasting is converting a value from one data type to another. 

- `"1"` is a string value.
- `1` is an integer.
- `1.0` is a float value.

### Conversion Functions
- `str(parameter)`: Converts parameter to string value.
- `int(parameter)`: Converts parameter to integer value.
- `float(parameter)`: Converts parameter to float value.

### Example of Typecasting
```python
a = 1
b = a
c = str(b)  # converting int to str
d = float(a)  # converting int to float
print(a, type(a))  # 1, <class 'int'>
print(b, type(b))  # 1, <class 'int'>
print(c, type(c))  # '1', <class 'str'>
print(d, type(d))  # 1.0, <class 'float'>
```

```python
print()  # just to insert a new line in the output

e = 1.5
f = int(e)
g = str(e)
print(e, type(e))  # 1.5, <class 'float'>
print(f, type(f))  # 1, <class 'int'>
print(g, type(g))  # '1.5', <class 'str'>
```

## Comments
Comments are written for human understanding; machines do not read them. In Python, comments start with `#`.

### Example
```python
# This is a single line comment

# This is
# a multi-line
# comment
```

## Data Types in Python
A data type defines:
- (i) The range/set of values for a variable.
- (ii) The operations that can be performed on a variable.

### Classification of Data Types
- **Number:**
  - `int`: Non-fractional numbers.
  - `float`: Fractional numbers.
  - `boolean`: Only two values: `True` or `False`.
  - `complex`: Not covered here.
  
- **Sequence:**
  - `string`: Anything inside `''` or `""`.
  - `list`: Discussed later.
  - `tuple`: Discussed later.

- **Set:**
  - `set`: Discussed later.

- **None:**
  - `None`: Discussed later.

- **Mapping:**
  - `Dictionary`: Discussed later.

### Example
```python
# Print statement for Kid's Education and "Good Morning"
print("Kid's education")
print('"Good Morning"')
```

## Operators, Operands, and Expressions
- **Operator:** A symbol that represents an operation (e.g., `+`, `~`, `<`, `>`).
- **Operand:** A variable or value on which the operation is applied.
- **Expression:** A valid combination of operators and operands.

### Example
```python
a = 10 + 20  # This is an expression
# Operators: +, =
# Operands: for +; 10 & 20 are operands, for =; a & 30 are operands.
```

### Types of Operators
1. **Based on the Number of Operands:**
   - **Unary Operator:** Applicable on one operand.
     ```python
     a = -10  # Here, - is unary
     ```
   - **Binary Operator:** Applicable on two operands.
     ```python
     a = 10 - 5  # Here, - is binary
     ```
   - **Ternary Operator:** Applicable on three operands (discussed later).

2. **Based on the Nature of Operations:**
   - Arithmetic operators
   - Relational operators
   - Logical operators
