#!/bin/bash

# Solution for all currently solved pages of the Liber Primus
# (Vigenere skips non-included)

# Atbash for page 0 ('A Warning')
./primus.py -p 0 -@

# Vigenere with key 'DIVINITY' for page 1 ('Welcome')
./primus.py -p 1 -v divinity

# Direct translation for page 2 ('Some wisdom')
./primus.py -p 2

# Atbash -> Shift 3 for the 3rd segment ('Koan 1')
./primus.py -s 2 -c [@,S:3]

# Direct translation for the 4th segment ('The loss of divinity')
./primus.py -s 3

# Vigenere with key FIRFUMFERENCE for page 12 ('Koan 2')
./primus.py -p 12 -v firfumference

# Direct translation for page 13 ('An instruction')
./primus.py -p 14

# Totient running stream for page 56 (=page 71 when including solved pages)
./primus.py -p u56 -t

# Direct translation for page 57 (=page 72 when including solved pages)
./primus.py -p 72

