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
#boto3,wheel,numpy,click,attrs,pyjwt,wrapt,flask,scipy,smmap,gitdb,tomli,parso,regex,redis,pyzmq,ujson,isort,gcsfs,black,babel,toolz,keras,anyio,numba,uamqp,knack,torch,retry,astor,faker,jdcal,ijson,arrow,pylev,httpx,patsy,cachy,kombu,typer,spacy,ecdsa,thinc,tblib,srsly,cymem,emoji,pydot,partd,ephem,geopy,munch,twine,fiona,cligj,bokeh,pyotp,hpack,pathy,parse,clang,s3cmd,pyaml,motor,sympy,scapy,aenum,patch,oyaml,vcrpy,uwsgi,webob,w3lib,pydub,json5,dpath,ldap3,kazoo,cliff,fysom,azure,sanic,pyxdg,agate,pyaes,raven,yappi,cmake,annoy,pyorc,pyyml,ninja,covid,funcy,cmaes,build,pyqt5,naked,pycel,flaky,luigi,rtree,minio,ws4py,wandb,j2cli,conan,qdldl,cvxpy,jieba,jsmin,quinn,odfpy,txaio,glob2,paste,py7zr,pyhdb,urwid,asana,trino,polib,nose2,pooch,pyusb,panel,ptvsd,cbor2,kafka,pamqp,async,ropwr,slack,pyhs2,arviz,pymc3,jsons,radon,pylru,param,ccard,edlib,pysmi,mxnet,mando,pydoe,kedro,pypng,gnupg,scanf,pygam,hjson,pysmb,pyu2f,shtab,meson,pyshp,kneed,ghapi,pyjks,delta,ngram,pyfcm,hyper,stone,pybcj,pdoc3,janus,pyhcl,fuzzy,awacs,mleap,mdurl,js2py,gdown,neo4j,modin,optax,mobly,pdbpp,apns2,mpld3,pysam,clint,scons,zenpy,dodgy,crc16,mgzip,carto,cnvrg,adlfs,image,pyicu,gcovr,rauth,pydyf,ffmpy,tendo,utils,names,pdfrw,pyvim,pyomo,cowpy,parsy,decli,salib,blist,hdfs3,sgqlc,lmfit,pygal,tatsu,pyro4,aiopg,nbval,mrjob,meld3,zappa,kappa,blspy,times,qiniu,pyvis,dirac,pyknp,emcee,dowhy,mysql,yapsy,roman,rules,lpips,conda,bpemb,pyang,textx,nylas,imath,mpire,pypdf,dlint,faust,tryme,grimp,xlrd3,flair,fpdf2,pyddq,clize,pgcli,pvlib,solrq,mixer,dagit,blosc,amply,leven,oauth,pgmpy,jiwer,first,unify,bunch,pydes,style,evdev,serpy,feast,tbats,etcd3,fido2,shade,pycli,authy,timer,alibi,pyemd,quart,pyro5,pecan,pymel,spyne,sarge,dtale,pylcs,email,pyatv,combo,mybad,pyvcf,eight,lorem,nbdev,clamd,dimod,saspy,civis,osmnx,spooq,pyuca,xattr,pansi,exrex,xenon
