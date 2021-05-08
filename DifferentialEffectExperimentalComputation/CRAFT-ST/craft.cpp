/*
Modified version of designer's implementation
*/
// CRAFT Cipher
//#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"
#include <time.h>
#include <string.h>
#include <math.h>
#include <omp.h>
#include <iostream>
using namespace std;
#define Nthreads 16
typedef unsigned long long int UINT64;

//	0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF,
const uint8_t S[16] = {0xc, 0xa, 0xd, 0x3, 0xe, 0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6};
const uint8_t P[16] = {0xF, 0xC, 0xD, 0xE, 0xA, 0x9, 0x8, 0xB, 0x6, 0x5, 0x4, 0x7, 0x1, 0x2, 0x3, 0x0};
const uint8_t Q[16] = {0xC, 0xA, 0xF, 0x5, 0xE, 0x8, 0x9, 0x2, 0xB, 0x3, 0x7, 0x4, 0x6, 0x0, 0x1, 0xD};
const uint8_t RC3[32] = {0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5, 0x6, 0x7, 0x3, 0x1, 0x4, 0x2, 0x5};
const uint8_t RC4[32] = {0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6, 0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8, 0x4, 0x2, 0x9, 0xc, 0x6, 0xb, 0x5, 0xa, 0xd, 0xe, 0xf, 0x7, 0x3, 0x1, 0x8};

void init_prng(int offset) {
	//int initial_seed = 0x5EC7F2B0;
    //int initial_seed = 0x30051991; My birthday!
    unsigned int initial_seed = 10*time(NULL) + 11*offset;
    srand(initial_seed);   // Initialization, should only be called once. int r = rand();
	printf("[+] PRNG initialized to 0x%08X\n", initial_seed);
}

void Initialize(uint8_t TK_enc[][16], uint8_t TK_dec[][16], uint8_t key_0[16], uint8_t key_1[16], uint8_t Tweak[16], int r)
{
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[0][i] = (key_0[i] & 0xf);
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[1][i] = (key_1[i] & 0xf);
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[2][i] = TK_enc[0][i];
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[3][i] = TK_enc[1][i];

    for (uint8_t i = 0; i < 16; i++)
        TK_enc[0][i] ^= (Tweak[i] & 0xf);
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[1][i] ^= (Tweak[i] & 0xf);
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[2][i] ^= (Tweak[Q[i]] & 0xf);
    for (uint8_t i = 0; i < 16; i++)
        TK_enc[3][i] ^= (Tweak[Q[i]] & 0xf);

    for (uint8_t j = 0; j < 4; j++)
        for (uint8_t i = 0; i < 4; i++)
        {
            TK_dec[j][i] = TK_enc[j][i] ^ TK_enc[j][i + 8] ^ TK_enc[j][i + 12];
            TK_dec[j][i + 4] = TK_enc[j][i + 4] ^ TK_enc[j][i + 12];
            TK_dec[j][i + 8] = TK_enc[j][i + 8];
            TK_dec[j][i + 12] = TK_enc[j][i + 12];
        }
}

void RandomSubkeys(uint8_t TK_enc[][16], uint8_t TK_dec[][16])
{
    for (uint8_t r = 0; r < 9; r++)
    {
        for (uint8_t i = 0; i < 16; i++)
        {
            TK_enc[r][i] = rand() & 0xf;
            TK_dec[9 - r - 1][i] = TK_enc[r][i];
        }
        // printf("\nR%02d : ", r);
        // for (uint8_t i = 0; i < 16; i++){
        //     printf("%.1X", TK_enc[r][i]);
        // }
        // printf("\nEnd!\n");
    }
}

void Enc(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t TK_enc[][16])
{
    for (uint8_t i = 0; i < 16; i++)
    {
        ciphertext[i] = plaintext[i] & 0xf;
    }
    for (uint8_t r = 0; r < R; r++)
    {
        //MixColumn
        for (uint8_t i = 0; i < 4; i++)
        {
            ciphertext[i] ^= (ciphertext[i + 8] ^ ciphertext[i + 12]);
            ciphertext[i + 4] ^= ciphertext[i + 12];
        }

        //AddConstant
        ciphertext[4] ^= RC4[r];
        ciphertext[5] ^= RC3[r];

        //AddTweakey
        for (uint8_t i = 0; i < 16; i++)
        {
            //ciphertext[i] ^= TK_enc[r][i];
            ciphertext[i] ^= TK_enc[r % 4][i];
        }
        //Permutation
        uint8_t Temp[16];
        for (uint8_t i = 0; i < 16; i++)
            Temp[P[i]] = ciphertext[i];
        // SBox
        for (uint8_t i = 0; i < 16; i++)
            ciphertext[i] = S[Temp[i]];
        // Next State
        // printf("\nR%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", ciphertext[i]);
    }
}

// void Dec(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t TK_enc[][16]) {
//     for (uint8_t i = 0; i < 16; i++) {
//         plaintext[i] = ciphertext[i] & 0xf;
//     }
//     int ind;
//     for (int r = 0; r < R; r++) {
//         // SBox
//         for (uint8_t i = 0; i < 16; i++)
//             plaintext[i] = S[plaintext[i]];
//         //Permutation
//         uint8_t Temp[16];
//         for (uint8_t i = 0; i < 16; i++)
//             Temp[i] = plaintext[P[i]];
//         //AddTweakey
//         ind = R - r - 1;
//         for (uint8_t i = 0; i < 16; i++){
//                 //plaintext[i] = Temp[i] ^ TK_enc[ind][i];
//                 plaintext[i] = Temp[i] ^ TK_enc[ind % 4][i];

//         }
//         //AddConstant
//         plaintext[4] ^= RC4[ind];
//         plaintext[5] ^= RC3[ind];
//         //MixColumn
//         for (uint8_t i = 0; i < 4; i++) {
//             plaintext[i] ^= (plaintext[i + 8] ^ plaintext[i + 12]);
//             plaintext[i + 4] ^= plaintext[i + 12];
//         }
//         //Next State
//         // printf("\nR%02d : ", r + 1);
//         // for (uint8_t i = 0; i < 16; i++)
//         //     printf("%X", plaintext[i]);
//     }
// }

UINT64 differentialQuery(uint8_t *dp, uint8_t *dc, int r, uint8_t TK_enc[][16], uint8_t TK_dec[][16], int N)
{
    int i, t;
    UINT64 num = 0;
    for (i = 0; i < 16; i++)
        dp[i] = dp[i] & 0xf;
    for (i = 0; i < 16; i++)
        dc[i] = dc[i] & 0xf;
    uint8_t p1[16], p2[16];
    uint8_t c1[16], c2[16];
    bool flag;

    for (t = 0; t < N; t++)
    {
        // randomly choose p1
        for (i = 0; i < 16; i++)
            p1[i] = rand() & 0xf;
        // derive p2
        for (i = 0; i < 16; i++)
            p2[i] = p1[i] ^ dp[i];
        Enc(r, p1, c1, TK_enc);
        Enc(r, p2, c2, TK_enc);
        flag = 1;
        for (i = 0; i < 16; i++)
            if ((c1[i] ^ c2[i]) != dc[i])
                flag = 0;
        if (flag)
        {
            num++;
        }
    }
    return num;
}

UINT64 verify(int R, int N2, int N3)
{
    uint8_t Tweak[16]; // = {0xD, 0xa, 0xA, 0x0, 0xA, 0xA, 0x0, 0xA, 0x6, 0x5, 0xC, 0x0, 0x0, 0x1, 0x1, 0x1}; // Tweak
    uint8_t Key_0[16]; // = {0x1, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA, 0xD, 0xF, 0xC, 0xE, 0xD, 0x7, 0x8, 0xB, 0xD}; // Key 0
    uint8_t Key_1[16]; // = {0xD, 0x9, 0xE, 0x0, 0xE, 0x3, 0x8, 0x1, 0xF, 0xE, 0x6, 0xA, 0x9, 0x4, 0xC, 0x5}; // Key 1
    // uint8_t TK_enc[R][16];
    // uint8_t TK_dec[R][16];
    // RandomSubkeys(TK_enc, TK_dec);
    uint8_t TK_enc[4][16];
    uint8_t TK_dec[4][16];
    for (int i = 0; i < 16; i++)
        Key_0[i] = rand() & 0xf;
    for (int i = 0; i < 16; i++)
        Key_1[i] = rand() & 0xf;

    // //Serial execution
    // FILE* fic;
    // fic=fopen("differentialQuery","w");
    // //0x00A0000000AA00A0
    // uint8_t dp[16] = {0x0, 0xA, 0x0, 0x0, 0xA, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0};
    // //0xA00000000A000000
    // uint8_t dc[16] = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA};
    // double sum = 0;
    // printf("#Queries: 2^(%f)\n", log(Nthreads*N2*N3)/log(2));
    // for(int i = 0; i < Nthreads*N2; i++){
    // 	double num = differentialQuery(dp, dc, R, TK_enc, TK_dec, N2);
    // 	sum += num;
    // }
    // printf("%f\n", sum);
    // sum = double(Nthreads*N2*N3)/sum;
    // printf("%f\n", log(sum)/log(2));
    // fclose(fic);

    //Parallel execution
    UINT64 NUM[Nthreads];
    int counter;
    printf("#Rounds: %d rounds\n", R);
    //printf("#Queries: 2^(%f)\n", log(Nthreads*N2*N3)/log(2));
    printf("#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = %d * %d * %d = 2^(%f)\n", Nthreads, N2, N3, log(Nthreads * N2 * N3) / log(2));
    clock_t clock_timer;
    double wall_timer;
    clock_timer = clock();
    wall_timer = omp_get_wtime();
    omp_set_num_threads(Nthreads);
    #pragma omp parallel for
    for (counter = 0; counter < Nthreads; counter++)
    {
        //uint8_t dp[16] = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0};
        //uint8_t dc[16] = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0};
        // 9 Rounds
        //0x00A0000000AA00A0
        //uint8_t dp[16] = {0x0, 0xA, 0x0, 0x0, 0xA, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0};
        //0xA00000000A000000
        //uint8_t dc[16] = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA};
        //0x0000000A00000000
        //uint8_t dc[16] = {0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0};
		uint8_t dp[16] = { 0x0, 0x0, 0xA, 0xA, 0x0, 0x0, 0xA, 0x0, 0xA, 0x0, 0x0, 0xA, 0x0, 0x0, 0xA, 0x0 };
		//
		uint8_t dc[16] = { 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0 };
		//
        int j;
        UINT64 num = 0;
        int ID = omp_get_thread_num();
        init_prng(ID);
        for (j = 0; j < N2; j++)
        {
            for (int i = 0; i < 16; i++)
                Tweak[i] = rand() & 0xf;
            Initialize(TK_enc, TK_dec, Key_0, Key_1, Tweak, R);
            num += differentialQuery(dp, dc, R, TK_enc, TK_dec, N3);
        }
        NUM[ID] = num;
    }
    cout << " time on clock(): " << (double)(clock() - clock_timer) / CLOCKS_PER_SEC << endl;
    cout << " time on wall: " << omp_get_wtime() - wall_timer << "\n";
    UINT64 sum = 0;
    //double sum_temp = 0;
    for (int i = 0; i < Nthreads; i++)
        sum += NUM[i];
    printf("sum = %llu\n", sum);
    // sum_temp = double(Nthreads*N2*N3)/sum;

    // printf("2^(-%f)\n\n", log(sum_temp)/log(2));
    printf("##########################\n");
    return sum;
}

int main()
{
    // srand(time(NULL)); // Initialization, should only be called once. int r = rand();
    const int n = 2;   //number of indipendent experiments
    int R = 3;         //Number of rounds
    //##########################
    //Nthreads = Number of paralle threads
    int deg = 11;
    int N2 = 1 << deg; //2^(deg) : Number of bunches per threads
    int N3 = 1 << 10;     // Number of queries per bunches
    //##########################
    UINT64 sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += verify(R, N2, N3);
    }
    printf("final sum : %llu\n", sum);
    sum = double(n*Nthreads*N2*N3)/sum;
    printf("\nAverage = 2^(-%f)\n", log(sum)/log(2));
}
