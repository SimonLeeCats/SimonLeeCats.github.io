# hashcrack (easy)

Considering the amount of hashcat I used in NCL, this one should be a piece of cake.&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2025-12-15 at 12.35.42 PM.png" alt=""><figcaption></figcaption></figure>

When first connected to the server, it greets you with an hash, and a password to fill out. Very similar to password cracking.&#x20;

***

Of course, the first thing to do with that hash it identify the type.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

This ended up being an MD5 hash. This means the mode is 0. Let's just also assume we will using an attack mode of 0 (dictionary) using the rockyou password database.

```
hashcat -m 0 -a 0 (insert hash) /usr/share/wordlists/rockyou.txt
```

Surprisingly, it didn't just end there, it gave us another hash! But same procedures. We check the hash type.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

And we plug it in hashcat (with a different hash mode this time)&#x20;

```
hashcat -m 100 -a 0 (insert hash) /usr/share/wordlists/rockyou.txt
```

We cracked it, and then it gave us one last hash... you already know the process.&#x20;

<figure><img src="../../../.gitbook/assets/Screen Shot 2025-12-15 at 12.46.23 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screen Shot 2025-12-15 at 12.46.14 PM.png" alt=""><figcaption></figcaption></figure>

And we found the last hash! Instead of a 100 mode, we used an 1400 mode (SHA2-256).&#x20;
