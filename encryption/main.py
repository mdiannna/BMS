from encryption import encryptMessage, readKey, encryptBlocks


K = [0] * 100000000

key_len = 4;
key = 1232
plaintext = "AAAAAAAAA"
block_size = 3

readKey(key, K, key_len)

print encryptMessage(plaintext, K, key_len)

print "Encrypt Blocks of 3:"
print encryptBlocks(plaintext, K, key_len, block_size)