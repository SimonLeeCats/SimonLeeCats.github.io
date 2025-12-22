# Learning Decompilers

> ```
> "Decompilers do the impossible and reverse compiled code back into psuedocode/code."
> ```

Decompilers allow you to recover source-like representations from compiled code such as .NET assemblies, Java archives, Python bytecode, or Flash objects. In CTF reverse engineering challenges, this step often exposes authentication routines, flag checks, or encryption functions hidden in compiled applications.

\
In other words, decompilers are tools that try to convert compiled machine code (binary) back into higher-level source code, usually C or C-like pseudocode. They're like reverse-compilers - they undo what the compiler did. Since Assembly is generally hard to read, decompliers are necessary to really understand code.Ghidra and other tools can achieve this.
