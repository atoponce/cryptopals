#!/usr/bin/python

# Fixed XOR
# 
# Write a function that takes two equal-length buffers and produces their XOR
# combination.
# 
# If your function works properly, then when you feed it the string:
# 
# 1c0111001f010100061a024b53535009181c
# 
# ... after hex decoding, and when XOR'd against:
# 
# 686974207468652062756c6c277320657965
# 
# ... should produce:
# 
# 746865206b696420646f6e277420706c6179

import s1p1

def RawToHex(s):                                                                
    """Return a hexadecimal strong from raw bytes."""                           
    h = s.encode("hex")                                                         
    return h                                                                    

def XORHex(s1, s2):
    """Calculate the XOR from two equal length strings."""
    if len(s1) != len(s2):
        return Null

    r1 = s1p1.HexToRaw(s1)
    r2 = s1p1.HexToRaw(s2)
    result = ''

    for x,y in zip(r1,r2):
        result += chr(ord(x) ^ ord(y))

    return RawToHex(result)

if __name__ == "__main__":
    t1 = "1c0111001f010100061a024b53535009181c"
    t2 = "686974207468652062756c6c277320657965"
    a = "746865206b696420646f6e277420706c6179"
    try:
        assert(XORHex(t1,t2).strip() == a)
        print("Success")
    except AssertionError:
        print("Failure")
