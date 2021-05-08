/*
Modified version of designer's implementation
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
#include <fstream>
using namespace std;
#define Nthreads 8 // Number of parallel threads
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

UINT64 boomerang(uint8_t* dp, uint8_t* dc, uint8_t r, uint8_t tk[][16], int N3)
{
    int i, t;
    UINT64 num = 0;
    for(i = 0; i < 16; i++) dp[i] = dp[i] & 0xf;
    for(i = 0; i < 16; i++) dc[i] = dc[i] & 0xf;
	uint8_t p1[16],p2[16];
    uint8_t p3[16],p4[16];
    uint8_t c1[16],c2[16];
	uint8_t c3[16],c4[16];	
	bool flag;

	for (t = 0; t < N3; t++){
		// randomly choose p1
		for(i = 0; i < 16; i++) p1[i] = rand() & 0xf;
		// derive p2
		for(i = 0; i < 16; i++) p2[i] = p1[i]^dp[i];
        enc(r, p1, c1, tk);
        //enc_with_random_tweakies(r, p1, c1, rnd_tk);
        enc(r, p2, c2, tk);		
        //enc_with_random_tweakies(r, p2, c2, rnd_tk);		
        
		// derive c3
		for(i = 0; i < 16; i++) c3[i] = c1[i]^dc[i];
		// derive c4
		for(i = 0; i < 16; i++) c4[i] = c2[i]^dc[i];
        dec(r, p3, c3, tk);
        //dec_with_random_tweakies(r, p3, c3, rnd_tk);
        dec(r, p4, c4, tk);
        //dec_with_random_tweakies(r, p4, c4, rnd_tk);
		flag = 1;
		for(i = 0; i < 16; i++)
			if ((p3[i]^p4[i]) != dp[i])
				flag = 0;
		if (flag) {num ++;}
	}
	return num;
}


double verify(uint8_t dp[16], uint8_t dc[16], uint8_t R, int N1, int N2, int N3) {
    uint8_t key0[16];// = {0x1, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA, 0xD, 0xF, 0xC, 0xE, 0xD, 0x7, 0x8, 0xB, 0xD}; // Key 0
    uint8_t key1[16];// = {0xD, 0x9, 0xE, 0x0, 0xE, 0x3, 0x8, 0x1, 0xF, 0xE, 0x6, 0xA, 0x9, 0x4, 0xC, 0x5}; // Key 1
    for(int i = 0; i < 16; i++) key0[i] = rand() & 0xf;
    for(int i = 0; i < 16; i++) key1[i] = rand() & 0xf;
    UINT64 *NUM;
    NUM = (UINT64 *)malloc(N1 * sizeof(UINT64));
	int counter;
    printf("#Rounds: %d rounds\n", R);
    printf("#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = %d * %d * %d = 2^(%f)\n", N1, N2, N3, log(N1 * N2 * N3) / log(2));
    clock_t clock_timer;
    double wall_timer;
	clock_timer = clock();
	wall_timer = omp_get_wtime();
	omp_set_num_threads(N1);
	#pragma omp parallel for
	for(counter = 0; counter < N1; counter++){
		UINT64 num = 0;
        uint8_t master_tweak[16];// = {0xD, 0xa, 0xA, 0x0, 0xA, 0xA, 0x0, 0xA, 0x6, 0x5, 0xC, 0x0, 0x0, 0x1, 0x1, 0x1}; // master_tweak
        uint8_t tk[4][16];
		for(int j = 0; j < N2; j++){
            for(int i = 0; i < 16; i++) master_tweak[i] = rand() & 0xf;
            initialize(key0, key1, master_tweak, tk);
			num += boomerang(dp, dc, R, tk, N3);
        }
		int ID = omp_get_thread_num();
		NUM[ID] = num;
	}
    cout << " time on clock(): " << ((double)clock() - clock_timer) / CLOCKS_PER_SEC<<endl;
    cout << " time on wall: " <<  omp_get_wtime() - wall_timer << "\n";		
	UINT64 sum = 0;
	for(int i = 0; i < N1; i++)
		sum += NUM[i];
	free(NUM);
	printf("sum = %llu\n", sum);
	double sum_temp;
    sum_temp = double(N1)*double(N2)*double(N3)/sum;
	
	printf("2^(-%f)\n", log(sum_temp)/log(2));
    printf("#####################################\n");
    return sum;
}

//####################################################################################################################################################################
//####################################################################################################################################################################
//#########################################################################Random Part################################################################################

void enc_with_random_tweakies(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t *rnd_tk) {
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
            ciphertext[i] ^= rnd_tk[16*r + i];
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
        //Next State
        // printf("\nR%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", ciphertext[i]);
        // printf("\ntk%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", rnd_tk[r*16 + i]);
    }
}

void dec_with_random_tweakies(uint8_t R, uint8_t plaintext[16], uint8_t ciphertext[16], uint8_t *rnd_tk) {    
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
            plaintext[i] = Temp[i] ^ rnd_tk[ind*16 + i];
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
        // printf("\ntk%02d : ", r + 1);
        // for (uint8_t i = 0; i < 16; i++)
        //     printf("%X", rnd_tk[ind*16 + i]); 
    }
}

int boomerang_random_subtks(uint8_t* dp, uint8_t* dc, uint8_t *rnd_tk, uint8_t r, int N3)
{
    int i, t, num = 0;
    for(i = 0; i < 16; i++) dp[i] = dp[i] & 0xf;
    for(i = 0; i < 16; i++) dc[i] = dc[i] & 0xf;
	uint8_t p1[16],p2[16];
    uint8_t p3[16],p4[16];
    uint8_t c1[16],c2[16];
	uint8_t c3[16],c4[16];
	bool flag;
	for(t = 0; t < N3; t++){
		// randomly choose p1
		for(i = 0; i < 16; i++) p1[i] = rand() & 0xf;
		// derive p2
		for(i = 0; i < 16; i++) p2[i] = p1[i]^dp[i];
        enc_with_random_tweakies(r, p1, c1, rnd_tk);
        enc_with_random_tweakies(r, p2, c2, rnd_tk);
		// derive c3
		for(i = 0; i < 16; i++) c3[i] = c1[i]^dc[i];
		// derive c4
		for(i = 0; i < 16; i++) c4[i] = c2[i]^dc[i];
        dec_with_random_tweakies(r, p3, c3, rnd_tk);
        dec_with_random_tweakies(r, p4, c4, rnd_tk);
		flag = 1;
		for(i = 0; i < 16; i++)
			if ((p3[i]^p4[i]) != dp[i])
				flag = 0;
		if (flag) {num ++;}
	}
	return num;
}

double verify_random_subtks(uint8_t dp[16], uint8_t dc[16], uint8_t R, int N1, int N2, int N3) {
    int *NUM;
    NUM = (int *)malloc(N1 * sizeof(int));
	int counter;
    printf("#Rounds: %d rounds\n", R);
    printf("#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = %d * %d * %d = 2^(%f)\n", N1, N2, N3, log(N1 * N2 * N3) / log(2));
    clock_t clock_timer;
    double wall_timer;
	clock_timer = clock();
	wall_timer = omp_get_wtime();
	omp_set_num_threads(N1);
	#pragma omp parallel for
	for(counter = 0; counter < N1; counter++){
		int num = 0;
        uint8_t *rnd_tk;
        rnd_tk = (uint8_t *)malloc(R*16*sizeof(uint8_t));
		for(int j = 0; j < N2; j++){
            for(int nr = 0; nr < R; nr++){
                for(int nn = 0; nn < 16; nn++){
                    rnd_tk[nr*16 + nn] = rand() & 0xf;
                }
            }
			num += boomerang_random_subtks(dp, dc, rnd_tk, R, N3);
        }
		int ID = omp_get_thread_num();
		NUM[ID] = num;
        free(rnd_tk);
	}
    cout << " time on clock(): " << (double) (clock() - clock_timer) / CLOCKS_PER_SEC<<endl;
    cout << " time on wall: " <<  omp_get_wtime() - wall_timer << "\n";		
	double sum = 0;
	for(int i = 0; i < N1; i++)
		sum += NUM[i];
	free(NUM);
	printf("sum = %f\n", sum);
	
	printf("2^(-%f)\n", (log(N1) + log(N2) + log(N3) - log(sum))/log(2));
    printf("#####################################\n");
    return sum;
}

//####################################################################################################################################################################
//####################################################################################################################################################################
//#################################################################The end of random part#############################################################################

int check_correctness(uint8_t r) {
    uint8_t key0[16];// = {0x1, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA, 0xD, 0xF, 0xC, 0xE, 0xD, 0x7, 0x8, 0xB, 0xD}; // Key 0
    uint8_t key1[16];// = {0xD, 0x9, 0xE, 0x0, 0xE, 0x3, 0x8, 0x1, 0xF, 0xE, 0x6, 0xA, 0x9, 0x4, 0xC, 0x5}; // Key 1    
    for(int i = 0; i < 16; i++) key0[i] = rand() & 0xf;
    for(int i = 0; i < 16; i++) key1[i] = rand() & 0xf;
    uint8_t p[16];
    uint8_t c[16];
    for(int i = 0; i < 16; i++) p[i] = rand() & 0xf;
    uint8_t master_tweak[16];
    for(int i = 0; i < 16; i++) master_tweak[i] = rand() & 0xf;
    uint8_t tk[4][16];
    initialize(key0, key1, master_tweak, tk);
    printf("#Rounds: %d rounds\n", r);
    printf("%s\n", "Encryption:");
    enc(r, p, c, tk);
    printf("%27s: ", "plaintext before encryption");
    print_state(p);
    printf("%27s: ", "ciphertext after encryption");
    print_state(c);
    printf("%s\n", "Decryption:");
    dec(r, p, c, tk);
    printf("%27s: ", "plaintext after decryption");
    print_state(p);
    printf("\n");
    return 0;
}

void init_prng() {
	//int initial_seed = 0x5EC7F2B0;
    //int initial_seed = 0x30051991; // My birthday's date :)
    unsigned int initial_seed = time(NULL);
    srand(initial_seed);   // Initialization, should only be called once. int r = rand();
	printf("[+] PRNG initialized to 0x%08X\n", initial_seed);
}

int main() {
    init_prng();
    //#################################################################################
    bool random_subtks = false;
    const int n = 100;        //Number of repetitions
    uint8_t R = 7;          //Number of rounds
    int deg1 = 12;
    int deg2 = 12;
    int N1 = Nthreads;
	int N2 = 1 << deg1;     // 2^(deg1): Number of bunches per thread
	int N3 = 1 << deg2;     // 2^(deg2): Number of queries per bunch
    string dp_str = "0000000050000000";
    string dc_str = "0000500000000000";
    //#################################################################################
    uint8_t dp[16];
    uint8_t dc[16];
    convert_hexstr_to_statearray(dp_str, dp, false);
    convert_hexstr_to_statearray(dc_str, dc, false);
    check_correctness(R);
    char pr_matrix_9r[15][15][20];

    for(uint8_t k1 = 1; k1 < 16; k1++){
        for(uint8_t k2 = 1; k2 < 16; k2++){
            dp[8] = k1;
            dc[4] = k2;
            UINT64 sum = 0;
            for(int i = 0; i < n; i++) {
                if (random_subtks == true){
                    sum += verify_random_subtks(dp, dc, R, N1, N2, N3);
                }
                else{
                    sum += verify(dp, dc, R, N1, N2, N3);
                }
            }
            sprintf(pr_matrix_9r[k1 - 1][k2 - 1], "2^-%0.2f", (log(n) + log(N1) + log(N2) + log(N3) - log(sum))/log(2));
            printf("(k1, k2) = (%d, %d), Average : 2^-%0.2f\n\n", k1, k2, (log(n) + log(N1) + log(N2) + log(N3) - log(sum))/log(2));
        }
    }

    printf("Saving a latex format of generated matrix in R7re.txt ...\n");
    ofstream fileobj;    
    fileobj.open("R7reNew14r.txt");
    for (int t1 = 0; t1 < 15; t1++){        
        for (int t2 = 0; t2 < 15; t2++) {            
            if (t2 == 14) {
                fileobj << pr_matrix_9r[t1][t2];
                fileobj << "\\\\\n";
            }
            else {
                fileobj << pr_matrix_9r[t1][t2] << " & ";
            }
        }
    }
    fileobj.close();

    printf("Saving a Sage format of generated matrix in R7reSage.txt ...\n");
    fileobj.open("R7reSageNew14r.txt");
    for (int t1 = 0; t1 < 15; t1++){    
        fileobj << "[";
        for (int t2 = 0; t2 < 15; t2++) {            
            if (t2 == 14) {
                fileobj << pr_matrix_9r[t1][t2];
            }
            else {
                fileobj << pr_matrix_9r[t1][t2] << ", ";
            }
        }
        if(t1 == 14)
            fileobj << "]]";
        else
            fileobj << "], ";
    }
    fileobj.close();
    return 0;
}
