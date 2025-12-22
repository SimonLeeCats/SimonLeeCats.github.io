# Learning Debuggers

"Debuggers are essential tools for analyzing program execution, inspecting memory, and understanding runtime logic. In CTF reversing or exploitation tasks, they reveal hidden logic paths, encryption routines, or validation functions and are vital for dynamic analysis." - CTF Support&#x20;

Essentially, debuggers at it's core lets you run a program step by step and modify behavior in real time. This includes to examining registers and memory at a specific time. We'll be analyzing the most important, and popular debugger:  **GDB**

{% hint style="info" %}
* Use **breakpoints** before key functions (like `strcmp`, `recv`, `decrypt`) to observe intermediate values.
* Combine static and dynamic analysis, inspect the binary structure in a disassembler before stepping through execution.
* Use **Pwndbg** or **GEF** extensions with GDB to enhance usability during CTF reversing tasks. (This is Mandatory!)&#x20;
{% endhint %}

***

GDB is a standard Linux debugger for low-level program inspection. The way you first GDB is through the terminal, and actually through compiling the program.

```
gcc -g my_program.c -o my_program

gcc -g test.c -o test
```

Then, only can you start it.

```
gdb ./test
```

To run it, type "run". However, you need to set up your breakpoints before running it (or else it just executes without any analysis) To create breakpoints:

```
Breakpoints tell GDB "stop here so I can look around."

break main           # Stop at the start of main()
break add            # Stop at the start of add()
break test.c:10      # Stop at line 10 of test.c
break *0x401234      # Stop at memory address (for assembly)
info breakpoints     # List all breakpoints
delete 1             # Delete breakpoint #1
```

Now if you type run again, it stops at the start of main()! Now that you're at the breakpoint, there's alot you can do, I'll list out a few things you can do.

```
Once stopped at a breakpoint:

next      # Execute next line (steps OVER function calls)
step      # Execute next line (steps INTO functions)
continue  # Resume running until next breakpoint
finish    # Run until current function returns

Example:
(gdb) next
Stopped at line 11

(gdb) step
Stopped at line 4 (INSIDE add() function!)

(gdb) next
Stopped at line 11 (about to call add())

(gdb) next
Stopped at line 12

Example:
(gdb) break main
(gdb) run
(gdb) next      # Move to next line
(gdb) next      # Keep going
(gdb) step      # This will step INTO the add() function
(gdb) finish    # Complete the function and retur
```

***

At each breakpoint you can quickly examine the code with the following commands.

```
print x           # Show value of variable x
print result      # Show result
print x + y       # Evaluate expressions
info locals       # Show all local variables
info proc map     # Processes's map address
display var_name  # Display a variable continuously as execution progresses
set var_name = new_value    # Modify a variable during execution:
display/10i $pc - 0x5       # (gdb) display/[# of instructions]i $pc [± offset]

list              # Show source code around current line
list add          # Show source code of add() function
disassemble       # Show assembly code for current function
disassemble add   # Show assembly for add() function
set 0x1e4a70=0x123: Sets the data at 0x1e4a70 to 0x123

info registers         # Show all registers
print $rax            # Show value in RAX register (x86-64)
print $eip            # Instruction pointer (where we are)

x/10x 0x7fffffffe000   # eXamine 10 heX values at address
x/10i $rip             # Show 10 Instructions at current position
x/s 0x400500           # Show String at address
```

### Cheatsheet

{% embed url="https://docs.google.com/viewerng/viewer?url=https://www.chciken.com/assets/gdb_cheat_sheet/gdb_cheat_sheet_dark.pdf" %}
