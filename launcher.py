import sys, time
from hashfunction import Hash

def fetch(fname: str, tname: str, maxThreads: int=50000):
    print("Fetch every hash for passwordlist: " + fname + " => " + tname +  " | maxThreads: " + str(maxThreads))
    time.sleep(1)
    
    file = open(fname, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    
    file = open(tname, "a", encoding="utf-8")
    c = 1
    for val in lines:
        val = val.replace("\n", "")
        try:
            val_h = hashFunction.hexHash(val)
            print(c, val, val_h)
            file.write(val_h + "\n")
        except:
            print(c, val, "!no hash")
            file.write("no hash: [" + val + "]\n")
        if c == maxThreads: break
        c+=1
    file.close()
    print("Fetch done. " + str(c-1) + " strings hashed")
    
def range_(tname: str, start: int=10, end: int=200):
    print("Fetch every hash for stringrange: " + tname + " | range: " + str(start) + "|" + str(end))
    time.sleep(1)
    
    file = open(tname, "a", encoding="utf-8")
    c = 1
    c_ = 1
    for v in range(start, end):
        st = "a"*v
        for i in "abcdefghijklmnopqrstuvwxyz":
            st_ = st + i
            val_h = hashFunction.hexHash(st_)
            print(c, st_, val_h)
            file.write(val_h + "\n")
            c_+=1
        c+=1
    file.close()
    print("Fetch done. " + str(c-1) + "|" + str(c_-1) + " strings hashed")

def chain(word: str, tname: str, end: int=1000):
    print("Chain hashes from 1 word: " + str(word) + " | " +  tname +" | maxThreads: " + str(maxThreads))
    time.sleep(1)
    
    file = open(tname, "a", encoding="utf-8")
    firstWord = word
    c = 1
    while c <= maxThreads:
        val_h = hashFunction.hexHash(word)
        if len(word) > 16: print(c, word[:16]+"...", val_h)
        else: print(c, word, val_h)
        file.write(val_h + "\n")
        word = val_h
        c+=1
    file.close()
    print("Fetch done. " + str(c-1) + "|" + str(firstWord) + " strings hashed")

def collision(tname: str):
    print("Check hashlist for collisions: " + fname)
    time.sleep(1)
    
    file = open(fname, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    
    c = 1
    for val in lines:
        print(str(c) + "/" + str(len(lines)), val.replace("\n", ""))
        if lines.count(val) > 1:
            print("=> collision found:", c, val.replace("\n", ""), "\n=> " + str(lines.count(val)) + " times")
            quit()
        c+=1
    print("No collisions found :)")

def sendHelp(t: int=-1):
    fileName = str(sys.argv[0])
    print(fileName + " | " + str("Usage error #" + str(t)).replace("Usage error #-1", "Help"))
    if t == -1: print("$> python " + fileName + " <words>")
    if t == 1 or t == -1: print("$> python " + fileName + " -fetch <filename: str> <targetname: str> <maxThreads: int>")
    if t == 2 or t == -1: print("$> python " + fileName + " -range <targetname: str> <start: int> <end: int>")
    if t == 3 or t == -1: print("$> python " + fileName + " -chain <targetname: str> <end: int>")
    if t == 4 or t == -1: print("$> python " + fileName + " -collision <filename: str>")
    if t == -1: print("For more information go here: https://github.com/Delta203/Hashfunction/blob/main/README.md")
    if t == -1: print("Full project: https://github.com/Delta203/Hashfunction")
    quit()

# usage: python hashfunction.py <words>
start_time = time.time()

w = ""
for i in range(1, len(sys.argv)):
    w = w + " " + sys.argv[i]
w = w[1:]

hashFunction = Hash()

if len(w) == 0:
    sendHelp()

fname = ""

if w.startswith("-fetch"):
    try: fname = sys.argv[2]
    except: sendHelp(1)
    tname = ""
    try: tname = sys.argv[3]
    except: sendHelp(1)
    maxThreads = 50000
    try: maxThreads = int(sys.argv[4])
    except: pass
    fetch(fname, tname, maxThreads)
    
elif w.startswith("-range"):
    try: fname = sys.argv[2]
    except: sendHelp(2)
    start = 10
    try: start = int(sys.argv[3])
    except: pass
    end = 200
    try: end = int(sys.argv[4])
    except: pass
    range_(fname, start, end)
    
elif w.startswith("-chain"):
    try: fname = sys.argv[2]
    except: sendHelp(3)
    word = ""
    try: word = sys.argv[3]
    except: sendHelp(3)
    maxThreads = 50
    try: maxThreads = int(sys.argv[4])
    except: pass
    chain(word, fname, maxThreads)
    
elif w.startswith("-collision"):
    try: fname = sys.argv[2]
    except: sendHelp(4)
    collision(fname)
    
else:
    print("input       :", w)
    print("hash        :", hashFunction.hexHash(w, False, True))

end_time = time.time()
print("process time:", str(round(end_time-start_time, 6)) + "sec")
