/*
Modified version of designer's implementation
 * Simmulation of boomerang analysis for Skinny
 * Date: March 21, 2020
 * Author: Hosein Hadipour
 * Contact: hsn.hadipour@gmail.com
*/
// CRAFT Cipher 
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <string>
#include <math.h>
#include <omp.h>
#include <iostream>
using namespace std;
#define Nthreads 12 // Number of parallel threads
typedef unsigned long long int UINT64;

					  //0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF
const uint8_t S[16] = { 0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6 };
const uint8_t P[16] = { 0xF, 0xC, 0xD, 0xE, 0xA, 0x9, 0x8, 0xB, 0x6, 0x5, 0x4, 0x7, 0x1, 0x2, 0x3, 0x0 };
const uint8_t Q[16] = { 0xC, 0xA, 0xF, 0x5, 0xE, 0x8, 0x9, 0x2, 0xB, 0x3, 0x7, 0x4, 0x6, 0x0, 0x1, 0xD };
const uint8_t RC3[32] = { 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5 };
const uint8_t RC4[32] = { 0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6, 0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6, 0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8 };

void print_state(uint8_t state[16])
{
    for (int i = 0; i < 16; i++)
        printf("%01x", state[i]);
    printf("\n");
}

void convert_hexstr_to_statearray(string hex_str, uint8_t int_array[16], bool reversed = false)
{
    if (reversed == true)
        for (size_t i = 0; i < 16; i++)
            int_array[15 - i] = static_cast<uint8_t>(stoi(hex_str.substr(i, 1), 0, 16) & 0xf);
    else
        for (size_t i = 0; i < 16; i++)
            int_array[i] = static_cast<uint8_t>(stoi(hex_str.substr(i, 1), 0, 16) & 0xf);
}

void initialize(uint8_t key0[16], uint8_t key1[16], uint8_t master_tweak[16], uint8_t tk[][16]) {
	for (uint8_t i = 0; i < 16; i++)
		tk[0][i] = (key0[i] & 0xf);
	for (uint8_t i = 0; i < 16; i++)
		tk[1][i] = (key1[i] & 0xf);
	for (uint8_t i = 0; i < 16; i++)
		tk[2][i] = tk[0][i];
	for (uint8_t i = 0; i < 16; i++)
		tk[3][i] = tk[1][i];

	for (uint8_t i = 0; i < 16; i++)
		tk[0][i] ^= (master_tweak[i] & 0xf);
	for (uint8_t i = 0; i < 16; i++)
		tk[1][i] ^= (master_tweak[i] & 0xf);
	for (uint8_t i = 0; i < 16; i++)
		tk[2][i] ^= (master_tweak[Q[i]] & 0xf);
	for (uint8_t i = 0; i < 16; i++)
		tk[3][i] ^= (master_tweak[Q[i]] & 0xf);
    // printf("\nTK_enc00: ");
    // for (uint8_t i = 0; i < 16; i++)
    //     printf("%X", tk[0][i]);
    // printf("\nTK_enc01: ");
    // for (uint8_t i = 0; i < 16; i++)
    //     printf("%X", tk[1][i]);
    // printf("\nTK_enc10: ");
    // for (uint8_t i = 0; i < 16; i++)
    //     printf("%X", tk[2][i]);
    // printf("\nTK_enc11: ");
    // for (uint8_t i = 0; i < 16; i++)
    //     printf("%X", tk[3][i]);
}

void enc(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t tk[][16]) {
    for (uint8_t i = 0; i < 16; i++) {
        ciphertext[i] = plaintext[i] & 0xf;
    }
    for (uint8_t r = 0; r < R; r++) {        
        //MixColumn
        for (uint8_t i = 0; i < 4; i++) {
            ciphertext[i] ^= (ciphertext[i + 8] ^ ciphertext[i + 12]);
            ciphertext[i + 4] ^= ciphertext[i + 12];
        }

        //AddConstant
        ciphertext[4] ^= RC4[r];
        ciphertext[5] ^= RC3[r];

        //AddTweakey
        for (uint8_t i = 0; i < 16; i++) {            
            ciphertext[i] ^= tk[r % 4][i];
        }
            
        
        if (r != 31) {
            //Permutation
            uint8_t Temp[16];
            for (uint8_t i = 0; i < 16; i++)
                Temp[P[i]] = ciphertext[i];
                        
            // SBox
            for (uint8_t i = 0; i < 16; i++)
                ciphertext[i] = S[Temp[i]];
        }
        // Next State
        // printf("\nR%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", ciphertext[i]);
    }
}


void dec(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t tk[][16]) {    
    for (uint8_t i = 0; i < 16; i++) {
        plaintext[i] = ciphertext[i] & 0xf;
    }
    int ind;
    for (int r = 0; r < R; r++) {
        // SBox        
        for (uint8_t i = 0; i < 16; i++)
            plaintext[i] = S[plaintext[i]];        
        //Permutation            
        uint8_t Temp[16];
        for (uint8_t i = 0; i < 16; i++)
            Temp[i] = plaintext[P[i]];
        //AddTweakey
        ind = R - r - 1;        
        for (uint8_t i = 0; i < 16; i++)
            plaintext[i] = Temp[i] ^ tk[ind % 4][i];
        //AddConstant        
        plaintext[4] ^= RC4[ind];
        plaintext[5] ^= RC3[ind];
        //MixColumn
        for (uint8_t i = 0; i < 4; i++) {
            plaintext[i] ^= (plaintext[i + 8] ^ plaintext[i + 12]);
            plaintext[i + 4] ^= plaintext[i + 12];
        }
        //Next State
        // printf("\nR%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", plaintext[i]);
    }
}

int main() {
    int r = 12; // Number of rounds
    string k0_str = "1e97469ac59c9ea9";
    string k1_str = "fe87e344887e3ee5";
    string tweak_str = "c1bd0a3437864c1f";    
    string p1_str = "7f39ad1a3683588f";
    string p2_str = "7f93ad103c235885";
    string p3_str = "4329c595f6d51b67";
    string p4_str = "4383c59ffc751b6d";

    //#################################################################################
    uint8_t key0[16];
    uint8_t key1[16];    
    uint8_t master_tweak[16];
    uint8_t tk[4][16];
    uint8_t p1[16];
    uint8_t p2[16];
    uint8_t p3[16];
    uint8_t p4[16];
    uint8_t c1[16];
    uint8_t c2[16];
    uint8_t c3[16];
    uint8_t c4[16];
    bool reversed = false;
    convert_hexstr_to_statearray(p1_str, p1, reversed);
    convert_hexstr_to_statearray(p2_str, p2, reversed);
    convert_hexstr_to_statearray(p3_str, p3, reversed);
    convert_hexstr_to_statearray(p4_str, p4, reversed);
    convert_hexstr_to_statearray(k0_str, key0, reversed);
    convert_hexstr_to_statearray(k1_str, key1, reversed);
    convert_hexstr_to_statearray(tweak_str, master_tweak, reversed);

    initialize(key0, key1, master_tweak, tk);
    enc(r, p1, c1, tk);
    enc(r, p2, c2, tk);
    enc(r, p3, c3, tk);
    enc(r, p4, c4, tk);
    printf("p1: ");
    print_state(p1);
    printf("p2: ");
    print_state(p2);
    printf("c1: ");
    print_state(c1);
    printf("c2: ");
    print_state(c2);
    printf("\np3: ");
    print_state(p3);
    printf("p4: ");
    print_state(p4);
    printf("c3: ");
    print_state(c3);
    printf("c4: ");
    print_state(c4);
    return 0;
}
