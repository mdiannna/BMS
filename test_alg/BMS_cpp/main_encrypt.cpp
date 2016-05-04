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
    else{


        srand (time(NULL));

        string plaintext= "";
        string ciphertext = "";
        int block_size = 2;
        int key_len = 0;
        int int_key;
        arr K1;

        // plaintext = "AAAAAA";
        // int_key = 12;

        plaintext = argv[1];
        int_key = atoi(argv[2]);


        readKey(int_key, K1, key_len);

        // cout << "plaintext:" << plaintext;
        // cout << "int_key:" << int_key;
        // cout << "key_len:" << key_len;
        
        clock_t tStart = clock();

        ciphertext = blockEncryptionV4 ( block_size ,  plaintext , K1, key_len);
        // Ca sa mearga graficele trebuie sters rindul
        // cout << "Ciphertext: " <<  ciphertext << endl << "key_len:" << key_len << endl;


        printf("%.29f\n", (double)(clock() - tStart)*1000/CLOCKS_PER_SEC);
    }

    return 0;
}

