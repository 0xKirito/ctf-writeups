# HTB Cyber Apocalypse CTF

## CaaS (cURL as a Service) - Web

- I tried a lot of different URL things and nothing seemed to work. I then started looking into `escapeshellcmd` bypasses but while doing my research, I came across file protocol `file://` somewhere and realized how stupid I was being for not trying other protocols/URI schemes.
- In curl field on webpage, I entered `file:///flag` and got the flag!
- `file://localhost/../../flag` also worked.
- Flag => CHTB{f1le_r3trieval_4s_a_s3rv1ce}
- But there are more ways to do this so I've added the links to the writeups explaining them.
- [Another Method for CaaS](https://s-3ntinel.github.io/ctfs/cyberapocalypse_ctf2021/web/caas/caas.html)
- [Yet Another Method for CaaS](https://github.com/KamilPacanek/writeups/blob/master/ctf/HTB.CA2021/caas.md)
- [And Yet Another Method for CaaS](https://thehackersbrain.pythonanywhere.com/blog/caas-web-challenge-writeup-cyber-apocalypse-2021-hackthebox-ctf/)
