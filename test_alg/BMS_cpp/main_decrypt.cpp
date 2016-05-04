#include <iostream>
#include <string>
#include "decryption.h"
#include "keylib.h"
#include "encryption.h"
#include <time.h>
#include <stdio.h>
#include <stdlib.h>


using namespace std;

arr FK; // first key, actual key
int * K;
arr K1;
int first_key_len, block_pos;


int main(int argc, char *argv[]){
    if(argc <3)
        cout << "Error! please specify message and key";
    else
{

        
        srand (time(NULL));

        string plaintext= "";
        string ciphertext = "";
        int block_size = 2;
        int key_len = 0;
        int int_key;
        arr K1;
    
        
        plaintext = argv[1];
        int_key = atoi(argv[2]);


        readKey(int_key, K1, key_len);

         ciphertext = blockEncryptionV4 ( block_size ,  plaintext , K1, key_len);
        // cout << "Ciphertext: " <<  ciphertext << endl;

        clock_t tStart = clock();
        plaintext = blockDecryptV4(ciphertext, K1, key_len, block_size);
        // cout << "Decrypted plaintext: "<< plaintext << endl;

        // printf("------------------------\n");
        // printf("----Time taken: -- %.29f ms \n", (double)(clock() - tStart)*1000/CLOCKS_PER_SEC);
        // printf("------------------------\n");

        printf("%.29f\n", (double)(clock() - tStart)*1000/CLOCKS_PER_SEC);
    }

    return 0;
}

