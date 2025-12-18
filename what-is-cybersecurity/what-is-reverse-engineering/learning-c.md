# Learning C

I'm going to make this page quite dense and short as learning C is a very particular part of cybersecurity. One of the main reasons people use C at least for CTFs is that C directly complies down to assembly code. Additionally, most exploitation are targeted towards C! However, it's good to know anyways as it's very similar and constructs the foundation of most languages we used today. I'll be mostly referencing material form here:&#x20;

{% embed url="https://ctf101.org/reverse-engineering/what-is-c/" %}

***

I already had a decent experience with Python, Java, and even C previously, so I'll skim a bit of it.

Let's start off with printing "Hello World!"

```
#include <stdio.h>
int main()
{
   printf("Hello, World!");
   return 0;
}
```

***

## Syntax

#### Variables and Types

There's many types like with any other language like int, float, double (64 bit floating number) etc...&#x20;

```
int x = 10;         // Integer 
```

However, there's additional types in C specifically. unsigned int means the number can't be negative, and long long is used with large, large numbers. char is a single alphabet. which means...&#x20;

```
char str[] = "Hello";  // Actually: ['H','e','l','l','o','\0'], we need the /0 at the end to mark the end!
```

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

#### Arrays

Arrays in C have a fix size. It has the same order (like arr\[0] ) Additionally, every array in C needs to be the **same type**.&#x20;

```
int arr[5]; int arr[5];           // Fixed size, no bounds checking!
arr[0] = 10;
arr[4] = 50;
arr[10] = 99;         // NO ERROR - but corrupts memory!

// Initialize:
int numbers[3] = {1, 2, 3};
```

#### Control Flow & Functions&#x20;

The control flow and functions is the same as in java.&#x20;

```
if (x > 10) {
    printf("Big\n");
} else {
    printf("Small\n");
}

for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
}

while (x > 0) {
    x--;
}
```

***

<figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

### Pointers

Pointers is what differtiates what previous languges such as Java and Python. Pointers are variables that hold memory addresses of another varaible. Firstly, we need to understand that memory is stored under terms of addresses, and data connecting to said data. I'll let CTF 101 do the talking since I do think they give a very clear explaination:

***

Take the following example of defining an integer in C:

```
int x = 4;
```

To the programmer this is the variable `x` receiving the value of 4. The computer stores this value in some location in memory. For example we can say that address `0x1000` now holds the value `4`. The computer knows to directly access the memory and retrieve the value `4` whenever the programmer tries to use the `x` variable. If we were to say `x + 4`, the computer would give you `8` instead of `0x1004`.

But in C we can retrieve the memory address being used to hold the 4 value (i.e. 0x1000) by using the `&` character and using `*` to create an "integer pointer" type.

```
int* y = &x;
```

The `y` variable will store the address pointed to by the `x`variable (0x1000) as a number.

The `*` character allows us to declare pointer variables but also allows us to access the value stored at a pointer. For example, entering `*y` allows us to access the 4 value instead of 0x1000.

Whenever we use the `y` variable we are using the memory address, but if we use the `x` variable we use the value stored at the memory address.

***

<figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

Now that you're starting to get it now, let's go through an quick example.&#x20;

````
int x = 42;           // x holds the value 42
int *ptr = &x;        // ptr holds the ADDRESS of x

// Two operators:
// & = "address of"
// * = "value at" (dereference)

printf("Value: %d\n", x);        // 42
printf("Address: %p\n", &x);     // 0x7fff1234 (some address)
printf("Ptr holds: %p\n", ptr);  // 0x7fff1234 (same address)
printf("Value at ptr: %d\n", *ptr);  // 42 (follows the pointer)
```

**Visual:**
```
Memory:
Address    Variable    Value
0x1000     x           42
0x2000     ptr         0x1000  (points to x)
````

Knowing this, let's do this quick exercise.

***

What would this print?

```
int x = 10;
int *ptr = &x;

*ptr = 20;  

printf("%d\n", x);  
```

Explanation: We know the second line stores the address of x. However, when we type \*ptr, it follows the pointer (address) of x, to the value of 20. This essentially becomes x= 20 in a way.. Hence, when we print it, it prints out 20!

There's a lot more to it also!

```
int arr[5] = {10, 20, 30, 40, 50};

printf("%d\n", arr[0]);   // 10
printf("%d\n", *ptr);     // 10 (same thing!)

printf("%d\n", arr[1]);   // 20
printf("%d\n", *(ptr+1)); // 20 (pointer arithmetic!)

char *str = "Hello";  // str points to "Hello" in memory

char str2[] = "Hello";  // Creates an array, same result

// Accessing characters:
printf("%c\n", str[0]);   // 'H'
printf("%c\n", *(str+1)); // 'e'
```

Now that we know this, let's see how it interacts with the stack

```
#include <stdio.h>

void function() {
    int x = 10;
    printf("x = %d\n", x);
}

int main() {
    int a = 5;
    function();
    printf("a = %d\n", a);
    return 0;
}

[a = 5]  ← a lives here on the stack

[return address]  ← "Come back to main after function() ends"
[x = 10]          ← x lives here on the stack
[a = 5]           ← a is still here

[a = 5]  ← x is gone! Stack shrunk back

```

The stack exists for function calls and especially for local variables.  After calling the function(), unless it returns an answer, nothing is kept in the stack!&#x20;
