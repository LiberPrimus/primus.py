### Primus.py

A python script to help attempt to decrypt the Liber Primus.

This tool allows you to chain different ciphers in a given order on any page/segment/paragraph of the Liber Primus.
You can also do Gematria sums of the words, lines, sentences or full page/segment/paragraph.

It uses Taiiwo's great [Cicada Python Library](https://github.com/Taiiwo/cicada)


**Installation:**
```bash
git clone https://github.com/LiberPrimus/primus.py.git primus
cd primus
git submodule update --init

# Optionally, add primus.py to your path so you can use it anywhere
echo PATH=$PATH:$(pwd) >> ~/.bashrc && . ~/.bashrc
```


**Usage examples:**
```bash
# View help page
./primus.py --help

# Process all pages with Totient -> Atbash -> Shift by 13 -> Vigenere w/ key "PRIMUS" -> Reverse text
./primus.py --page all --ciphers [totient,atbash,shift:13,vigenere:primus,reverse]
# only unsolved pages (uall)
./primus.py -p uall -c [totient,atbash,shift:13,vigenere:primus,reverse]
# try it on segments instead of pages
./primus.py --segment all -c [totient,atbash,shift:13,vigenere:primus,reverse]
# shorthand version
./primus.py -p all -c [t,@,S:13,v:primus,R]


# Print the 1st of the solved pages ("A Warning") in Latin
./primus.py --page 0
# shorthand version
./primus.py -p 0


# Print the 1st of the solved pages ("A Warning") in Runic
./primus.py --page 0 --runic
# shorthand version
./primus.py -p 0 -r


# Print the 1st of the unsolved pages (0.jpg)
./primus.py --page 15
# prefix with 'u' to match only the unsolved pages
./primus.py --page u0


# Atbash the first solved page ("A Warning")
./primus.py --page 0 --atbash
# alternative
./primus.py -p 0 -c [atbash]
# shorthand version
./primus.py -p 0 -@


# Atbash followed by Shift of 3 on page 4
./primus.py --page 4 --ciphers [atbash, shift:3]
./primus.py -p 4 -c [@,S:3]


# Vigenere with key "FIRFUMFERENCE" on page 12
./primus.py --page 12 --vigenere FIRFUMFERENCE
# key can be in latin or runic, uppercase or lowercase
./primus.py --page 12 --vigenere ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ
# alternative
./primus.py --page 12 --ciphers [vigenere:firfumference]
# other alternative
./primus.py -p 12 -c [v:firfumference]
# shorthand version                   
./primus.py -p 12 -v firfumference               


# Totient running stream on page 56
./primus.py --page u56 --totient
# page 56 is 71 if including the solved pages
./primus.py --page 71 --totient
# alternative
./primus.py -p u56 --ciphers [totient]
# alternative shorthand
./primus.py -p u56 -c [t]
 # shorthand version          
./primus.py -p 71 -t             


# Gematria sum of the words on page 57
./primus.py --page u57 --sumwords
# shorthand
./primus.py -p u57 -sw
# Atbash page 57 then gematria sum the words
./primus.py -p u57 -c [atbash,sumwords]
# shorthand
./primus.py -p u57 -c [@,sw]
# Gematria sum of the lines on page 57
./primus.py -p u57 --sumlines
# shorthand
./primus.py -p u57 -sl
# Gematria sum of the sentences on page 57
./primus.py --page u57 --sumsentences
# shorthand
./primus.py -p u57 -ss
# Gematria sum of the whole page 57
./primus.py --page u57 --sum


# Print only the possible english words found
./primus.py --page uall --wordsonly
# shorthand
./primus.py -p uall -w


# Saving results
./primus.py -p all -c [@,t,R] > results.txt
```
