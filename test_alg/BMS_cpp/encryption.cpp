#include <iostream>
#include <stdio.h>
#include <time.h>
#include <string>
//#include <stream.h>
#include <sstream>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#include "keylib.h"



void readKey(int int_key, arr &K, int &key_len){
    key_len = 0;
    int nr1 = 0;
    int nr2 = 0;

    nr2 = int_key;

    while(int_key>0){
        int_key = int_key / 10;
        key_len++;
    }

    int i = key_len - 1;

    while(nr2>0){
        K[i] = nr2 %10;
        nr2 = nr2 / 10;
        i--;
    }

}



char random_ch(){
    return (char)(rand() % 2) + 48;
}


string simpleencryptMessage(string message, arr K, int key_len){
    string ciphertext = "";
    int letter_pos = 0;
    int key_pos = 0;
    int message_len = message.length();

    while(letter_pos < message_len){

        for(int i=0; i<K[key_pos]; i++){
            ciphertext = ciphertext + random_ch();
        }
        ciphertext = ciphertext + message[letter_pos];

        key_pos++;
        letter_pos++;

        if(key_pos == key_len)
            key_pos = 0;
    }

     for(int i=0; i<K[key_pos]; i++){
            ciphertext = ciphertext + random_ch();
    }

    return ciphertext;
}


string blockEncryption (int block_size , string plaintext , arr K, int key_len)
{
    string ciphertext = "";
    int letter_pos = 0;
    int i = 0;
    int plaintext_len = plaintext.length();
    string ithmessage;
    while (letter_pos < plaintext_len)
    {
        ithmessage = "";
        if (plaintext_len-letter_pos<block_size)
            block_size = plaintext_len-letter_pos;
        ithmessage = plaintext.substr(letter_pos,block_size);
        letter_pos += block_size;
        ciphertext = ciphertext + simpleencryptMessage( ithmessage,  K, key_len);
    }
    return ciphertext;
}


string NumberToString ( int Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}


string intArrTochar(arr J,int key_len){
    string rez="";
    int key_int = 0;
    for (int i=0; i<key_len; i++){
        key_int = key_int*10 + J[i];
    }

    rez = NumberToString(key_int);
    return rez;
}


void pointerToArray(int * p, arr &A, int len){
    for ( int i = 0; i < len; i++ )
   {
       A[i] = *(p+i);
   }
}


string blockEncryptionV4 (int block_size , string plaintext , arr K, int key_len)
{
    string ciphertext = "";
    int letter_pos = 0;
    int i = 0;
    int plaintext_len = plaintext.length();
    string ithmessage;
    int * J;
    arr arr_J;
    // arr arr_J;
    arr prev_K;
    pointerToArray(K, prev_K, key_len);

   // cout<<"letter pos is "<<letter_pos<<endl<<"plaintext len is "<<plaintext_len <<endl;
    while (letter_pos < plaintext_len)
    {
        ithmessage = "";
        if (plaintext_len-letter_pos<block_size)
            block_size = plaintext_len-letter_pos;

        ithmessage = plaintext.substr(letter_pos, block_size);
        cout << "ith message:" << ithmessage << endl;

        // !!! Carefully! Risk of error!!
       

        J = generateRandomKey(key_len);
       
       // for ( int i = 0; i < 10; i++ )
       // {
       //     arr_J[i] = *(J + i) << endl;
       // }
       //  // pointerToArray(J, arr_J, key_len);

         cout << "Random key:";
        printArray(prev_K, key_len);

        string rand_key = intArrTochar(J, key_len);
        ithmessage += rand_key;

        letter_pos += block_size;
        ciphertext = ciphertext + simpleencryptMessage( ithmessage,  prev_K, key_len);
        pointerToArray(J, prev_K, key_len);
    }
    return ciphertext;
}



