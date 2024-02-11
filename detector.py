import re
from termcolor import colored

bureau="(BUREAU|BUEREAU|BUEARU|BUERO|BÜRO|BURO|BIRO|BIURO|BUREU|OFFICE|BUERAU|BURAU|BUREO|BUREAO|BURÓ|BIREAU|BUREA|BEURO|ASOCIACION|DARC|DOK|BAUNATAL|USKA|RSGB|NRRL)"

positives = [
   ".*VIA.*"+bureau ,
   ".*"+bureau ,
   "([A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]\d\d|)$",
   "(PLEASE|PSE|)ONLY PAPER QSL",
]

negatives = [
    "^NO$",
    ".*NO MEMBER.*",
    ".*NO "+bureau+".*",
    ".*NOT "+bureau+".*",
    ".*NO VIA"+bureau+".*",
    ".*NOT VIA"+bureau+".*",
    ".*NO QSL VIA"+bureau+".*",
    ".*NOT QSL VIA"+bureau+".*",
    ".*NO MORE "+bureau+".*",
    ".*NOT IN "+bureau+".*",
    ".*NO QSL (PLEASE|).*",
    ".*NO CARDS (PLEASE|).*",
    ".*PLEASE DO NOT SEND QSL (CARDS|) VIA.*"+bureau,
    ".*PLEASE NO QSL.*",
    ".*YOUR QSL IS NOT NEEDED.*",
    ".*(I|WE) NEED NO CARDS.*",
    ".*DON'T REPLY PLEASE.*",
    ".*NM DARC.*",
    ".*NOT MEMBER OF DARC.*",
    ".*I DO NOT USE THE "+bureau+".*",
    ".*I DO NOT USE "+bureau+".*",
]

file = open("via_global3.txt", "r")

for line in file.read().splitlines() :
    line = line.upper()
    bureau = False

    for positive in positives :
        if re.match(positive, line) :
            bureau = True
    for negative in negatives :
        if re.match(negative, line) :
            bureau = False
    
    if bureau == True :
        print(colored(line,'green'))
    else:
        print(colored(line,'red'))
