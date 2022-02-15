#!/usr/bin/python3

#pythle

import random, sys, os, re

RESET_RE = '\033\[0m'
RESET = '\033[0m'
COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(30, 38))
            ))
        )

COLORS_RE = '\033\[(?:%s)m' % '|'.join(['%d' % v for v in COLORS.values()])

def colored(text, color=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = re.sub(COLORS_RE + '(.*?)' + RESET_RE, r'\1', text)
            text = fmt_str % (COLORS[color], text)
        return text + RESET
    else:
        return text

def out(stri):
    sys.stdout.write(stri)
    sys.stdout.flush()


wfile = open(__file__,"a")
rfile = open(__file__,"r")

def rmln(foo): return foo.replace("\n","")
file = list(map(rmln,rfile.readlines()))

data = file.pop()

if data == "newgame":
    afdata = input("pythle has no words yet. can you supply some? (text file)")
    wfile.write("\n#" + open(afdata).read())
else:
    out("-" * 10 + " PYTHLE v1 " + "-" * 10)
    out("\n" * 3)
    words = data[slice(1,-1)].split(",")
    word = words[random.randint(0,len(words)-1)]
    inp = ""
    x = 0
    while x < 6:
        inp = ""
        x += 1
        while len(inp) != 5 or (not inp in words):
            inp = input("Attempt " + str(x) + ":")
            out("\n")
            if len(inp) != 5: out("Word needs to have a length of 5.\n")
            if not inp in words: out("Invallid Word.\n")
            out("\n")
        
        al = 0
        for nu in range(len(inp)):
            char = inp[nu]
            if char in word:
                if inp[nu] == word[nu]:
                    out(colored(char,"green"))
                    al += 1
                else:
                    out(colored(char,"yellow"))
            else:
                out(char)
        
        if al == 5:
            print("\n\nYou Win! Word Was: " + colored(word,"green"))
            exit()
        
        print("\n\n------------\n")
    print("You didn't guess the right word. Good luck next time! Word Was: " + colored(word,"red"))

exit()
newgame