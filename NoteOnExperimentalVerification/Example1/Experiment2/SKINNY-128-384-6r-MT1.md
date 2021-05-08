In this experiment, we utilize 4 parallel threads each of which running 2^5 bunches of 2^17 boomerang queries where a different random tweakey is used in each bunch. In other words, we essentially divide 2^24 boomerang queries into 2^5 bunches of 2^17 boomerang queries where a new random tweakey is used for each bunch. Next we repeat such experiment 8 times and compute the average of 8 outputs.

```sh
Experiment Number 0:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EA4D
[+] PRNG initialized to 0xC465EA58
[+] PRNG initialized to 0xC465EA42
[+] PRNG initialized to 0xC465EA63
time on clock: 82.4720
time on wall: 21.5005
sum = 16.000000
2^(-20.000000)

##########################
Experiment Number 1:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EB2A
[+] PRNG initialized to 0xC465EB14
[+] PRNG initialized to 0xC465EB35
[+] PRNG initialized to 0xC465EB1F
time on clock: 82.7393
time on wall: 21.5150
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 2:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EC11
[+] PRNG initialized to 0xC465EBF0
[+] PRNG initialized to 0xC465EBFB
[+] PRNG initialized to 0xC465EC06
time on clock: 83.5118
time on wall: 21.6499
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 3:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465ECE3
[+] PRNG initialized to 0xC465ECCD
[+] PRNG initialized to 0xC465ECD8
[+] PRNG initialized to 0xC465ECC2
time on clock: 83.1841
time on wall: 21.6260
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 4:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EDBF
[+] PRNG initialized to 0xC465EDB4
[+] PRNG initialized to 0xC465ED9E
[+] PRNG initialized to 0xC465EDA9
time on clock: 83.0337
time on wall: 21.5690
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 5:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EE7A
[+] PRNG initialized to 0xC465EE90
[+] PRNG initialized to 0xC465EE85
[+] PRNG initialized to 0xC465EE9B
time on clock: 83.0263
time on wall: 21.5125
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 6:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465EF4C
[+] PRNG initialized to 0xC465EF62
[+] PRNG initialized to 0xC465EF6D
[+] PRNG initialized to 0xC465EF57
time on clock: 83.2710
time on wall: 21.6019
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 7:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 32 * 131072 = 2^(24.000000)
[+] PRNG initialized to 0xC465F028
[+] PRNG initialized to 0xC465F049
[+] PRNG initialized to 0xC465F03E
[+] PRNG initialized to 0xC465F033
time on clock: 83.2679
time on wall: 21.6150
sum = 14.000000
2^(-20.192645)

##########################
A summary of all results:
2^(-20.00), 2^(-20.54), 2^(-20.42), 2^(-20.68), 2^(-20.30), 2^(-20.42), 2^(-21.19), 2^(-20.19), 
##########################
Average = 2^(-20.4301)
```