# Rockyou (Easy)

I've had never done a password cracking CTF before this, so this is a new one for me. I used this methodology to help me solve this puzzle and soon the rest of the other puzzles.&#x20;

<figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption><p>Found on ctf.support</p></figcaption></figure>

It was definitely a challenge to learn a new set of tools and skills, but Rockyou is just easy enough to start on.

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

In this challenge, we know two things. First of all, the hashes are given so we don't really need to extract any hashes. But secondly, the "Rockyou" title of the challenge indicates usage of wordlist from the Rockyou data breach.&#x20;

***

<figure><img src="../../../.gitbook/assets/Screen Shot 2025-12-09 at 12.23.36 PM.png" alt=""><figcaption></figcaption></figure>

I proceeded to identify the hash for the challenge. It seems to be a MD5 hash so we'll run with that.&#x20;



Next, for password cracking, we typically will need to use hashcat. Good thing that hashcat and rockyou.txt is already installed on all Kali Linux VMs!

### Using Hashcat  (and vim...)

Before using Hashcat, I needed to create txt files including all of the hashes. And to do so... I needed to also learn the fundamentals of vim (although not neccesary but reccomened.)

<figure><img src="../../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

There's 4 main modes of vim, but really I'll only be using the "insert" and "normal" mode. The "insert" mode is where you'll do all of your typing, and the "normal" mode is where you'll run short commands like ":wq" to save and quit. To switch from normal mode to insert mode, you would press o or any other shortcut of insert mode, and to switch from insert mode to normal mode, you would press esc.&#x20;

More commands can be found here: [https://www.freecodecamp.org/news/vim-key-bindings-reference/](https://www.freecodecamp.org/news/vim-key-bindings-reference/)

#### Inserting Hashcat

The way Hashcat works is almost like this:

```
# hashcat [options such as -m, -a] hashfile [path to wordlist, mask, attack options]

an example would be: hashcat -m 17200 -a 0 zip.hash rockyou.txt
```

The command I used for this challenge is: hashcat -m 0 -a 0 test.txt /usr/share/wordlists/rockyou.txt --show.&#x20;

The -m parameter siginfies the type of hash we're decoding. While the -a parameter is the attack mode, 0 being dictionary. There's a lot more to it, but that's all for now!

<figure><img src="../../../.gitbook/assets/Screen Shot 2025-12-09 at 2.26.37 PM.png" alt=""><figcaption></figcaption></figure>
