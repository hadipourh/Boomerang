In this test, we choose a single tweakey at random and perform 2^30 boomerang queries with the fixed tweakey. Next, we repeat this experiment 100 times with 100 different random tweakey and compute the average.

Results:

```sh
Experiment Number 0:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4538B72
[+] PRNG initialized to 0xC4538B93
[+] PRNG initialized to 0xC4538B88
[+] PRNG initialized to 0xC4538B7D
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4995.2902
time on wall: 1262.9535
sum = 11.000000
2^(-26.540568)

##########################
Experiment Number 1:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC453BCC8
[+] PRNG initialized to 0xC453BCDE
[+] PRNG initialized to 0xC453BCE9
[+] PRNG initialized to 0xC453BCD3
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4822.1016
time on wall: 1208.2221
sum = 6.000000
2^(-27.415037)

##########################
Experiment Number 2:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC453EBF8
[+] PRNG initialized to 0xC453EC19
[+] PRNG initialized to 0xC453EC0E
[+] PRNG initialized to 0xC453EC03
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4799.0469
time on wall: 1200.7034
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 3:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4541AED
[+] PRNG initialized to 0xC4541B03
[+] PRNG initialized to 0xC4541AE2
[+] PRNG initialized to 0xC4541AF8
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4797.6081
time on wall: 1200.3758
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 4:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45449C2
[+] PRNG initialized to 0xC45449E3
[+] PRNG initialized to 0xC45449D8
[+] PRNG initialized to 0xC45449CD
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4783.6630
time on wall: 1196.6662
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 5:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45478A5
[+] PRNG initialized to 0xC454788F
[+] PRNG initialized to 0xC454789A
[+] PRNG initialized to 0xC4547884
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4786.7745
time on wall: 1197.4317
sum = 21.000000
2^(-25.607683)

##########################
Experiment Number 6:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC454A746
[+] PRNG initialized to 0xC454A75C
[+] PRNG initialized to 0xC454A767
[+] PRNG initialized to 0xC454A751
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4789.3599
time on wall: 1197.9325
sum = 32.000000
2^(-25.000000)

##########################
Experiment Number 7:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC454D612
[+] PRNG initialized to 0xC454D628
[+] PRNG initialized to 0xC454D61D
[+] PRNG initialized to 0xC454D633
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4788.7687
time on wall: 1197.8594
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 8:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45504FF
[+] PRNG initialized to 0xC45504E9
[+] PRNG initialized to 0xC45504DE
[+] PRNG initialized to 0xC45504F4
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4792.2017
time on wall: 1198.8080
sum = 36.000000
2^(-24.830075)

##########################
Experiment Number 9:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45533CA
[+] PRNG initialized to 0xC45533D5
[+] PRNG initialized to 0xC45533B4
[+] PRNG initialized to 0xC45533BF
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4787.8301
time on wall: 1197.6346
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 10:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4556276
[+] PRNG initialized to 0xC4556281
[+] PRNG initialized to 0xC455628C
[+] PRNG initialized to 0xC4556297
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4785.7159
time on wall: 1196.9960
sum = 30.000000
2^(-25.093109)

##########################
Experiment Number 11:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4559138
[+] PRNG initialized to 0xC455914E
[+] PRNG initialized to 0xC4559159
[+] PRNG initialized to 0xC4559143
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4778.8725
time on wall: 1195.3505
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 12:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC455C006
[+] PRNG initialized to 0xC455C011
[+] PRNG initialized to 0xC455BFF0
[+] PRNG initialized to 0xC455BFFB
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4784.9569
time on wall: 1197.2824
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 13:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC455EEB2
[+] PRNG initialized to 0xC455EEC8
[+] PRNG initialized to 0xC455EED3
[+] PRNG initialized to 0xC455EEBD
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4783.4446
time on wall: 1197.6764
sum = 11.000000
2^(-26.540568)

##########################
Experiment Number 14:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4561D7E
[+] PRNG initialized to 0xC4561D9F
[+] PRNG initialized to 0xC4561D94
[+] PRNG initialized to 0xC4561D89
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4783.3074
time on wall: 1196.4564
sum = 25.000000
2^(-25.356144)

##########################
Experiment Number 15:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4564C41
[+] PRNG initialized to 0xC4564C57
[+] PRNG initialized to 0xC4564C4C
[+] PRNG initialized to 0xC4564C36
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4786.0040
time on wall: 1197.4628
sum = 14.000000
2^(-26.192645)

##########################
Experiment Number 16:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4567B02
[+] PRNG initialized to 0xC4567B0D
[+] PRNG initialized to 0xC4567B23
[+] PRNG initialized to 0xC4567B18
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4779.6569
time on wall: 1195.7843
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 17:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC456A9D1
[+] PRNG initialized to 0xC456A9BB
[+] PRNG initialized to 0xC456A9B0
[+] PRNG initialized to 0xC456A9C6
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4785.6040
time on wall: 1197.4005
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 18:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC456D892
[+] PRNG initialized to 0xC456D87C
[+] PRNG initialized to 0xC456D887
[+] PRNG initialized to 0xC456D89D
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4782.7929
time on wall: 1196.2740
sum = 20.000000
2^(-25.678072)

##########################
Experiment Number 19:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC457073F
[+] PRNG initialized to 0xC4570755
[+] PRNG initialized to 0xC4570734
[+] PRNG initialized to 0xC457074A
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4780.2886
time on wall: 1195.7596
sum = 18.000000
2^(-25.830075)

##########################
Experiment Number 20:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45735F7
[+] PRNG initialized to 0xC4573602
[+] PRNG initialized to 0xC45735EC
[+] PRNG initialized to 0xC457360D
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4784.7683
time on wall: 1196.9273
sum = 6.000000
2^(-27.415037)

##########################
Experiment Number 21:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45764CF
[+] PRNG initialized to 0xC45764B9
[+] PRNG initialized to 0xC45764C4
[+] PRNG initialized to 0xC45764AE
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4782.9046
time on wall: 1196.5162
sum = 34.000000
2^(-24.912537)

##########################
Experiment Number 22:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4579366
[+] PRNG initialized to 0xC457937C
[+] PRNG initialized to 0xC4579387
[+] PRNG initialized to 0xC4579371
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4785.5213
time on wall: 1197.1230
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 23:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC457C233
[+] PRNG initialized to 0xC457C23E
[+] PRNG initialized to 0xC457C249
[+] PRNG initialized to 0xC457C228
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4781.2445
time on wall: 1196.1796
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 24:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC457F0EA
[+] PRNG initialized to 0xC457F10B
[+] PRNG initialized to 0xC457F100
[+] PRNG initialized to 0xC457F0F5
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4786.6033
time on wall: 1197.4987
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 25:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4581FAC
[+] PRNG initialized to 0xC4581FB7
[+] PRNG initialized to 0xC4581FCD
[+] PRNG initialized to 0xC4581FC2
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4776.8258
time on wall: 1194.7577
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 26:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4584E7B
[+] PRNG initialized to 0xC4584E5A
[+] PRNG initialized to 0xC4584E70
[+] PRNG initialized to 0xC4584E65
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4781.7073
time on wall: 1196.0375
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 27:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4587D33
[+] PRNG initialized to 0xC4587D1D
[+] PRNG initialized to 0xC4587D12
[+] PRNG initialized to 0xC4587D28
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4779.6394
time on wall: 1195.7498
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 28:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC458ABCA
[+] PRNG initialized to 0xC458ABE0
[+] PRNG initialized to 0xC458ABEB
[+] PRNG initialized to 0xC458ABD5
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4785.4025
time on wall: 1197.0878
sum = 6.000000
2^(-27.415037)

##########################
Experiment Number 29:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC458DA8C
[+] PRNG initialized to 0xC458DA97
[+] PRNG initialized to 0xC458DAAD
[+] PRNG initialized to 0xC458DAA2
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4782.9156
time on wall: 1196.5006
sum = 12.000000
2^(-26.415037)

##########################
Experiment Number 30:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC459095A
[+] PRNG initialized to 0xC459094F
[+] PRNG initialized to 0xC4590965
[+] PRNG initialized to 0xC4590944
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4779.0645
time on wall: 1195.5314
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 31:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC459381D
[+] PRNG initialized to 0xC45937FC
[+] PRNG initialized to 0xC4593812
[+] PRNG initialized to 0xC4593807
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4785.9240
time on wall: 1197.3541
sum = 2.000000
2^(-29.000000)

##########################
Experiment Number 32:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45966C9
[+] PRNG initialized to 0xC45966D4
[+] PRNG initialized to 0xC45966DF
[+] PRNG initialized to 0xC45966BE
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4776.3151
time on wall: 1194.7043
sum = 12.000000
2^(-26.415037)

##########################
Experiment Number 33:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC459956C
[+] PRNG initialized to 0xC459958D
[+] PRNG initialized to 0xC4599577
[+] PRNG initialized to 0xC4599582
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4776.3072
time on wall: 1194.6193
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 34:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC459C426
[+] PRNG initialized to 0xC459C431
[+] PRNG initialized to 0xC459C410
[+] PRNG initialized to 0xC459C41B
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4786.9397
time on wall: 1197.6313
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 35:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC459F2DC
[+] PRNG initialized to 0xC459F2FD
[+] PRNG initialized to 0xC459F2F2
[+] PRNG initialized to 0xC459F2E7
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4787.3196
time on wall: 1197.7247
sum = 30.000000
2^(-25.093109)

##########################
Experiment Number 36:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45A21A8
[+] PRNG initialized to 0xC45A21C9
[+] PRNG initialized to 0xC45A21BE
[+] PRNG initialized to 0xC45A21B3
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4776.7868
time on wall: 1194.9605
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 37:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45A5056
[+] PRNG initialized to 0xC45A5061
[+] PRNG initialized to 0xC45A506C
[+] PRNG initialized to 0xC45A5077
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4783.4636
time on wall: 1196.4752
sum = 22.000000
2^(-25.540568)

##########################
Experiment Number 38:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45A7F19
[+] PRNG initialized to 0xC45A7F2F
[+] PRNG initialized to 0xC45A7F24
[+] PRNG initialized to 0xC45A7F0E
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4781.1672
time on wall: 1195.8852
sum = 7.000000
2^(-27.192645)

##########################
Experiment Number 39:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45AADDC
[+] PRNG initialized to 0xC45AADE7
[+] PRNG initialized to 0xC45AADC6
[+] PRNG initialized to 0xC45AADD1
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4783.7867
time on wall: 1196.8885
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 40:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45ADC9E
[+] PRNG initialized to 0xC45ADC93
[+] PRNG initialized to 0xC45ADCA9
[+] PRNG initialized to 0xC45ADC88
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4796.1180
time on wall: 1200.5381
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 41:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45B0B72
[+] PRNG initialized to 0xC45B0B93
[+] PRNG initialized to 0xC45B0B88
[+] PRNG initialized to 0xC45B0B7D
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4785.2359
time on wall: 1197.3293
sum = 2.000000
2^(-29.000000)

##########################
Experiment Number 42:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45B3A4A
[+] PRNG initialized to 0xC45B3A34
[+] PRNG initialized to 0xC45B3A3F
[+] PRNG initialized to 0xC45B3A55
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4789.0071
time on wall: 1197.9373
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 43:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45B6916
[+] PRNG initialized to 0xC45B6921
[+] PRNG initialized to 0xC45B690B
[+] PRNG initialized to 0xC45B6900
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4786.0307
time on wall: 1197.0383
sum = 2.000000
2^(-29.000000)

##########################
Experiment Number 44:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45B97E3
[+] PRNG initialized to 0xC45B97C2
[+] PRNG initialized to 0xC45B97CD
[+] PRNG initialized to 0xC45B97D8
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4789.6070
time on wall: 1197.8800
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 45:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45BC6AF
[+] PRNG initialized to 0xC45BC68E
[+] PRNG initialized to 0xC45BC6A4
[+] PRNG initialized to 0xC45BC699
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4796.4405
time on wall: 1199.8243
sum = 14.000000
2^(-26.192645)

##########################
Experiment Number 46:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45BF58F
[+] PRNG initialized to 0xC45BF579
[+] PRNG initialized to 0xC45BF584
[+] PRNG initialized to 0xC45BF56E
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4799.4933
time on wall: 1201.1527
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 47:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45C246E
[+] PRNG initialized to 0xC45C2463
[+] PRNG initialized to 0xC45C2458
[+] PRNG initialized to 0xC45C2479
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4796.6742
time on wall: 1199.9625
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 48:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45C5359
[+] PRNG initialized to 0xC45C5343
[+] PRNG initialized to 0xC45C534E
[+] PRNG initialized to 0xC45C5338
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4778.4191
time on wall: 1195.2480
sum = 23.000000
2^(-25.476438)

##########################
Experiment Number 49:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45C81FC
[+] PRNG initialized to 0xC45C8207
[+] PRNG initialized to 0xC45C81E6
[+] PRNG initialized to 0xC45C81F1
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4777.1100
time on wall: 1195.1777
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 50:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45CB094
[+] PRNG initialized to 0xC45CB0AA
[+] PRNG initialized to 0xC45CB0B5
[+] PRNG initialized to 0xC45CB09F
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4778.0544
time on wall: 1195.3376
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 51:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45CDF63
[+] PRNG initialized to 0xC45CDF4D
[+] PRNG initialized to 0xC45CDF58
[+] PRNG initialized to 0xC45CDF42
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4776.0297
time on wall: 1194.8479
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 52:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45D0DF0
[+] PRNG initialized to 0xC45D0E06
[+] PRNG initialized to 0xC45D0DFB
[+] PRNG initialized to 0xC45D0E11
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4780.8009
time on wall: 1195.8979
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 53:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45D3CC9
[+] PRNG initialized to 0xC45D3CB3
[+] PRNG initialized to 0xC45D3CA8
[+] PRNG initialized to 0xC45D3CBE
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4780.0801
time on wall: 1195.6144
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 54:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45D6B6B
[+] PRNG initialized to 0xC45D6B76
[+] PRNG initialized to 0xC45D6B60
[+] PRNG initialized to 0xC45D6B81
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4780.3327
time on wall: 1195.7750
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 55:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45D9A23
[+] PRNG initialized to 0xC45D9A18
[+] PRNG initialized to 0xC45D9A2E
[+] PRNG initialized to 0xC45D9A39
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4778.3505
time on wall: 1195.2736
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 56:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45DC8C6
[+] PRNG initialized to 0xC45DC8DC
[+] PRNG initialized to 0xC45DC8D1
[+] PRNG initialized to 0xC45DC8E7
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4777.1832
time on wall: 1194.9090
sum = 2.000000
2^(-29.000000)

##########################
Experiment Number 57:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45DF774
[+] PRNG initialized to 0xC45DF78A
[+] PRNG initialized to 0xC45DF77F
[+] PRNG initialized to 0xC45DF795
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4785.4635
time on wall: 1196.9431
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 58:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45E2641
[+] PRNG initialized to 0xC45E2636
[+] PRNG initialized to 0xC45E2657
[+] PRNG initialized to 0xC45E264C
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4776.7034
time on wall: 1194.8342
sum = 27.000000
2^(-25.245112)

##########################
Experiment Number 59:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45E54FA
[+] PRNG initialized to 0xC45E5505
[+] PRNG initialized to 0xC45E54E4
[+] PRNG initialized to 0xC45E54EF
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4779.3811
time on wall: 1195.4184
sum = 13.000000
2^(-26.299560)

##########################
Experiment Number 60:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45E83A8
[+] PRNG initialized to 0xC45E839D
[+] PRNG initialized to 0xC45E83B3
[+] PRNG initialized to 0xC45E8392
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4782.9001
time on wall: 1196.8074
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 61:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45EB254
[+] PRNG initialized to 0xC45EB275
[+] PRNG initialized to 0xC45EB25F
[+] PRNG initialized to 0xC45EB26A
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4782.3950
time on wall: 1196.2179
sum = 38.000000
2^(-24.752072)

##########################
Experiment Number 62:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45EE10C
[+] PRNG initialized to 0xC45EE117
[+] PRNG initialized to 0xC45EE12D
[+] PRNG initialized to 0xC45EE122
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4766.0753
time on wall: 1192.0285
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 63:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45F0F9C
[+] PRNG initialized to 0xC45F0FBD
[+] PRNG initialized to 0xC45F0FB2
[+] PRNG initialized to 0xC45F0FA7
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4784.6376
time on wall: 1197.0633
sum = 15.000000
2^(-26.093109)

##########################
Experiment Number 64:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45F3E5E
[+] PRNG initialized to 0xC45F3E74
[+] PRNG initialized to 0xC45F3E7F
[+] PRNG initialized to 0xC45F3E69
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4785.7896
time on wall: 1197.2284
sum = 14.000000
2^(-26.192645)

##########################
Experiment Number 65:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45F6D41
[+] PRNG initialized to 0xC45F6D36
[+] PRNG initialized to 0xC45F6D20
[+] PRNG initialized to 0xC45F6D2B
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4783.5637
time on wall: 1197.0638
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 66:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45F9BE2
[+] PRNG initialized to 0xC45F9BF8
[+] PRNG initialized to 0xC45F9BED
[+] PRNG initialized to 0xC45F9C03
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4780.1890
time on wall: 1196.0343
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 67:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45FCA9A
[+] PRNG initialized to 0xC45FCAA5
[+] PRNG initialized to 0xC45FCABB
[+] PRNG initialized to 0xC45FCAB0
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4781.5898
time on wall: 1196.0733
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 68:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC45FF952
[+] PRNG initialized to 0xC45FF968
[+] PRNG initialized to 0xC45FF973
[+] PRNG initialized to 0xC45FF95D
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4783.4145
time on wall: 1196.6464
sum = 21.000000
2^(-25.607683)

##########################
Experiment Number 69:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4602835
[+] PRNG initialized to 0xC460282A
[+] PRNG initialized to 0xC4602814
[+] PRNG initialized to 0xC460281F
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4782.5897
time on wall: 1196.4096
sum = 23.000000
2^(-25.476438)

##########################
Experiment Number 70:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46056E1
[+] PRNG initialized to 0xC46056EC
[+] PRNG initialized to 0xC46056D6
[+] PRNG initialized to 0xC46056F7
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4788.8253
time on wall: 1197.9586
sum = 9.000000
2^(-26.830075)

##########################
Experiment Number 71:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46085A2
[+] PRNG initialized to 0xC46085C3
[+] PRNG initialized to 0xC46085B8
[+] PRNG initialized to 0xC46085AD
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4783.6249
time on wall: 1196.6559
sum = 28.000000
2^(-25.192645)

##########################
Experiment Number 72:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC460B47B
[+] PRNG initialized to 0xC460B45A
[+] PRNG initialized to 0xC460B465
[+] PRNG initialized to 0xC460B470
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4777.8896
time on wall: 1195.0841
sum = 6.000000
2^(-27.415037)

##########################
Experiment Number 73:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC460E31E
[+] PRNG initialized to 0xC460E313
[+] PRNG initialized to 0xC460E329
[+] PRNG initialized to 0xC460E308
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4785.5642
time on wall: 1197.1449
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 74:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46111EB
[+] PRNG initialized to 0xC46111E0
[+] PRNG initialized to 0xC46111CA
[+] PRNG initialized to 0xC46111D5
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4787.1653
time on wall: 1197.3601
sum = 26.000000
2^(-25.299560)

##########################
Experiment Number 75:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46140B7
[+] PRNG initialized to 0xC46140A1
[+] PRNG initialized to 0xC4614096
[+] PRNG initialized to 0xC46140AC
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4822.8557
time on wall: 1207.4259
sum = 12.000000
2^(-26.415037)

##########################
Experiment Number 76:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4616FDD
[+] PRNG initialized to 0xC4616FC7
[+] PRNG initialized to 0xC4616FBC
[+] PRNG initialized to 0xC4616FD2
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4811.7394
time on wall: 1205.0861
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 77:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4619ED9
[+] PRNG initialized to 0xC4619ECE
[+] PRNG initialized to 0xC4619EE4
[+] PRNG initialized to 0xC4619EEF
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4783.5335
time on wall: 1196.7210
sum = 4.000000
2^(-28.000000)

##########################
Experiment Number 78:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC461CD90
[+] PRNG initialized to 0xC461CDB1
[+] PRNG initialized to 0xC461CD9B
[+] PRNG initialized to 0xC461CDA6
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4780.2179
time on wall: 1195.6208
sum = 7.000000
2^(-27.192645)

##########################
Experiment Number 79:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC461FC48
[+] PRNG initialized to 0xC461FC5E
[+] PRNG initialized to 0xC461FC69
[+] PRNG initialized to 0xC461FC53
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4782.8578
time on wall: 1196.2970
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 80:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4622B21
[+] PRNG initialized to 0xC4622B00
[+] PRNG initialized to 0xC4622B0B
[+] PRNG initialized to 0xC4622B16
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4785.6398
time on wall: 1196.9796
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 81:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46259CD
[+] PRNG initialized to 0xC46259C2
[+] PRNG initialized to 0xC46259E3
[+] PRNG initialized to 0xC46259D8
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4788.5147
time on wall: 1198.1013
sum = 16.000000
2^(-26.000000)

##########################
Experiment Number 82:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46288AF
[+] PRNG initialized to 0xC4628899
[+] PRNG initialized to 0xC46288A4
[+] PRNG initialized to 0xC462888E
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4781.8339
time on wall: 1196.2026
sum = 23.000000
2^(-25.476438)

##########################
Experiment Number 83:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC462B767
[+] PRNG initialized to 0xC462B75C
[+] PRNG initialized to 0xC462B751
[+] PRNG initialized to 0xC462B746
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4779.1843
time on wall: 1195.5829
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 84:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC462E61F
[+] PRNG initialized to 0xC462E609
[+] PRNG initialized to 0xC462E614
[+] PRNG initialized to 0xC462E5FE
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4782.0048
time on wall: 1196.3179
sum = 18.000000
2^(-25.830075)

##########################
Experiment Number 85:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46314B6
[+] PRNG initialized to 0xC46314CC
[+] PRNG initialized to 0xC46314C1
[+] PRNG initialized to 0xC46314D7
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4783.2257
time on wall: 1196.5107
sum = 5.000000
2^(-27.678072)

##########################
Experiment Number 86:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC463438E
[+] PRNG initialized to 0xC4634378
[+] PRNG initialized to 0xC4634399
[+] PRNG initialized to 0xC4634383
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4781.3741
time on wall: 1196.4261
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 87:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4637230
[+] PRNG initialized to 0xC463723B
[+] PRNG initialized to 0xC4637246
[+] PRNG initialized to 0xC4637251
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4932.5378
time on wall: 1245.9873
sum = 6.000000
2^(-27.415037)

##########################
Experiment Number 88:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC463A2FD
[+] PRNG initialized to 0xC463A2DC
[+] PRNG initialized to 0xC463A2E7
[+] PRNG initialized to 0xC463A2F2
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4994.6844
time on wall: 1264.6502
sum = 2.000000
2^(-29.000000)

##########################
Experiment Number 89:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC463D451
[+] PRNG initialized to 0xC463D467
[+] PRNG initialized to 0xC463D45C
[+] PRNG initialized to 0xC463D446
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4995.0589
time on wall: 1261.6926
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 90:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4640588
[+] PRNG initialized to 0xC4640593
[+] PRNG initialized to 0xC46405A9
[+] PRNG initialized to 0xC464059E
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4995.1018
time on wall: 1261.8185
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 91:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46436EA
[+] PRNG initialized to 0xC46436F5
[+] PRNG initialized to 0xC46436D4
[+] PRNG initialized to 0xC46436DF
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4915.6366
time on wall: 1247.0484
sum = 10.000000
2^(-26.678072)

##########################
Experiment Number 92:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46467AB
[+] PRNG initialized to 0xC4646795
[+] PRNG initialized to 0xC46467A0
[+] PRNG initialized to 0xC464678A
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4922.9657
time on wall: 1240.2186
sum = 22.000000
2^(-25.540568)

##########################
Experiment Number 93:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC464981B
[+] PRNG initialized to 0xC4649810
[+] PRNG initialized to 0xC4649805
[+] PRNG initialized to 0xC46497FA
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4993.2792
time on wall: 1269.5724
sum = 11.000000
2^(-26.540568)

##########################
Experiment Number 94:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC464C9A1
[+] PRNG initialized to 0xC464C9AC
[+] PRNG initialized to 0xC464C9B7
[+] PRNG initialized to 0xC464C996
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4908.4166
time on wall: 1247.5515
sum = 8.000000
2^(-27.000000)

##########################
Experiment Number 95:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC464FA56
[+] PRNG initialized to 0xC464FA6C
[+] PRNG initialized to 0xC464FA77
[+] PRNG initialized to 0xC464FA61
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4783.3673
time on wall: 1196.3967
sum = 20.000000
2^(-25.678072)

##########################
Experiment Number 96:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC465292F
[+] PRNG initialized to 0xC4652919
[+] PRNG initialized to 0xC4652924
[+] PRNG initialized to 0xC465290E
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
time on clock: 4771.3805
time on wall: 1193.6228
sum = 13.000000
2^(-26.299560)

##########################
Experiment Number 97:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC46557C8
[+] PRNG initialized to 0xC46557BD
[+] PRNG initialized to 0xC46557B2
[+] PRNG initialized to 0xC46557D3
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
time on clock: 4790.5339
time on wall: 1198.5763
sum = 1.000000
2^(-30.000000)

##########################
Experiment Number 98:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC4658689
[+] PRNG initialized to 0xC465867E
[+] PRNG initialized to 0xC465869F
[+] PRNG initialized to 0xC4658694
PID: 2  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 1  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
time on clock: 4806.4017
time on wall: 1202.7824
sum = 3.000000
2^(-28.415037)

##########################
Experiment Number 99:
#Rounds: 17 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 16384 * 16384 = 2^(30.000000)
#Queries per thread = (#Bunches per thread) * (#Queries per bunch) = 16384 * 16384 = 2^(28.000000)
[+] PRNG initialized to 0xC465B587
[+] PRNG initialized to 0xC465B592
[+] PRNG initialized to 0xC465B59D
[+] PRNG initialized to 0xC465B57C
PID: 1  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 0/16384
PID: 0  	 Bunch Number: 0/16384
PID: 2  	 Bunch Number: 0/16384
PID: 3  	 Bunch Number: 1024/16384
PID: 1  	 Bunch Number: 1024/16384
PID: 2  	 Bunch Number: 1024/16384
PID: 0  	 Bunch Number: 1024/16384
PID: 3  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 2048/16384
PID: 2  	 Bunch Number: 2048/16384
PID: 0  	 Bunch Number: 2048/16384
PID: 1  	 Bunch Number: 3072/16384
PID: 3  	 Bunch Number: 3072/16384
PID: 2  	 Bunch Number: 3072/16384
PID: 0  	 Bunch Number: 3072/16384
PID: 1  	 Bunch Number: 4096/16384
PID: 2  	 Bunch Number: 4096/16384
PID: 0  	 Bunch Number: 4096/16384
PID: 3  	 Bunch Number: 4096/16384
PID: 1  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 5120/16384
PID: 0  	 Bunch Number: 5120/16384
PID: 3  	 Bunch Number: 5120/16384
PID: 2  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 6144/16384
PID: 3  	 Bunch Number: 6144/16384
PID: 0  	 Bunch Number: 6144/16384
PID: 1  	 Bunch Number: 7168/16384
PID: 2  	 Bunch Number: 7168/16384
PID: 3  	 Bunch Number: 7168/16384
PID: 0  	 Bunch Number: 7168/16384
PID: 1  	 Bunch Number: 8192/16384
PID: 2  	 Bunch Number: 8192/16384
PID: 3  	 Bunch Number: 8192/16384
PID: 0  	 Bunch Number: 8192/16384
PID: 1  	 Bunch Number: 9216/16384
PID: 2  	 Bunch Number: 9216/16384
PID: 3  	 Bunch Number: 9216/16384
PID: 0  	 Bunch Number: 9216/16384
PID: 1  	 Bunch Number: 10240/16384
PID: 2  	 Bunch Number: 10240/16384
PID: 3  	 Bunch Number: 10240/16384
PID: 0  	 Bunch Number: 10240/16384
PID: 1  	 Bunch Number: 11264/16384
PID: 2  	 Bunch Number: 11264/16384
PID: 3  	 Bunch Number: 11264/16384
PID: 0  	 Bunch Number: 11264/16384
PID: 1  	 Bunch Number: 12288/16384
PID: 2  	 Bunch Number: 12288/16384
PID: 3  	 Bunch Number: 12288/16384
PID: 0  	 Bunch Number: 12288/16384
PID: 1  	 Bunch Number: 13312/16384
PID: 2  	 Bunch Number: 13312/16384
PID: 3  	 Bunch Number: 13312/16384
PID: 0  	 Bunch Number: 13312/16384
PID: 1  	 Bunch Number: 14336/16384
PID: 2  	 Bunch Number: 14336/16384
PID: 3  	 Bunch Number: 14336/16384
PID: 0  	 Bunch Number: 14336/16384
PID: 1  	 Bunch Number: 15360/16384
PID: 2  	 Bunch Number: 15360/16384
PID: 3  	 Bunch Number: 15360/16384
PID: 0  	 Bunch Number: 15360/16384
time on clock: 4801.8017
time on wall: 1201.7720
sum = 5.000000
2^(-27.678072)

##########################
A summary of all results:
2^(-26.54), 2^(-27.42), 2^(-27.00), 2^(-26.09), 2^(-26.09), 2^(-25.61), 2^(-25.00), 2^(-27.68), 2^(-24.83), 2^(-28.00), 2^(-25.09), 2^(-28.42), 2^(-27.68), 2^(-26.54), 2^(-25.36), 2^(-26.19), 2^(-28.00), 2^(-28.42), 2^(-25.68), 2^(-25.83), 2^(-27.42), 2^(-24.91), 2^(-26.09), 2^(-26.68), 2^(-28.42), 2^(-28.00), 2^(-28.42), 2^(-26.09), 2^(-27.42), 2^(-26.42), 2^(-26.68), 2^(-29.00), 2^(-26.42), 2^(-26.09), 2^(-28.00), 2^(-25.09), 2^(-27.00), 2^(-25.54), 2^(-27.19), 2^(-27.00), 2^(-27.00), 2^(-29.00), 2^(-26.09), 2^(-29.00), 2^(-27.68), 2^(-26.19), 2^(-27.68), 2^(-28.42), 2^(-25.48), 2^(-28.42), 2^(-27.68), 2^(-27.68), 2^(-27.68), 2^(-26.09), 2^(-26.68), 2^(-28.00), 2^(-29.00), 2^(-26.09), 2^(-25.25), 2^(-26.30), 2^(-28.42), 2^(-24.75), 2^(-28.42), 2^(-26.09), 2^(-26.19), 2^(-27.68), 2^(-27.00), 2^(-28.42), 2^(-25.61), 2^(-25.48), 2^(-26.83), 2^(-25.19), 2^(-27.42), 2^(-27.68), 2^(-25.30), 2^(-26.42), 2^(-26.68), 2^(-28.00), 2^(-27.19), 2^(-26.68), 2^(-28.42), 2^(-26.00), 2^(-25.48), 2^(-27.68), 2^(-25.83), 2^(-27.68), 2^(-28.42), 2^(-27.42), 2^(-29.00), 2^(-28.42), 2^(-27.00), 2^(-26.68), 2^(-25.54), 2^(-26.54), 2^(-27.00), 2^(-25.68), 2^(-26.30), 2^(-30.00), 2^(-28.42), 2^(-27.68), 
##########################
Average = 2^(-26.5043)
```