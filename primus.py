#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from cicada.cicada import LiberPrimus
from cicada.cicada.gematria import Latin, Runes, Cipher
from Levenshtein import *
from StringMatcher import StringMatcher
import argparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


LP = LiberPrimus()
TARGET = 'pages'
LANG = 'latin'
ATBASH = False
REVERSE = False
VIG = False
TOTIENT = False
CAESAR = False
SUM = False
SUM_WORDS = False
SUM_SENTENCES = False
SUM_LINES = False
WORDS_ONLY = False
CIPHER_CHAIN = []
CLOSE_WORDS = False
MATCH_RATIO = 0.84

msg = ''
string_matcher = StringMatcher()


def throw_shit(text):
    method = ''
    pagelen = len(str(text).replace('\n', '').replace('.', '').replace(' ', ''))
    print(f'PAGE LENGTH: {pagelen} characters')
    for cipher in CIPHER_CHAIN:
        # Atbash
        if cipher == 'atbash' or cipher == '@':
            text = Runes(str(text)).atbash()
            method += ' → ' if len(method) > 0 else ''
            method += 'Atbash'

        # Vigenere
        if cipher[0:8] == 'vigenere' or cipher == 'v' or 'v:' in cipher:
            key = cipher.split(':')[1] if ':' in cipher else VIG
            key = Latin(key).to_runes() if key.isalpha() else key
            text = Runes(str(text)).vigenere(str(key), [], True)
            method += ' → ' if len(method) > 0 else ''
            method += f'Vigenere with key "{key}"'

        # Totient Running Stream
        elif cipher == 'totient' or cipher == 't':
            text = Runes(str(text)).totient_stream()
            method += ' → ' if len(method) > 0 else ''
            method += 'Totient Stream'

        # Fibonacci Running Stream
        elif cipher == 'fibonacci' or cipher == 'fib' or cipher == 'f':
            text = Runes(str(text)).fib_stream()
            method += ' → ' if len(method) > 0 else ''
            method += 'Fibonacci Stream'

        elif cipher == 'mod60':
            text = Runes(str(text)).mod60()
            method += ' → ' if len(method) > 0 else ''
            method += 'i+3301 % 60 % 29'

        # Reverse Text
        elif cipher == 'reverse' or cipher == 'R':
            text = str(text)[::-1]
            method += ' → ' if len(method) > 0 else ''
            method += 'Reversed Text'

        # Caesar Shift
        elif cipher == 'S' or cipher == 'shift':
            text = Runes(str(text)).shift(CAESAR)
            method += ' → ' if len(method) > 0 else ''
            method += f'Caesar Shift by {CAESAR}'
        elif 'shift:' in cipher or 'S:' in cipher:
            shift_by = int(cipher.split(':')[1])
            text = Runes(str(text)).shift(shift_by)
            method += ' → ' if len(method) > 0 else ''
            method += f'Caesar Shift by {shift_by}'

        # Custom function
        elif 'custom:' in cipher:
            code = cipher.split(':')[1]

            def custom_func(i, primes, pos):
                return eval(code)

            text = Runes(str(text)).arbitrary(custom_func)
            method += ' → ' if len(method) > 0 else ''
            method += f'Custom Function ({code})'

        elif cipher == 'sw' or cipher == 'sumwords':
            text = Runes(str(text)).gematria_sum_words()
            method += ' → ' if len(method) > 0 else ''
            method += 'Gematria Sum of Words'

        elif cipher == 'ss' or cipher == 'sumsentences':
            text = Runes(str(text)).gematria_sum_sentences()
            method += ' → ' if len(method) > 0 else ''
            method += 'Gematria Sum of Sentences'

        elif cipher == 'sl' or cipher == 'sumlines':
            text = Runes(str(text)).gematria_sum_lines()
            method += ' → ' if len(method) > 0 else ''
            method += 'Gematria Sum of Lines'

        elif cipher == 'sum':
            text = Runes(str(text)).gematria_sum()
            method += ' → ' if len(method) > 0 else ''
            method += 'Gematria Sum of Text'

    if LANG == 'latin':
        text = Runes(str(text)).to_latin()

    if len(method) == 0:
        method = 'Direct Translation'

    print(f'{bcolors.OKGREEN}[Decryption method: {method}]{bcolors.ENDC}')

    if not WORDS_ONLY:
        print(str(text))

    matches = []
    possible_matches = []
    oneline = str(text).replace('\n', '')
    oneline = oneline.replace('.', ' ')

    with open('english4.txt') as f:
        english_dict = f.readlines()

    for word in oneline.lower().split():
        match = os.popen(f'grep -ow "\\b{word}\\b" english4.txt').read()
        match = match.split('\n')
        for m in match:
            if m and m not in matches:
                if len(m) > 3:
                    matches.append(m)

    if CLOSE_WORDS:
        for word in english_dict:
            word = word.replace('\n', '')
            for cword in oneline.lower().split():
                # only search for matches in words that are +/- 1 letters in length
                if 4 <= len(cword) == len(word) or 4 <= len(cword) == len(word) - 1 or 4 <= len(cword) == len(word) + 1:
                    string_matcher.set_seqs(word, cword)
                    dist = string_matcher.quick_ratio()
                    if MATCH_RATIO < dist < 1.0:
                        if word not in possible_matches and cword not in matches:
                            possible_matches.append(f'{word} ({round(dist * 100, 1)}%)')

    if len(matches) > 0:
        interesting = False
        if len(matches) >= 7:
            interesting = True

        matches = ", ".join(matches)
        print(f'\n{bcolors.OKCYAN}English words found:\n[{matches}]{bcolors.ENDC}')
        if CLOSE_WORDS:
            possible_matches = ", ".join(possible_matches).replace(',', ',\n')
            print(f'\n{bcolors.OKBLUE}Other possible words found:\n[{possible_matches}]{bcolors.ENDC}')
        if interesting:
            print(f'\n{bcolors.BOLD}{bcolors.HEADER}POSSIBLE SOLUTION ?!\n{bcolors.ENDC}')

    else:
        print(f'\n{bcolors.FAIL}No English words found :(\n{bcolors.ENDC}')


# Handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--page', action='store_true',
                    help='Select Liber Primus Page(s) [0-72]')
parser.add_argument('-s', '--segment', action='store_true',
                    help='Select Liber Primus Segment(s) [0-14]')
parser.add_argument('-P', '--paragraph', action='store_true',
                    help='Select Liber Primus Paragraph(s) [0-31]')
parser.add_argument('X', type=str,
                    help='The Liber Primus page/segment/paragraph number to use. Add \'u\' prefix to use only the unsolved pages' +
                         ' (\'all\' to brute-force)')
parser.add_argument('-r', '--runes', action='store_true',
                    help='Display results in Runic')
parser.add_argument('-l', '--latin', action='store_true',
                    help='Display results in Latin')
parser.add_argument('-@', '--atbash', action='store_true',
                    help='Atbash the selected text')
parser.add_argument('-t', '--totient', action='store_true',
                    help='Use totient running stream on selected text')
parser.add_argument('-f', '--fibonacci', action='store_true',
                    help='Use fibonacci stream (sum of the 2 previous runes % 29) on selected text')
parser.add_argument('-R', '--reverse', action='store_true',
                    help='Reverse the order of the selected text')
parser.add_argument('-v', '--vigenere', action='store', nargs='?', type=str,
                    help='Use totient running stream on the selected text')
parser.add_argument('-S', '--shift', action='store', nargs='?', type=int,
                    help='Apply a Caesar cipher with a shift of N')
parser.add_argument('-mod60', '--mod60', action='store_true',
                    help='Mod 60 -> Mod 29')
parser.add_argument('-custom', '--custom', action='store', nargs='?', type=str,
                    help='Run custom function on the rune indexes')
parser.add_argument('-c', '--ciphers', action='store', type=str, nargs='?',
                    help='Chain of ciphers to use in order, comma-separated. Eg: [atbash,shift:7,totient,vigenere:divinity,reverse] or [@,S7,t,v:divinity,R]')
parser.add_argument('-mr', '--matchratio', action='store', nargs='?', type=int,
                    help='Also look for English words that match X percents of the deciphered words')
parser.add_argument('-sw', '--sumwords', action='store_true',
                    help='Calculate Gematria Sum of the words in selected text')
parser.add_argument('-ss', '--sumsentences', action='store_true',
                    help='Calculate Gematria Sum of the lines in selected text')
parser.add_argument('-sl', '--sumlines', action='store_true',
                    help='Calculate Gematria Sum of the lines in selected text')
parser.add_argument('-sum', '--sum', action='store_true',
                    help='Calculate Gematria value of the individual characters in selected text')
parser.add_argument('-w', '--wordsonly', action='store_true',
                    help='Calculate Gematria value of the individual characters in selected text')

args = parser.parse_args()

if args.page:
    TARGET = 'pages'
elif args.segment:
    TARGET = 'segments'
elif args.paragraph:
    TARGET = 'paragraphs'

if args.ciphers:
    ciphers = str(args.ciphers[1:-1])
    ciphers = ciphers.split(',')
    CIPHER_CHAIN = ciphers
if args.atbash:
    CIPHER_CHAIN.append('atbash')
if args.vigenere:
    VIG = str(args.vigenere)
    CIPHER_CHAIN.append(f'vigenere_{VIG}')
if args.totient:
    CIPHER_CHAIN.append('totient')
if args.fibonacci:
    CIPHER_CHAIN.append('fibonacci')
if args.reverse:
    CIPHER_CHAIN.append('reverse')
if args.shift:
    CAESAR = int(args.shift)
    CIPHER_CHAIN.append(f'shift:{CAESAR}')
if args.mod60:
    CIPHER_CHAIN.append('mod60')
if args.custom:
    CIPHER_CHAIN.append(f'custom:{str(args.custom)}')
if args.matchratio:
    MATCH_RATIO = (int(args.matchratio) - 1) / 100
    CLOSE_WORDS = True
if args.sumwords:
    SUM_WORDS = True
    CIPHER_CHAIN.append('sumwords')
if args.sumsentences:
    SUM_SENTENCES = True
    CIPHER_CHAIN.append('sumsentences')
if args.sumlines:
    SUM_LINES = True
    CIPHER_CHAIN.append('sumlines')
if args.sum:
    SUM = True
    CIPHER_CHAIN.append('sum')
if args.wordsonly:
    WORDS_ONLY = True

if args.runes:
    LANG = 'runes'
elif args.latin:
    LANG = 'latin'

if args.X == 'all':
    for i, targ in enumerate(getattr(LP, TARGET)):
        print(f'{bcolors.BOLD}{bcolors.WARNING}\n\n======= {TARGET[:-1].upper()} {i} ======={bcolors.ENDC}')
        throw_shit(targ)

elif args.X[0] == 'u':
    if args.X[1:] == 'all':
        for i, targ in enumerate(getattr(LP, TARGET)[15:]):
            print(f'{bcolors.BOLD}{bcolors.WARNING}\n\n======= {TARGET[:-1].upper()} {i} ======={bcolors.ENDC}')
            throw_shit(targ)
    else:
        print(f'{bcolors.BOLD}{bcolors.WARNING}\n\n======= {TARGET[:-1].upper()} {args.X[1:]} ======={bcolors.ENDC}')
        throw_shit(getattr(LP, TARGET)[int(args.X[1:]) + 15])
else:
    print(f'{bcolors.BOLD}{bcolors.WARNING}\n\n======= {TARGET[:-1].upper()} {args.X} ======={bcolors.ENDC}')
    throw_shit(getattr(LP, TARGET)[int(args.X)])
