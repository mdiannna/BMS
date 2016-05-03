#ifndef KEYLIB_H_INCLUDED
#define KEYLIB_H_INCLUDED

#include <string>
using namespace std;

typedef int arr[10000];
//typedef int* arr;


int* readKey(int FK_int, int first_key_len);
void readArray(int FK_int, int key_len);
void printKey(arr FK, int first_key_len);
void printArray(arr A, int len);
int * keyTransform(arr first_key, int first_key_len);
int * generateRandomKey(int key_len);
string separateText(string plaintext, int key_len);
string separateKey(string plaintext, int key_len);

#endif // KEYLIB_H_INCLUDED
