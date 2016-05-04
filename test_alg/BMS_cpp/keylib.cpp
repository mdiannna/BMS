#include <iostream>
#include <stdio.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#include "keylib.h"
#include <vector>


using namespace std;

// Read First Key from standard input
int* readKey(int FK_int, int first_key_len){
    arr FK;

    for(int i=first_key_len-1; i>=0; i--){
        FK[i] = FK_int % 10;
        FK_int = FK_int / 10;
    }

    return FK;
}


void readArray(int FK_int, int key_len){
    arr A;
    int nr = 0;
    cin >> nr;
    for(int i=key_len-1; i>=0; i--){
        A[i] = FK_int %10;
        nr = nr / 10;
    }
}


//Print First Key
void printKey( arr FK, int key_len){
    cout << "Key is:" << endl;
    for(int i=0; i<key_len; i++)
        cout << FK[i];
}


void printArray(arr A, int len){
    for(int i=0; i<len; i++)
        cout << A[i] << " ";
    cout << endl;
}


// Transform First Key to actual key and read information from first key
int * keyTransform(arr first_key, int first_key_len){
    int * K;
    int pos_block = 3;
    int cursor = 0;
    while(cursor < first_key_len){
        if(cursor == pos_block){

        }
        cursor++;

    }
    return K;
}


int * getRandom( int key_len)
{
  int  r[key_len];

  // set the seed
  srand( (unsigned)time( NULL ) );
  for (int i = 0; i < key_len; ++i)
  {
    r[i] = rand() % 9 + 1;
    cout << r[i] << endl;
  }

  return r;
}


int * generateRandomKey(int key_len){

    arr random_key;

    // srand( (unsigned)time( NULL ) );
    for(int i=0; i<key_len; i++){
        random_key[i] = rand() % 9 + 1;
        // cout << random_key[i] << " ";
    }
    // cout << "***" << endl; 
    return random_key;
}


string separateText(string plaintext, int key_len){
    int pos = plaintext.length() - key_len;
    return plaintext.substr(0, pos);
}


string separateKey(string plaintext, int key_len){
    int pos = plaintext.length() - key_len;
    return plaintext.substr(pos, key_len);
}
