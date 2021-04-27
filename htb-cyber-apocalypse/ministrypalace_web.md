# HTB Cyber Apocalypse CTF

## MiniSTRyplace - Web

- The name suggests `str_replace` vulnerability that allows for path traversal/LFI.
- And the source code was downloadable so I knew the `flag` file was in the root `/` directory.
- The source code also showed that the function was replacing `../` in the URL.
- So I ran a few LFI payloads and this `....//....//` one worked.
- `IP:PORT/?lang=....//....//flag`
- Flag => CHTB{b4d_4li3n_pr0gr4m1ng}
- [HTB Academy - Local File Inclusion](https://academy.hackthebox.eu/course/preview/file-inclusion--directory-traversal/local-file-inclusion)
- [OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
