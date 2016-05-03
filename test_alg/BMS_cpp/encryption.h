#ifndef ENCRYPTION_H_INCLUDED
#define ENCRYPTION_H_INCLUDED
//#include <string.h>

typedef int arr[10000];
using namespace std;

void readKey(int int_key, arr &K, int &key_len);
//void printArray(arr A, int len);
char random_ch();
string simpleencryptMessage(string message, arr K, int key_len);
string blockEncryption (int block_size , string plaintext , arr K, int key_len);
string intArrTochar(arr J,int key_len);
string blockEncryptionV4 (int block_size , string plaintext , arr K, int key_len);

#endif // ENCRYPTION_H_INCLUDED
