#!/usr/bin/python3

import pwn
import codecs

# the provided `ps2.txt` file had 10000 lines of hex encoded strings
# only one of them was the flag we needed

line_number = 0
flag_match_str = "CHTB"
flag = ""
break_loop = False

with open("ps2.txt") as file:
    for line in file:
        if break_loop:
            break
        line = line.rstrip("\n")
        line = bytes.fromhex(line)
        # print(line)
        line_number += 1
        print("Line: ", line_number)
        # to brute force single byte XOR key (max 256 chars)
        for i in range(256):

            xored = pwn.xor(line, i)
            unicoded = codecs.decode(xored, "UTF-8", errors="ignore")

            if flag_match_str in unicoded:
                flag = unicoded
                print("Flag: ", flag, unicoded)
                break_loop = True

if len(flag) > 1:
    print("Flag: ", flag)
else:
    print("Flag: ", flag, ": not found!")

# Flag => CHTB{n33dl3_1n_4_h4yst4ck}
