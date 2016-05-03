#include <string>
#include "keylib.h"

using namespace std;

#ifndef DECRYPTION_H_INCLUDED
#define DECRYPTION_H_INCLUDED


string simpleDecrypt(string ciphertext, arr K,  int key_len);
int calcCipherblockLen(int block_size, arr K, int key_len);
string blockDecrypt(string ciphertext, arr K, int key_len, int block_size);
string blockDecryptV4(string ciphertext, arr K, int key_len, int block_size);


#endif // DECRYPTION_H_INCLUDED
