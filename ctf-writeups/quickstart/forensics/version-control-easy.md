# Version Control (Easy)

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption><p>There's more questions that follow up this screenshot</p></figcaption></figure>

From the title, I can already guess it's using git commands and checking the version history of the file. Prior to this challenge I was already quite familiar with Git (as anyone should be), so I'm guessing is using the inspect git commands.&#x20;

{% embed url="https://education.github.com/git-cheat-sheet-education.pdf" %}

***

One thing I like to do is to put the extracted folder in desktop so I can get a visual view of the folder. After that it I moved into the directory. I used the most simple command: "git log"

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

And just there, is the answer for the first question! The next questions asks for the flag for that employee. I'm not really sure what it means by flag, but I'm assuming its the SHA1 hash near the commit text. I looked in the table of git commands, and I noticed that there was only one that used the hashed, "git show".&#x20;

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Next, I was a little stuck. However, I did what I always do. Look at the commands again. I tried other commands in the inspect page and the "Stage and Snapshot", but none of them work. Then I tried the Branch commands. I used the command:

```
git branch
```

It displayed there was actually 2 branches! The other one was called "next". I moved into that branch, and read the file in that branch.

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
