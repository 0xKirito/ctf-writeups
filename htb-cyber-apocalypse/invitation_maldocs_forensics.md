# HTB Cyber Apocalypse CTF

## Invitation - Document Forensics Breakdown

- Extract the `.docm` file: `unzip file.docm`. We will get one directory named `word` which will have a `vbaProject.bin` file in it. Thats what we need.
- Use Python [OleTools](https://github.com/decalage2/oletools) to read the `vbaProject.bin` file.
- `olevba3 --decode --deobf --reveal vbaProject.bin` (you can play around with these options but `--deobf` flag didn't work for me so had to manually do everything. Maybe I was doing something wrong).

[Trick to deobfuscate malware code from Unicorns of Security's writeup](https://ctftime.org/writeup/27836)

> My favorite trick is always to ask malware to deobfuscate itself for us. It can save a lot of time in case of more complex obfuscation scenarios. In this case I added this one line to the code: `ActiveDocument.Content.InsertAfter Text:=odsuozldxufm` and then ran the macro again.

- We will get hundreds of hex strings (encoded VBA). Use a good code editor to copy all of them at once and paste it in CyberChef.
- In CyberChef, add 'From Hex', then add 'From Base64', then add 'Remove null bytes' to get rid of all the pesky little dots/periods and bake.
- Decode Hex strings => Decode Base64 => Remove Null Bytes => Manual Code Review.
- We will find the strings for flag in the code upon code review but they are a bit jumbled up and reversed. So we will need to fix that manually to get the flag. And the flag string is in two different but similar code blocks. So we will also need to piece it together.

```
SEt ("G8"+"h")  (  " ) )63]Rahc[,'raZ'EcalPeR-  43]Rahc[,)05]Rahc[+87]Rahc[+94]Rahc[(  eCAlpERc-  )';2'+'N'+'1'+'}atem_we'+'n_eht'+'_2N1 = n'+'gerr'+'aZ'(( ( )''niOj-'x'+]3,1[)(GNirTSot.EcNereFeRpEsOBREv$ ( . "  ) ;-jOIn ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue[ - 1.. - ( ( lS ("VAR"+"IaB"+"LE:g"+"8H")  ).VALue.LengtH)] | IeX
```

- `atem_we'+'n_eht'+'_2N1` => `atem_wen_eht_` => `_the_new_meta`

```
. ( $PshomE[4]+$pshoMe[30]+'x') ( [strinG]::join('' , ([REGeX]::MaTCHES( ")'x'+]31[DIlLeHs$+]1[DiLLehs$ (&| )43]RAhc[]GnIRTs[,'tXj'(eCALPER.)'$','wqi'(eCALPER.)';tX'+'jera_scodlam'+'{B'+'T'+'HCtXj '+'= p'+'gerwqi'(" ,'.' ,'R'+'iGHTtOl'+'eft' ) | FoREaCH-OBJecT {$_.VALUE} ))  )
```

- `tX'+'jera_scodlam'`
- The `tXj` or `jXt` reversed, is actually getting replaced with something else as we can see in the code, so it is not a part of the string we need.
- `era_scodlam` => `maldocs_are`
- And piecing everything together => `CHTB{maldocs_are_the_new_meta}`
