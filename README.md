### Primus.py

A python script to help attempt to decrypt the Liber Primus.

This tool allows you to apply various types of ciphers, in specific order, to all or any page/segment/paragraph of the Liber Primus

It uses Taiiwo's great [Cicada Python Library](https://github.com/Taiiwo/cicada)

Usage examples:
```bash
# Process all pages with Totient -> Atbash -> Shift by 13 -> Vigenere w/ key "PRIMUS" -> Reverse text
./primus --page all --ciphers [totient,atbash,shift:13,vigenere:primus,reverse]
./primus -p uall -c [totient,atbash,shift:13,vigenere:primus,reverse] # only unsolved pages
./primus --segment all -c [totient,atbash,shift:13,vigenere:primus,reverse] # try it on segments instead of pages
./primus -p all -c [t,@,S:13,v:primus,R] #shorthand version

# Print the 1st of the solved pages ("A Warning") in Latin
./primus --page 0
./primus -p 0     #shorthand version

# Print the 1st of the solved pages ("A Warning") in Runic
./primus --page 0 --runic
./primus -p 0 -r     #shorthand version

# Print the 1st of the unsolved pages (0.jpg)
./primus --page 15
./primus --page u0 #prefix with 'u' to match only the unsolved pages

# Atbash the first solved page ("A Warning")
./primus --page 0 --atbash
./primus -p 0 -c [@]       #alternative
./primus -p 0 -@           #shorthand version

# Atbash followed by Shift of 3 on page 4
./primus --page 4 --ciphers [atbash, shift:3]
./primus -p 4 -c [@,S:3]

# Vigenere with key "FIRFUMFERENCE" on page 12
./primus --page 12 --vigenere FIRFUMFERENCE
./primus --page 12 --vigenere ᚠᛁᚱᚠᚢᛗᚠᛖᚱᛖᚾᚠᛖ #key can be in latin or runic, uppercase or lowercase
./primus --page 12 --ciphers [vigenere:firfumference] #alternative
./primus -p 12 -c [v:firfumference]                   #alternative
./primus -p 12 -v firfumference                       #shorthand version

# Totient running stream on page 56
./primus --page u56 --totient
./primus --page 71 --totient        #page 56 is 71 if including the solved pages
./primus -p u56 --ciphers [totient] #alternative
./primus -p u56 -c [t]              #alternative shorthand
./primus -p 71 -t                   #shorthand version

# Saving results
./primus -p all -c [@,t,v:liber] > results.txt
```
