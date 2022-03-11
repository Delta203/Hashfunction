# Hashfunction
python3 32byte hashfunction<br/>
**Warning! You should not use this hashfunction for serious encryption. This function has not been tested by professionals.**<br/>

**Usage:**
```
# import class
from hashfunction import Hash

# register class
foo = Hash()
# generate hash
foo.hexHash(inputString: str, printBlocks: bool=False, printBitHash: bool=False)
```
```
$> python launcher.py <words>
$> python launcher.py -fetch <filename: str> <targetname: str> <maxThreads: int> | fetch password list
$> python launcher.py -range <filename: str> <start: int> <end: int> | generate password by "a"*n
$> python launcher.py -collision <filename: str>
```
___
**Construction:**
- Converting string to binary ("hello": str ⇒ 110100001100101011011000110110001101111)
- Adding reversed bitString to bitString (⇒ 110100001100101011011000110110001101111111101100011011000110110101001100001011)
- Pad the bitString to length 512(byte) * 3(minimum block amount) by repeatedly adding bitString to bitString<br/>
  (The amount of blocks depents on length of inputString|bitString)
- Split the long bitString into seperate 512 bit blocks (⇒ list of 512 bit blocks)

![](https://raw.githubusercontent.com/Delta203/Hashfunction/main/guideimages/pic1.PNG)
- Create another list with modulus values of each block(512 bit) % primeKey(very high primenumber * length of inputString)<br/>
  (eg: 110100001100101011011000110110001101111(39 bit) % 31(primeKey) = 6, "6" ⇒ 110110, pad 110110 to 512 bit by repeating)

![](https://raw.githubusercontent.com/Delta203/Hashfunction/main/guideimages/pic2.PNG)
- XOR every block with every block from split list and modulus list

![](https://raw.githubusercontent.com/Delta203/Hashfunction/main/guideimages/pic3.PNG)
- Compress 512 bitString by splitting the block into 256 bit blocks and XOR the two blocks
- Convert 256 bit block into 32 byte hex
```
$> python launcher.py hello
input       : hello
bithash     : 1010100100111001101010111110111011110000110100101010101000000110010111001011111000010101101101001110011111111100010101111011001100111100010000011110001111001011000111001011101010001111010100000101101000111001000000110011011011011010001110010110111100110100 256
hash        : 0xa939abeef0d2aa065cbe15b4e7fc57b33c41e3cb1cba8f505a390336da396f34
process time: 0.0sec
```
___
**Speed:**
- {a}^1000  = 0.020067sec sec ⇒ ```0x8b92ce0c089a0b62ffffbd3342630e4c56bd7979c08ba8050132dad650b4609b```
- {a}^8171  = 0.480313sec sec ⇒ ```0xcfdfb9ef1ee5f95f0853537271ee7bee5889d569ed4d0c97779b72d495c6feb7```
___
**Math calculating blocks:**
- *input*: string input
- *primeKey*: n ∈ ℕ, very high prime number
- *block* : b ∈ blocklist, b ⊆ {0,1}+, |b| = 512
- *block_mod* : bm ∈ moduluslist, bm = *block* % (*primeKey* * |*input*|), bm ⇒ 512 bit format
- *bitHash*: *bitHash* ⊕ x, ∀x ∈ blocklist ∪ moduluslist
- *finalHash*: *bitHash*[:256] ⊕ *bitHash*[256:], (256 bit format)
