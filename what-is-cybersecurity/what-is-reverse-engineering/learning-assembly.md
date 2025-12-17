# Learning Assembly

### Learning Assembly&#x20;

"Machine Code or Assembly is code which has been formatted for direct execution by a CPU. Machine Code is the reason why readable programming languages like C, when compiled, cannot be reversed into source code (well [Decompilers](https://ctf101.org/reverse-engineering/what-is-assembly-machine-code/) can sort of, but more on that later)." - CTF 101

Assembly in a way is the direct code to the CPU, making it suited for direct optimization or hardware interaction. For example, we all know that all of our code is just a bunch of binary. However, Assembly gives that binary readable names. Assembly consists of registers,&#x20;

There's several main modes of Assembly, x84-64 (or called x64), x84, and ARMS. Assembly x64 is generally used for every CTF and system, as it's just a lot cleaner and more convenient than x84. hence, we'll go through x64 with an emphasis.

***

### Registers

"A **register** is a location within the processor that is able to store data, much like RAM. Unlike RAM however, accesses to registers are effectively instantaneous, whereas reads from main memory can take hundreds of CPU cycles to return." - CTF101&#x20;

Registers are these tiny, super-fast storage components built on the CPU. There's multiple, but let's name a few and their functions. But before doing, let's clear up some confusion. In x84 and x64, there are 32 bit registers from x84 (like eax, ebx, ecx) that extend to x64. In x64, not only thre's double the amount of general registers than in x84, there's also registers like rax, rbx, and rcx that hold much more memory, but also `rax` contains `eax`, which contains `ax`, which contains `al` and `ah`. &#x20;

You might be wondering, if x64 can hold more memory, why don't we always use x64 registers?&#x20;

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

It boils down to backward compatability and effciency. Let's say you only need to deal with 32 bits. You would use EAX instead of RAX. If you need to extract little bits at a time, you would also use this.

```
mov rax, 0x1234567890ABCDEF   ; Full 64-bit value
mov al, 0xFF                   ; Only changes the lowest byte
; Now rax = 0x1234567890ABCDFF (only last 2 hex digits changed)
```

#### Examples

* `rax`, `rbx`, `rcx`, `rdx` - general purpose registers
* `rsp` - stack pointer (tracks the top of the stack)
* `rbp` - base pointer (tracks the bottom of the current stack frame)
* `rip` - instruction pointer (points to the next instruction to execute)

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption><p>More examples</p></figcaption></figure>

***

### Instructions

To put it simply, instructions are the actual operations the CPU performs. Here are a few:

* `mov dest, src` - move/copy data from source to destination
* `add dest, src` - add source to destination
* `sub dest, src` - subtract source from destination
* `jmp label` - jump to a different location in code
* `cmp a, b` - compare two values
* `call function` - call a function
* `ret` - return from a function

There's also control flow instructions, such as if statements.

* `jnz <address>`   &#x20;
* `je <address>`
* `jge <address>`
* `jle <address>`

jnz is "jump if not zero", and "je" is jump if equal. Pretty self-explanatory! You might also not recognize what the "address" are. **Addresses** in assembly are just numbers that point to a specific location in the memory. They are usually hexadecimal, and often paired with instructions. If you add "\[ ]" around the address, you're accessing what's stored in at that address.&#x20;

```
Memory:
Address    Value
0x1000:    [0x42]
0x1001:    [0x13]
0x1002:    [0x37]
0x1003:    [0xFF]
...
```

```
mov rax, 0x1000      ; rax = the number 0x1000
mov rax, [0x1000]    ; rax = the VALUE stored at address 0x1000
```

```
mov rax, [0x401000]    ; Load value from address 0x401000
```

You likely already saw these instructions being used, and that's for a good purpose! It's all about modifying and changing registers using these instructions.  Here is an example:

```
mov rax, [user_input]    ; Load user's password into rax
cmp rax, 0x70617373      ; Compare with "pass" (in hex ASCII)
jne wrong_password       ; If not equal, jump to wrong password
mov rdi, flag_string     ; If equal, load flag address
call print_flag          ; Print the flag
jmp end

wrong_password:
    mov rdi, fail_msg    ; Load "Wrong!" message
    call print_message
    
end:
    ret                  ; Return from function
```

### The Stack

The stack is used to store local variables, function parameters, saved registers, pointers, and more, It's a region of memory (RAM) in where it stores temporary data for function execution. It's automatic and fast, but it's buffer memory can be exceeded. For example, if a buffer can hold 64 bytes but you write 80 bytes, those extra 16 bytes overwrite whatever comes after. (Which would be called an buffer overflow!)

Or in other words, "A region of memory used for temporary storage, function calls, and local variables. It grows downward in memory (from high addresses to low)." It follows a **Last in First Out (LIFO)**

<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

In otherwords, you can only push (add to the top) or pop (remove from the top). The stack exists so we can do function calls, store local variables, and to store register values temporarly. But keep in mind, the stack stores, it doesn't execute anything. An example of how the stack would change is:

```
sub rsp, 32    ; Allocate 32 bytes on stack (move pointer down)
add rsp, 32    ; Deallocate 32 bytes (move pointer up)
```

Also, you might confuse yourself between the Stack and a Heap, but these are still different.  "The heap requires explicit allocation (malloc) and deallocation (free), and grows upward toward higher addresses. The stack is for short-lived data; the heap is for data that needs to persist beyond a single function call."

### Exercises&#x20;

1 ) What is the password?

```
mov rax, [user_input]
cmp rax, 0x1337
je success
jmp fail
```

Explanation:  What this is essentially doing is storing data from the user\_input into one of the registers, rax. Now it's comparing two values, rax and an number. This does not compare rax with the value of address, neither an address. It's comparing rax to a hexadecimal, which is 4919. If it's equal, it suceeds, and else it fails.&#x20;

2 ) Math

```
mov rax, 10      ; rax = 10
mov rbx, 5       ; rbx = 5
add rax, rbx     ; rax = 10 + 5 = 15
sub rax, 3       ; rax = 15 - 3 = 12
imul rax, 2      ; rax = 12 * 2 = 24
```

Explanation:  This one is quite simple. It's basically moving integers into these general purposes registers (rax, and rbx)  and then adding them. The "imul" command is doing the multiplication.

3 ) Stack

```
mov rax, 100      ; rax = 100
mov rbx, 200      ; rbx = 200
push rax          ; Put rax's value (100) on stack
push rbx          ; Put rbx's value (200) on stack
pop rcx           ; Take top value (200) and put it in rcx
pop rdx           ; Take next value (100) and put it in rdx
```

Explanation: Again, it's copying the integers 100 and 200 into their respective registers. Then it pushes the first register on top of the stack, with then the 2nd on top. Keep in mind, since the stack follows a LIFO order, the top value isn't the first value in the array. But you might ask, if created rax and rbx, but you popped rcx and rdx? This is because rcx/rdx takes the value from the top of the stack, or you can think of it a stack of plates. rcx copies the value from the top plate (200) and removes it. Same thing applies to rdx.&#x20;

Here's a last example:

```
   0x0804000: mov eax, 0xdeadbeef            Register Values:
   0x0804005: mov ebx, 0x1234                RIP = 0x080400d
   0x080400a: add, rax, rbx                  RAX = 0xdeadd123
-> 0x080400d: inc rbx                        RBX = 0x1234
   0x0804010: sub rax, rbx                   RCX = 0x0
   0x0804013: mov rcx, rax                   RDX = 0x0
```

Also last side note, if you're confused on whether the instruction is referring to an address or a hexadecimal, just generally look at their sizes. Addresses are usually 4-8 bytes long, and hexadecimals incude just a few digits.&#x20;

### Cheat Sheet&#x20;

It's generally good to get an overview!

{% embed url="https://web.stanford.edu/class/cs107/resources/x86-64-reference.pdf" %}
