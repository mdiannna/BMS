#include <string>
#include <iostream>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#include "decryption.h"
#include "keylib.h"

using namespace std;


string simpleDecrypt(string ciphertext, arr K,  int key_len)
{

    string plaintext;
    plaintext = "";
    int key_pos = 0;
	int cipher_pos = 0;
	int ciphertext_len = ciphertext.length();

	cout << "----ciphertext=" <<  ciphertext << "    ciphertext_len =" << ciphertext_len << endl;

    while(cipher_pos<ciphertext_len){
        cipher_pos = cipher_pos + K[key_pos];
        if(cipher_pos<ciphertext_len)
            plaintext = plaintext + ciphertext[cipher_pos];
        key_pos ++;
        cipher_pos++;
        if(key_pos == key_len)
            key_pos = 0;
    }

    return plaintext;
}


int calcCipherblockLen(int block_size, arr K, int key_len)
{
    int cipherblock_len = block_size;
    int key_pos = 0;
    for(int i=0; i<block_size + 1; i++){
        cipherblock_len += K[key_pos];
        key_pos++;
        if(key_pos == key_len)
            key_pos = 0;
        //cout << "K[" << key_pos << "]=" << K[key_pos] << endl;

    }
    return cipherblock_len;
}


int calcCipherblockLenV4(int block_size, arr K, int key_len)
{
    int cipherblock_len = block_size + key_len;
    int key_pos = 0;
    for(int i=0; i<block_size + key_len + 1; i++){
        cipherblock_len += K[key_pos];
        key_pos++;
        if(key_pos == key_len)
            key_pos = 0;
        //cout << "K[" << key_pos << "]=" << K[key_pos] << endl;
    }
    return cipherblock_len;
}


string blockDecrypt(string ciphertext, arr K, int key_len, int block_size)
{
    int block_pos = 0;
    int ciphertext_len = ciphertext.length();
    int cipherblock_len = 0;
    int remaining_ciphertext_len = 0;
    string plaintext = "";



    while(block_pos<ciphertext_len-1)
    {
        remaining_ciphertext_len = ciphertext_len-block_pos-1;
        cipherblock_len = calcCipherblockLen(block_size, K, key_len);

        if(remaining_ciphertext_len < cipherblock_len)
            cipherblock_len = remaining_ciphertext_len;

        string cipherblock = ciphertext.substr(block_pos, cipherblock_len);

        cout << "Cipherblock: " << cipherblock << "   Plainblock:" << simpleDecrypt(cipherblock, K, key_len) << endl;
        plaintext += simpleDecrypt(cipherblock, K, key_len);

        block_pos += cipherblock_len;
    }
    return plaintext;
}




string blockDecryptV4(string ciphertext, arr K, int key_len, int block_size)
{
    cout << "start decryption function" << endl;

    int block_pos = 0;
    int ciphertext_len = ciphertext.length();
    int cipherblock_len = 0;
    int remaining_ciphertext_len = 0;
    string raw_plaintext = "";
    string plaintext = "";
    int key_int = 0;

    arr K2;

    cout << "2start decryption function" << endl;

    while(block_pos<ciphertext_len-1)
    {
        remaining_ciphertext_len = ciphertext_len-block_pos-1;
        cipherblock_len = calcCipherblockLenV4(block_size, K, key_len);

        cout << "cipherblock length:" << cipherblock_len << endl;
    

        if(remaining_ciphertext_len < cipherblock_len)
            cipherblock_len = remaining_ciphertext_len;

        string cipherblock = ciphertext.substr(block_pos, cipherblock_len);
        raw_plaintext = simpleDecrypt(cipherblock, K, key_len);

        plaintext += separateText(raw_plaintext, key_len);
        cout << "raw_plaintext:" << raw_plaintext << endl;
        //////////////////////
          // block_pos += cipherblock_len;
    // }
        key_int = atoi(separateKey(raw_plaintext, key_len).c_str());
        
        cout << "key_int:" << key_int << endl;
        K = readKey(key_int, key_len);
        cout << "K:" << endl;
        printArray(K, key_len);

        block_pos += cipherblock_len;
    }
    return plaintext;
    // return ciphertext;
}
