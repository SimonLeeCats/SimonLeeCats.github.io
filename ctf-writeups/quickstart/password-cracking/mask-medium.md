# Mask (Medium)

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption><p>This challenge is pretty similar to the last challenge Rockyou</p></figcaption></figure>

The first step I did was to check the type of hash. Which ended up being **MD5**. This means it has a code of 0 in hashcat.&#x20;

<figure><img src="../../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Next, like the previous challenge, was to put all the hashes into a txt file! I used vim to create a MaskHashes.txt with the hashes. But now to the cracking part of it, I suspect the "mask" title of the problem means the **attack mode** of Hashcat.&#x20;

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

As we can see in the screenshot above, with the attack mode parameter (-a), there's multiple types of attack modes. For the Rockyou challenge, we used the first mode, "0", which is the dictionary attack. Hence, I'm suspecting we will instead use the Mask/Brute-Force attack mode of 3. So let's try that out!

I intially used the command: Now let's wait... (since hashcat does take a long time...)&#x20;

```
hashcat -m 0 -a 3 "MaskHashes.txt"
```

But turns out, although some of it was correct, it just took too long. Hence, I digged deeper and relize I needed to use the clue given to us: "`SKY-HQNT-` followed by 4 digits".  This website linked below does a good job in explaining not just the Mask Attack mode, but all the attack modes for hashcat.

{% embed url="https://deepwiki.com/hashcat/hashcat-legacy/3.1-attack-modes" %}

Using this website, I learnt that why mask attack are dictionaries, they are supposed to brute force the characters. I was supposed to include a structure after the txt file. So instead, I used this command:

```
hashcat -m 0 -a 3 "MashHashes.txt" 'SKY-HQNT-d?d?d?d?'
```

This resulted in a very quick answer!

<figure><img src="../../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>
