import random

def generate_keystream(length, seed):
    random.seed(seed)  # Seed the random number generator
    
    keystream = []
    for _ in range(length):
        keystream.append(random.randint(0, 255))  # Generate a random number between 0 and 255 (inclusive)
    
    return keystream


def ordFunction(list_word):
    newwords = [ord(x) for x in list_word]
    return newwords

def numToAscii(word):
    lista = []
    for x in word:
        temporal = []
        while x != 0:
            bin = x % 2
            temporal.insert(0,bin)
            x = x // 2
        while len(temporal) < 8:
            temporal.insert(0,0)
        lista.append(temporal)
    # print(lista)
    return lista

def valXor(word,key):
    xorfile = []
    for i in range(len(word)):
        for j in range(8):
            if word[i][j] == key[i][j]:
                xorfile.append(0)
            else:
                xorfile.append(1)
                
    # print(xorfile)
    newlist = []
    temporal = []
    for x in xorfile:
        if len(temporal) <8:
            temporal.append(x)
        else:
            newlist.append(temporal)
            temporal = [x]
        
    if temporal:
        newlist.append(temporal)
    # print(newlist)
    
    lista = []
    for x in newlist:
        # print(x)
        x.reverse()
        # print(x)
        value = 0
        for i in range(8):
            value += 2**i * x[i]
        lista.append(value)
    # print(lista)
    
    final = []
    for x in lista:
        final.append(chr(x))
        
    # print(final)
    return final

def xorVal(word,key):
    newword = []
    for x in word:
        for i in x:
            newword.append(ord(i))
    # print(newword)
    word = numToAscii(newword)
    
    xorfile = []
    for i in range(len(word)):
        for j in range(8):
            if word[i][j] == key[i][j]:
                xorfile.append(0)
            else:
                xorfile.append(1)
                
    # print(xorfile)
    newlist = []
    temporal = []
    for x in xorfile:
        if len(temporal) <8:
            temporal.append(x)
        else:
            newlist.append(temporal)
            temporal = [x]
        
    if temporal:
        newlist.append(temporal)
    # print(newlist)
    
    lista = []
    for x in newlist:
        # print(x)
        x.reverse()
        # print(x)
        value = 0
        for i in range(8):
            value += 2**i * x[i]
        lista.append(value)
    # print(lista)
    
    final = []
    for x in lista:
        final.append(chr(x))
        
    # print(final)
    return final

mensaje = input("Ingrese el texto a cifrar: ")
ord_mensaje = ordFunction(mensaje)
ascii_mensaje = numToAscii(ord_mensaje)
# print(ascii_mensaje)

seed= random.randint(1,999999999)
keystream = generate_keystream(len(mensaje),seed)
ascii_key = numToAscii(keystream)
print("keystrean: ",keystream)
# print(ascii_key)

xor_value = valXor(ascii_mensaje,ascii_key)
val = "".join(xor_value)
print("xor result: ",val)

value = xorVal(xor_value,ascii_key)
val = "".join(value)
print("Desecnript value: ", val)
