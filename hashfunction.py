"""
Hash Function
Usage: from hashfunction import Hash
"""

class Hash:
    def __init__(self): pass
    
    def hexHash(self, st: str, printBlocks: bool=False, printBitHash: bool=False) -> str:
        """
        generate hash value
        output: hex 32 byte
        
        printBlocks : bool | debug binary value of string
        printBitHash : bool | debug bithash
        """
        st_len = len(st)
        blockLen = 512 # 512 for 32 byte hash
        minBlockAmount = blockLen * 3
        primeKey = 1373*st_len # key modulus high prime number avoiding quick collisions
        bitString = str(self.__stringToBinary(st)) + str(self.__stringToBinary(st))[::-1]
        if len(bitString) < minBlockAmount: bitString = (bitString*((minBlockAmount//len(bitString))+1))[:minBlockAmount]
        
        trim = [bitString[blockLen*x:blockLen*(x+1)] for x in range(len(bitString)//blockLen)]
        trimMod = [str(str(self.__stringToBinary(str(int(x) % primeKey))) * (blockLen//len(str(self.__stringToBinary(str(int(x) % primeKey))))+1))[:blockLen] for x in trim]
        trimfull = trim + trimMod
        
        cachebitHash = "0" * blockLen
        c = 0
        for i in trimfull:
            if printBlocks: print("Block " + str(c) + "     :", i, len(i))
            cachebitHash = self.__XOR(cachebitHash, i)
            c+=1
        bitHash = self.__XOR(cachebitHash[:blockLen//2], cachebitHash[blockLen//2:]) # compress 512 bit to 256 bits
        
        if printBitHash: print("bithash     :", bitHash, len(bitHash))
        hexHash = self.__numToHex(int(bitHash))
        
        return hexHash
    
    def __stringToBinary(self, st: str) -> int:
        return int("".join(format(ord(i), "08b") for i in st))
        
    def __numToHex(self, num: int) -> str:
        """ num: int | has to be bit format """
        return hex(int(str(num), 2))
    
    def __XOR(self, stnum1: str, stnum2: str) -> int:
        """
        xor number function
        len(stnum1) == len(stnum2)
        
        Returns: int | bit
        """
        result = ""
        for i in range(len(stnum1)):
            if i == 0: 
                result+="1"
                continue
            if stnum1[i] == "0" and stnum2[i] == "0": result+="0"
            elif stnum1[i] == "1" and stnum2[i] == "0": result+="1"
            elif stnum1[i] == "0" and stnum2[i] == "1": result+="1"
            elif stnum1[i] == "1" and stnum2[i] == "1": result+="0"
        return result
