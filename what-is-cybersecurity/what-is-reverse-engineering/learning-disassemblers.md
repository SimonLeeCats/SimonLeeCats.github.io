# Learning Disassemblers

A disassembler is a tool that breaks down complied program into machine code. "In CTF challenges, examining assembly helps identify encryption loops, password checks, and hidden key comparisons."  For example, we could find functions such as check\_password() or validate\_flag(), or find vulnerabilities.

There's many tools for disassemblers, but we'll be going through the most popular one, Ghidra.&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2025-12-17 at 3.05.12 PM.png" alt=""><figcaption></figcaption></figure>

***

### Ghidra&#x20;

Once you import your exe file or whatever, you'll be met with the main screen.&#x20;

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

On the top left you'll see the "Program Tree" Section

<figure><img src="../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

This part could be really useful as it does usually contain all the functions, classes, imports (libraries) etc...&#x20;

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption><p>This is the functions of from the viewer. Could really be useful in CTFs! (Also FUN is the default name for an unnamed function)</p></figcaption></figure>

***

By clicking on entry in the main window, you'll see the  code:

<figure><img src="../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

Additionally, on the top left if you press "Defined Strings" you can search up for strings. Almost like the index in Wireshark.&#x20;

<figure><img src="../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

***

I can't explain too much without being practical, so the rest is up to me and you guys to learn it for yourself!
