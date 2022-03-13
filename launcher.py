import sys, time
from hashfunction import Hash

# usage: python hashfunction.py <words>
start_time = time.time()

w = ""
for i in range(1, len(sys.argv)):
    w = w + " " + sys.argv[i]
w = w[1:]

hashFunction = Hash()

if w.startswith("-fetch"):
    fname = sys.argv[2]
    ftname = sys.argv[3]
    maxThreads = 50000
    try: maxThreads = int(sys.argv[4])
    except: pass
    print("Fetch every hash for passwordlist: " + fname + " | maxThreads: " + str(maxThreads))
    time.sleep(1)
    
    file = open(fname, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    
    file = open(ftname, "a", encoding="utf-8")
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
elif w.startswith("-range"):
    ftname = sys.argv[2]
    start = 10
    try: start = int(sys.argv[3])
    except: pass
    maxThreads = 200
    try: maxThreads = int(sys.argv[4])
    except: pass
    print("Fetch every hash for passwordlist: range() | range: " + str(start) + "|" + str(maxThreads))
    time.sleep(1)
    
    file = open(ftname, "a", encoding="utf-8")
    c = 1
    c_ = 1
    for v in range(start, maxThreads):
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
elif w.startswith("-chain"):
    ftname = sys.argv[2]
    word = sys.argv[3]
    firstWord = word
    maxThreads = 50
    try: maxThreads = int(sys.argv[4])
    except: pass
    print("Chain hashes from 1 word: chain() | word: " + str(word) + "|" + str(maxThreads))
    time.sleep(1)
    
    file = open(ftname, "a", encoding="utf-8")
    c = 1
    while c<=maxThreads:
        val_h = hashFunction.hexHash(word)
        if len(word) > 16: print(c, word[:16]+"...", val_h)
        else: print(c, word, val_h)
        file.write(val_h + "\n")
        word = val_h
        c+=1
    file.close()
    print("Fetch done. " + str(c-1) + "|" + str(firstWord) + " strings hashed")
elif w.startswith("-collision"):
    fname = sys.argv[2]
    print("Check hashlist for collisions: " + fname)
    time.sleep(1)
    
    file = open(fname, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    
    c = 1
    for val in lines:
        print(c, val.replace("\n", ""))
        if lines.count(val) > 1:
            print("=> collision found:", c, val.replace("\n", ""), "\n=> " + str(lines.count(val)) + " times")
            quit()
        c+=1
    print("No collisions found :)")
else:
    print("input       :", w)
    print("hash        :", hashFunction.hexHash(w, False, True))

end_time = time.time()
print("process time:", str(round(end_time-start_time, 6)) + "sec")
