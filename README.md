### Primus.py

A python script to help attempt to decrypt the Liber Primus.

This tool allows you to chain different ciphers in a given order on any page/segment/paragraph of the Liber Primus.
You can also do Gematria sums of the words, lines, sentences or full page/segment/paragraph.

It uses Taiiwo's great [Cicada Python Library](https://github.com/Taiiwo/cicada)

**Usage examples:**
```bash
# Process all pages with Totient -> Atbash -> Shift by 13 -> Vigenere w/ key "PRIMUS" -> Reverse text
./primus --page all --ciphers [totient,atbash,shift:13,vigenere:primus,reverse]
# only unsolved pages (uall)
./primus -p uall -c [totient,atbash,shift:13,vigenere:primus,reverse]
# try it on segments instead of pages
./primus --segment all -c [totient,atbash,shift:13,vigenere:primus,reverse]
# shorthand version
./primus -p all -c [t,@,S:13,v:primus,R]


# Print the 1st of the solved pages ("A Warning") in Latin
./primus --page 0
# shorthand version
./primus -p 0


# Print the 1st of the solved pages ("A Warning") in Runic
./primus --page 0 --runic
# shorthand version
./primus -p 0 -r


# Print the 1st of the unsolved pages (0.jpg)
./primus --page 15
# prefix with 'u' to match only the unsolved pages
./primus --page u0


# Atbash the first solved page ("A Warning")
./primus --page 0 --atbash
# alternative
./primus -p 0 -c [atbash]
# shorthand version
./primus -p 0 -@


# Atbash followed by Shift of 3 on page 4
./primus --page 4 --ciphers [atbash, shift:3]
./primus -p 4 -c [@,S:3]


# Vigenere with key "FIRFUMFERENCE" on page 12
./primus --page 12 --vigenere FIRFUMFERENCE
# key can be in latin or runic, uppercase or lowercase
./primus --page 12 --vigenere ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ
# alternative
./primus --page 12 --ciphers [vigenere:firfumference]
# other alternative
./primus -p 12 -c [v:firfumference]
# shorthand version                   
./primus -p 12 -v firfumference               


# Totient running stream on page 56
./primus --page u56 --totient
# page 56 is 71 if including the solved pages
./primus --page 71 --totient
# alternative
./primus -p u56 --ciphers [totient]
# alternative shorthand
./primus -p u56 -c [t]
 # shorthand version          
./primus -p 71 -t             


# Gematria sum of the words on page 57
./primus --page u57 --sumwords
# shorthand
./primus -p u57 -sw
# Atbash page 57 then gematria sum the words
./primus -p u57 -c [atbash,sumwords]
# shorthand
./primus -p u57 -c [@,sw]
# Gematria sum of the lines on page 57
./primus -p u57 --sumlines
# shorthand
./primus -p u57 -sl
# Gematria sum of the sentences on page 57
./primus --page u57 --sumsentences
# shorthand
./primus -p u57 -ss
# Gematria sum of the whole page 57
./primus --page u57 --sum


# Saving results
./primus -p all -c [@,t,R] > results.txt
```
