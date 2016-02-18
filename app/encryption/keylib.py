

def readKey(nr, K, key_len):
	key_len = 0
	nr1 = nr

	while nr>0:
		nr = nr / 10
		key_len += 1

	i = key_len - 1

	while nr1>0:
		K[i] = nr1 % 10
		nr1 = nr1 / 10
		i -= 1


def printK(K, key_len):
	for i in range(0, key_len):
		print K[i]


def firstKeyToKey(first_key, key_len, block_pos, del_pos):
    block_size = 0
    new_key = [0]*key_len
    new_key_pos = 0
 
    for i in range(block_pos+1, first_key[block_pos+first_key[block_pos]]):
        block_size = block_size*10 + first_key[i]
 
    print "block size:",block_size
 
    for key_pos in range(0, key_len):
        if key_pos >= del_pos and key_pos <= del_pos + first_key[del_pos]:
            pass
        elif key_pos >= block_pos and key_pos <= block_pos + first_key[block_pos]:
            pass
        else:
            new_key[new_key_pos] = first_key[key_pos]
            new_key_pos += 1
 
    
    return new_key, block_size


def keyTextSeparation(plaintext, block_size):
    plaintext_len = len(plaintext)
    key = ""
    text = ""
    for i in range(0, block_size):
        text += plaintext[i]
    for i in range(block_size, plaintext_len):
        key += plaintext[i]

    int_key = 0
    try:
        int_key = int(key)
    except:
        int_key = -1
    
    return int_key,  text
