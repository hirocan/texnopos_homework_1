from random import choice
def getPrime(minN, maxN, flag = False, primes = []):
    for num in range(minN, maxN):
        for get in range(2,num):
            if num % get == 0:
                flag = True
                break
        if not flag:
            primes.append(num)
        flag = False
    return primes
def getPubExp(minN, maxN, Fn, pubExp = []):
    for e in range(minN, maxN):
        d = int((1 + 2 * Fn) / e)
        if d * e == 1 + 2 * Fn:
            pubExp.append(e)
    return pubExp
def getNumK(minN, maxN, Fn, e, numK = []):
    for k in range(minN, maxN):
        d = int((1 + k * Fn) / e)
    if d * e == 1 + k * Fn:
        numK.append(k)
    return numK
def getPrivExp(e, n, Fn, k):
    d = int((1 + k * Fn) / e)
    if d * e != 1 + k * Fn:
        raise SystemExit
    return d
def generateKeys(minP, maxP, maxN):
    primes = getPrime(minP,maxP)
    p, q = choice(primes), choice(primes)
    if p == q: return generateKeys(minP, maxP, maxN)
    n, Fn = p*q, (p-1)*(q-1)
    try:
        pubExp = getPubExp(2, maxN, Fn)[0]
        numK = getNumK(2, maxN, Fn, pubExp)[0]
        privExp = getPrivExp(pubExp, n, Fn, numK)
    except: return generateKeys(minP, maxP, maxN)
    if pubExp > privExp: return generateKeys(minP, maxP, maxN)
    return ([pubExp,n], [privExp,n])
def encryptDecrypt(message, key):
    return powerWithModule(message,key[0],key[1])
def powerWithModule(message, power, mod, result = 1):
    for _ in range(power):
        result = result * message % mod
    return result
while True:
    try:
        cryptMode = input("[G]enerate_[C]ipher: ").upper()
    except KeyboardInterrupt:
        print(); raise SystemExit
    if cryptMode == 'G':
        pub, priv = generateKeys(50,500,25)
        print("Public_key: [%d.%d]\nPrivate_key: [%d.%d]\n"%
        (pub[0], pub[1], priv[0], priv[1]))
    elif cryptMode == 'C':
        try:
            startMessage = int(input("Write the number: "))
            rsaKey = [int(k) for k in input("Write the key: ").split(".")]
        except (KeyboardInterrupt, ValueError):
            print(); raise SystemExit
        print("Final message: %d\n"%(encryptDecrypt(startMessage,
rsaKey)))
    else:
        print("Error: mode is not found")
        raise SystemExit
