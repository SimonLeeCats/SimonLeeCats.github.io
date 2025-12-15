# PDF (Medium)

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

This one a little more unique in that this time, it includes a PDF file. But the process remains the same. Identity the file, Identify the hash, and generally use hashcat!&#x20;

***

For this challenge, I'm going to use the tool "pdf2john". What it basically does it converts a pdf to an active hash. pdf2john has a relativlty simple command structure



<figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

But from here, I got kind of stuck. The obvious thing to do first of all, since we used john, we needed to remove the "encrypted.pdf:" title in the hash. There are various ways to do this but, I just used vim to manually delete it. From here, there's not really an specific direction in where I should aim in. But the first thing I should do is to identify the hash.&#x20;

{% embed url="https://hashcat.net/wiki/doku.php?id=example_hashes" %}

I went through the hash types and figured that there was a few likely hash:&#x20;

<figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

And after analyzing a bit, I realize the hash number was definitely 10700.&#x20;

***

Next is to actually use hashcat. There's 7 main attack modes according to the wiki:

<figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

I don't think any attack type aside from 0 and 1 could work in this situation. Hence, let's just use attack type 0 considering we did it in a previous challenge. If we're using attack 0, we need a wordlist. And if we need a wordlist, let's just use Rockyou considering we also used it before! I used the command:

```
hashcat -m 10700 -a 0 pdf.txt /usr/share/wordlists/rockyou.txt 
```

However, I didn't bother running the command, as I'm using a Kali Linux VM. (This would take over 3 hours!) I checked my steps with the guide and I got it all correct, so I'll call this a success. ;)&#x20;

