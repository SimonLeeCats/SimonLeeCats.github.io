# File Carving (Medium)

<figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

I didn't mean to solve two of the questions so fast, but I did.... But anyways, this challenge is relativly easy.&#x20;

***

I first used the command "file \_\_\_" to identiy the file type. It ended up being a simple PNG.&#x20;

Next I used the command binwalk. And lord behold, it showed me this. &#x20;

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

If I count the amount of hexadecimals files, there's **6**. That ended up being the answer also.&#x20;

***

So far it's been relatively easy. So when they asked for a hidden flag, I've actually suspected that it was a stenography-based question. Before even answering any questions, one thing I noticed is how pixelated and grainy the picture was. This clued that there was something going on visually.&#x20;

But...I wasn't able to make it work (even after converting it to a png). Next I tried using strips and grepping the word "SKY", but that also didn't work. I was quite stumped on how to proceed next.&#x20;

***

I figured it was something to do with binwalk and the rest of the 5 files.  Hence, I searched up functions of binwalk.

{% embed url="https://commandmasters.com/commands/binwalk-common/" %}

I learnt that other than scanning a binary file, it's also commonly used to extract files. Knowing this, I used the command:&#x20;

```
binwalk green_file --extract 
```

It extracted a tar file called "CAB". By now, I know this probably contains the flag, and it does!&#x20;

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
