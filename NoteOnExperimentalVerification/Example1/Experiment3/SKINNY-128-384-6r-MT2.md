In this experiment, we utilize 4 parallel threads each of which running 2^10 bunches of 2^12 boomerang queries where a different random tweakey is used in each bunch. In other words, we essentially divide 2^24 boomerang queries into 2^12 subsets each of which including 2^12 boomerang queries where a new random tweakey is used for each subset. Next, we repeat this experiment 128 times and compute the average of 128 outcomes.

Results:

```sh
Experiment Number 0:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46665E4
[+] PRNG initialized to 0xC46665FA
[+] PRNG initialized to 0xC4666605
[+] PRNG initialized to 0xC46665EF
time on clock: 77.1315
time on wall: 20.1062
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 1:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46666B7
[+] PRNG initialized to 0xC46666C2
[+] PRNG initialized to 0xC46666CD
[+] PRNG initialized to 0xC46666AC
time on clock: 77.3237
time on wall: 20.0687
sum = 16.000000
2^(-20.000000)

##########################
Experiment Number 2:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666774
[+] PRNG initialized to 0xC466677F
[+] PRNG initialized to 0xC4666795
[+] PRNG initialized to 0xC466678A
time on clock: 77.6673
time on wall: 20.1335
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 3:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466683C
[+] PRNG initialized to 0xC4666847
[+] PRNG initialized to 0xC4666852
[+] PRNG initialized to 0xC466685D
time on clock: 77.5994
time on wall: 20.0859
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 4:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666904
[+] PRNG initialized to 0xC4666925
[+] PRNG initialized to 0xC466690F
[+] PRNG initialized to 0xC466691A
time on clock: 77.5440
time on wall: 20.0915
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 5:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46669ED
[+] PRNG initialized to 0xC46669E2
[+] PRNG initialized to 0xC46669D7
[+] PRNG initialized to 0xC46669CC
time on clock: 77.3808
time on wall: 20.0641
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 6:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666ABF
[+] PRNG initialized to 0xC4666AA9
[+] PRNG initialized to 0xC4666A9E
[+] PRNG initialized to 0xC4666AB4
time on clock: 77.4177
time on wall: 20.0328
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 7:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666B71
[+] PRNG initialized to 0xC4666B7C
[+] PRNG initialized to 0xC4666B87
[+] PRNG initialized to 0xC4666B66
time on clock: 77.6647
time on wall: 20.1502
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 8:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666C4F
[+] PRNG initialized to 0xC4666C44
[+] PRNG initialized to 0xC4666C2E
[+] PRNG initialized to 0xC4666C39
time on clock: 77.6474
time on wall: 20.1582
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 9:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666D01
[+] PRNG initialized to 0xC4666D0C
[+] PRNG initialized to 0xC4666CF6
[+] PRNG initialized to 0xC4666D17
time on clock: 77.4836
time on wall: 20.0658
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 10:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666DC9
[+] PRNG initialized to 0xC4666DDF
[+] PRNG initialized to 0xC4666DD4
[+] PRNG initialized to 0xC4666DBE
time on clock: 76.8192
time on wall: 19.9745
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 11:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666E9C
[+] PRNG initialized to 0xC4666EA7
[+] PRNG initialized to 0xC4666E86
[+] PRNG initialized to 0xC4666E91
time on clock: 76.4740
time on wall: 19.9767
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 12:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4666F4E
[+] PRNG initialized to 0xC4666F64
[+] PRNG initialized to 0xC4666F59
[+] PRNG initialized to 0xC4666F6F
time on clock: 77.1986
time on wall: 19.9810
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 13:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667016
[+] PRNG initialized to 0xC4667037
[+] PRNG initialized to 0xC4667021
[+] PRNG initialized to 0xC466702C
time on clock: 77.5739
time on wall: 20.0870
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 14:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46670DE
[+] PRNG initialized to 0xC46670E9
[+] PRNG initialized to 0xC46670FF
[+] PRNG initialized to 0xC46670F4
time on clock: 77.4960
time on wall: 20.1638
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 15:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46671C7
[+] PRNG initialized to 0xC46671B1
[+] PRNG initialized to 0xC46671A6
[+] PRNG initialized to 0xC46671BC
time on clock: 77.2030
time on wall: 20.0263
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 16:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667284
[+] PRNG initialized to 0xC466728F
[+] PRNG initialized to 0xC466726E
[+] PRNG initialized to 0xC4667279
time on clock: 77.8208
time on wall: 20.1680
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 17:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667336
[+] PRNG initialized to 0xC4667341
[+] PRNG initialized to 0xC4667357
[+] PRNG initialized to 0xC466734C
time on clock: 77.1939
time on wall: 20.0566
sum = 18.000000
2^(-19.830075)

##########################
Experiment Number 18:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667414
[+] PRNG initialized to 0xC46673FE
[+] PRNG initialized to 0xC4667409
[+] PRNG initialized to 0xC466741F
time on clock: 77.7309
time on wall: 20.1496
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 19:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46674D0
[+] PRNG initialized to 0xC46674DB
[+] PRNG initialized to 0xC46674E6
[+] PRNG initialized to 0xC46674F1
time on clock: 77.6794
time on wall: 20.1420
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 20:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46675AE
[+] PRNG initialized to 0xC46675B9
[+] PRNG initialized to 0xC46675A3
[+] PRNG initialized to 0xC4667598
time on clock: 77.9163
time on wall: 20.2043
sum = 18.000000
2^(-19.830075)

##########################
Experiment Number 21:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667681
[+] PRNG initialized to 0xC466766B
[+] PRNG initialized to 0xC4667676
[+] PRNG initialized to 0xC4667660
time on clock: 77.2247
time on wall: 20.0340
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 22:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667733
[+] PRNG initialized to 0xC466773E
[+] PRNG initialized to 0xC4667728
[+] PRNG initialized to 0xC4667749
time on clock: 77.2383
time on wall: 20.0629
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 23:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667811
[+] PRNG initialized to 0xC46677FB
[+] PRNG initialized to 0xC46677F0
[+] PRNG initialized to 0xC4667806
time on clock: 77.3043
time on wall: 20.0608
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 24:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46678D9
[+] PRNG initialized to 0xC46678C3
[+] PRNG initialized to 0xC46678CE
[+] PRNG initialized to 0xC46678B8
time on clock: 77.1934
time on wall: 19.9954
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 25:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667980
[+] PRNG initialized to 0xC466798B
[+] PRNG initialized to 0xC46679A1
[+] PRNG initialized to 0xC4667996
time on clock: 77.3922
time on wall: 20.0971
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 26:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667A53
[+] PRNG initialized to 0xC4667A48
[+] PRNG initialized to 0xC4667A5E
[+] PRNG initialized to 0xC4667A69
time on clock: 71.0631
time on wall: 19.8748
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 27:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667B10
[+] PRNG initialized to 0xC4667B31
[+] PRNG initialized to 0xC4667B26
[+] PRNG initialized to 0xC4667B1B
time on clock: 72.5108
time on wall: 20.3353
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 28:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667BEE
[+] PRNG initialized to 0xC4667BD8
[+] PRNG initialized to 0xC4667BF9
[+] PRNG initialized to 0xC4667BE3
time on clock: 78.6885
time on wall: 20.2649
sum = 18.000000
2^(-19.830075)

##########################
Experiment Number 29:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667CB5
[+] PRNG initialized to 0xC4667CCB
[+] PRNG initialized to 0xC4667CC0
[+] PRNG initialized to 0xC4667CAA
time on clock: 78.7862
time on wall: 20.3004
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 30:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667D88
[+] PRNG initialized to 0xC4667D7D
[+] PRNG initialized to 0xC4667D93
[+] PRNG initialized to 0xC4667D72
time on clock: 78.0028
time on wall: 20.1698
sum = 18.000000
2^(-19.830075)

##########################
Experiment Number 31:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667E50
[+] PRNG initialized to 0xC4667E5B
[+] PRNG initialized to 0xC4667E3A
[+] PRNG initialized to 0xC4667E45
time on clock: 78.7279
time on wall: 20.2841
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 32:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667F23
[+] PRNG initialized to 0xC4667F0D
[+] PRNG initialized to 0xC4667F18
[+] PRNG initialized to 0xC4667F02
time on clock: 78.4373
time on wall: 20.1887
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 33:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4667FEA
[+] PRNG initialized to 0xC4667FF5
[+] PRNG initialized to 0xC4667FD4
[+] PRNG initialized to 0xC4667FDF
time on clock: 78.5849
time on wall: 20.2259
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 34:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46680A7
[+] PRNG initialized to 0xC46680B2
[+] PRNG initialized to 0xC466809C
[+] PRNG initialized to 0xC46680BD
time on clock: 78.1952
time on wall: 20.1512
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 35:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668164
[+] PRNG initialized to 0xC4668185
[+] PRNG initialized to 0xC466817A
[+] PRNG initialized to 0xC466816F
time on clock: 78.2394
time on wall: 20.1441
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 36:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466822C
[+] PRNG initialized to 0xC4668237
[+] PRNG initialized to 0xC466824D
[+] PRNG initialized to 0xC4668242
time on clock: 78.6454
time on wall: 20.2542
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 37:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46682FF
[+] PRNG initialized to 0xC466830A
[+] PRNG initialized to 0xC4668315
[+] PRNG initialized to 0xC46682F4
time on clock: 78.1215
time on wall: 20.1357
sum = 16.000000
2^(-20.000000)

##########################
Experiment Number 38:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46683BC
[+] PRNG initialized to 0xC46683D2
[+] PRNG initialized to 0xC46683DD
[+] PRNG initialized to 0xC46683C7
time on clock: 78.5000
time on wall: 20.1850
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 39:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466848E
[+] PRNG initialized to 0xC46684AF
[+] PRNG initialized to 0xC4668499
[+] PRNG initialized to 0xC46684A4
time on clock: 78.4258
time on wall: 20.1693
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 40:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668556
[+] PRNG initialized to 0xC4668577
[+] PRNG initialized to 0xC466856C
[+] PRNG initialized to 0xC4668561
time on clock: 78.5603
time on wall: 20.1997
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 41:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668634
[+] PRNG initialized to 0xC466861E
[+] PRNG initialized to 0xC4668629
[+] PRNG initialized to 0xC466863F
time on clock: 78.1257
time on wall: 20.1701
sum = 19.000000
2^(-19.752072)

##########################
Experiment Number 42:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668707
[+] PRNG initialized to 0xC46686F1
[+] PRNG initialized to 0xC46686E6
[+] PRNG initialized to 0xC46686FC
time on clock: 78.5997
time on wall: 20.2407
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 43:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46687AE
[+] PRNG initialized to 0xC46687B9
[+] PRNG initialized to 0xC46687C4
[+] PRNG initialized to 0xC46687CF
time on clock: 78.5718
time on wall: 20.2747
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 44:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466888B
[+] PRNG initialized to 0xC4668896
[+] PRNG initialized to 0xC4668880
[+] PRNG initialized to 0xC46688A1
time on clock: 78.6735
time on wall: 20.2535
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 45:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466895E
[+] PRNG initialized to 0xC4668953
[+] PRNG initialized to 0xC4668969
[+] PRNG initialized to 0xC4668948
time on clock: 78.8931
time on wall: 20.2928
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 46:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668A10
[+] PRNG initialized to 0xC4668A26
[+] PRNG initialized to 0xC4668A1B
[+] PRNG initialized to 0xC4668A31
time on clock: 78.1339
time on wall: 20.1389
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 47:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668AEE
[+] PRNG initialized to 0xC4668AE3
[+] PRNG initialized to 0xC4668AD8
[+] PRNG initialized to 0xC4668AF9
time on clock: 78.8801
time on wall: 20.2983
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 48:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668BCB
[+] PRNG initialized to 0xC4668BC0
[+] PRNG initialized to 0xC4668BB5
[+] PRNG initialized to 0xC4668BAA
time on clock: 79.0525
time on wall: 20.3179
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 49:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668C93
[+] PRNG initialized to 0xC4668C7D
[+] PRNG initialized to 0xC4668C88
[+] PRNG initialized to 0xC4668C72
time on clock: 78.4090
time on wall: 20.1749
sum = 17.000000
2^(-19.912537)

##########################
Experiment Number 50:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668D45
[+] PRNG initialized to 0xC4668D5B
[+] PRNG initialized to 0xC4668D50
[+] PRNG initialized to 0xC4668D3A
time on clock: 78.5755
time on wall: 20.2483
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 51:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668E02
[+] PRNG initialized to 0xC4668E0D
[+] PRNG initialized to 0xC4668E18
[+] PRNG initialized to 0xC4668E23
time on clock: 78.1609
time on wall: 20.1533
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 52:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668ED4
[+] PRNG initialized to 0xC4668EF5
[+] PRNG initialized to 0xC4668EDF
[+] PRNG initialized to 0xC4668EEA
time on clock: 78.0352
time on wall: 20.1269
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 53:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4668FA7
[+] PRNG initialized to 0xC4668F9C
[+] PRNG initialized to 0xC4668FB2
[+] PRNG initialized to 0xC4668FBD
time on clock: 78.7530
time on wall: 20.2604
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 54:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466907A
[+] PRNG initialized to 0xC4669085
[+] PRNG initialized to 0xC4669064
[+] PRNG initialized to 0xC466906F
time on clock: 78.0298
time on wall: 20.1229
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 55:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466912C
[+] PRNG initialized to 0xC4669142
[+] PRNG initialized to 0xC4669137
[+] PRNG initialized to 0xC466914D
time on clock: 78.0650
time on wall: 20.1493
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 56:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669215
[+] PRNG initialized to 0xC466920A
[+] PRNG initialized to 0xC46691FF
[+] PRNG initialized to 0xC46691F4
time on clock: 78.6772
time on wall: 20.2112
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 57:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46692C7
[+] PRNG initialized to 0xC46692DD
[+] PRNG initialized to 0xC46692D2
[+] PRNG initialized to 0xC46692BC
time on clock: 78.9201
time on wall: 20.3150
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 58:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466938E
[+] PRNG initialized to 0xC4669399
[+] PRNG initialized to 0xC46693A4
[+] PRNG initialized to 0xC46693AF
time on clock: 78.5247
time on wall: 20.2002
sum = 23.000000
2^(-19.476438)

##########################
Experiment Number 59:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669456
[+] PRNG initialized to 0xC4669477
[+] PRNG initialized to 0xC466946C
[+] PRNG initialized to 0xC4669461
time on clock: 78.4266
time on wall: 20.2316
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 60:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669529
[+] PRNG initialized to 0xC4669534
[+] PRNG initialized to 0xC466953F
[+] PRNG initialized to 0xC466951E
time on clock: 78.1221
time on wall: 20.1705
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 61:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46695FC
[+] PRNG initialized to 0xC4669607
[+] PRNG initialized to 0xC46695F1
[+] PRNG initialized to 0xC46695E6
time on clock: 71.0057
time on wall: 19.7041
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 62:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46696B9
[+] PRNG initialized to 0xC46696AE
[+] PRNG initialized to 0xC46696C4
[+] PRNG initialized to 0xC46696CF
time on clock: 77.1820
time on wall: 20.0465
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 63:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669776
[+] PRNG initialized to 0xC466978C
[+] PRNG initialized to 0xC4669781
[+] PRNG initialized to 0xC4669797
time on clock: 78.7724
time on wall: 20.1703
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 64:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466983E
[+] PRNG initialized to 0xC466985F
[+] PRNG initialized to 0xC4669849
[+] PRNG initialized to 0xC4669854
time on clock: 79.1564
time on wall: 20.2464
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 65:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669910
[+] PRNG initialized to 0xC466991B
[+] PRNG initialized to 0xC4669931
[+] PRNG initialized to 0xC4669926
time on clock: 78.2691
time on wall: 20.0414
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 66:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC46699EE
[+] PRNG initialized to 0xC46699E3
[+] PRNG initialized to 0xC46699F9
[+] PRNG initialized to 0xC46699D8
time on clock: 78.9039
time on wall: 20.1922
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 67:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669AC1
[+] PRNG initialized to 0xC4669AA0
[+] PRNG initialized to 0xC4669AB6
[+] PRNG initialized to 0xC4669AAB
time on clock: 78.4801
time on wall: 20.0820
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 68:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669B73
[+] PRNG initialized to 0xC4669B7E
[+] PRNG initialized to 0xC4669B68
[+] PRNG initialized to 0xC4669B89
time on clock: 75.5229
time on wall: 19.9438
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 69:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669C30
[+] PRNG initialized to 0xC4669C3B
[+] PRNG initialized to 0xC4669C51
[+] PRNG initialized to 0xC4669C46
time on clock: 76.6043
time on wall: 19.9806
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 70:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669D0E
[+] PRNG initialized to 0xC4669D19
[+] PRNG initialized to 0xC4669CF8
[+] PRNG initialized to 0xC4669D03
time on clock: 76.5055
time on wall: 19.9986
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 71:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669DC0
[+] PRNG initialized to 0xC4669DE1
[+] PRNG initialized to 0xC4669DD6
[+] PRNG initialized to 0xC4669DCB
time on clock: 77.3011
time on wall: 20.0814
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 72:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669E93
[+] PRNG initialized to 0xC4669E88
[+] PRNG initialized to 0xC4669EA9
[+] PRNG initialized to 0xC4669E9E
time on clock: 77.4719
time on wall: 20.0874
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 73:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC4669F5B
[+] PRNG initialized to 0xC4669F71
[+] PRNG initialized to 0xC4669F50
[+] PRNG initialized to 0xC4669F66
time on clock: 77.6442
time on wall: 20.1181
sum = 16.000000
2^(-20.000000)

##########################
Experiment Number 74:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A018
[+] PRNG initialized to 0xC466A02E
[+] PRNG initialized to 0xC466A039
[+] PRNG initialized to 0xC466A023
time on clock: 76.4687
time on wall: 19.8734
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 75:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A0E0
[+] PRNG initialized to 0xC466A101
[+] PRNG initialized to 0xC466A0EB
[+] PRNG initialized to 0xC466A0F6
time on clock: 78.2006
time on wall: 20.1576
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 76:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A1BE
[+] PRNG initialized to 0xC466A1B3
[+] PRNG initialized to 0xC466A1C9
[+] PRNG initialized to 0xC466A1A8
time on clock: 78.7902
time on wall: 20.1932
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 77:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A27B
[+] PRNG initialized to 0xC466A291
[+] PRNG initialized to 0xC466A286
[+] PRNG initialized to 0xC466A270
time on clock: 78.9604
time on wall: 20.1964
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 78:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A338
[+] PRNG initialized to 0xC466A359
[+] PRNG initialized to 0xC466A343
[+] PRNG initialized to 0xC466A34E
time on clock: 79.0167
time on wall: 20.2152
sum = 5.000000
2^(-21.678072)

##########################
Experiment Number 79:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A415
[+] PRNG initialized to 0xC466A420
[+] PRNG initialized to 0xC466A42B
[+] PRNG initialized to 0xC466A40A
time on clock: 79.1435
time on wall: 20.2771
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 80:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A4D2
[+] PRNG initialized to 0xC466A4F3
[+] PRNG initialized to 0xC466A4DD
[+] PRNG initialized to 0xC466A4E8
time on clock: 79.3636
time on wall: 20.3113
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 81:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A5A5
[+] PRNG initialized to 0xC466A5BB
[+] PRNG initialized to 0xC466A5B0
[+] PRNG initialized to 0xC466A59A
time on clock: 79.0283
time on wall: 20.2478
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 82:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A68D
[+] PRNG initialized to 0xC466A677
[+] PRNG initialized to 0xC466A682
[+] PRNG initialized to 0xC466A66C
time on clock: 78.0168
time on wall: 20.0205
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 83:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A755
[+] PRNG initialized to 0xC466A734
[+] PRNG initialized to 0xC466A73F
[+] PRNG initialized to 0xC466A74A
time on clock: 78.5370
time on wall: 20.0919
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 84:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A7FC
[+] PRNG initialized to 0xC466A812
[+] PRNG initialized to 0xC466A807
[+] PRNG initialized to 0xC466A81D
time on clock: 78.3323
time on wall: 20.0091
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 85:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A8CF
[+] PRNG initialized to 0xC466A8E5
[+] PRNG initialized to 0xC466A8C4
[+] PRNG initialized to 0xC466A8DA
time on clock: 78.8533
time on wall: 20.2112
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 86:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466A9AD
[+] PRNG initialized to 0xC466A98C
[+] PRNG initialized to 0xC466A9A2
[+] PRNG initialized to 0xC466A997
time on clock: 79.4943
time on wall: 20.3513
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 87:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AA5F
[+] PRNG initialized to 0xC466AA6A
[+] PRNG initialized to 0xC466AA54
[+] PRNG initialized to 0xC466AA75
time on clock: 78.5546
time on wall: 20.1183
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 88:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AB3D
[+] PRNG initialized to 0xC466AB27
[+] PRNG initialized to 0xC466AB32
[+] PRNG initialized to 0xC466AB1C
time on clock: 78.9749
time on wall: 20.1835
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 89:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AC04
[+] PRNG initialized to 0xC466AC0F
[+] PRNG initialized to 0xC466ABF9
[+] PRNG initialized to 0xC466ABEE
time on clock: 78.8307
time on wall: 20.1393
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 90:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466ACD7
[+] PRNG initialized to 0xC466ACCC
[+] PRNG initialized to 0xC466ACC1
[+] PRNG initialized to 0xC466ACB6
time on clock: 70.7285
time on wall: 19.4807
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 91:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AD8A
[+] PRNG initialized to 0xC466AD7F
[+] PRNG initialized to 0xC466AD95
[+] PRNG initialized to 0xC466AD74
time on clock: 78.6977
time on wall: 20.1902
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 92:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AE3C
[+] PRNG initialized to 0xC466AE52
[+] PRNG initialized to 0xC466AE5D
[+] PRNG initialized to 0xC466AE47
time on clock: 79.2966
time on wall: 20.2432
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 93:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AF19
[+] PRNG initialized to 0xC466AF24
[+] PRNG initialized to 0xC466AF0E
[+] PRNG initialized to 0xC466AF2F
time on clock: 79.7242
time on wall: 20.3776
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 94:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466AFD6
[+] PRNG initialized to 0xC466AFE1
[+] PRNG initialized to 0xC466AFEC
[+] PRNG initialized to 0xC466AFF7
time on clock: 79.2484
time on wall: 20.2522
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 95:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B09E
[+] PRNG initialized to 0xC466B0A9
[+] PRNG initialized to 0xC466B0BF
[+] PRNG initialized to 0xC466B0B4
time on clock: 78.9439
time on wall: 20.1316
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 96:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B166
[+] PRNG initialized to 0xC466B187
[+] PRNG initialized to 0xC466B171
[+] PRNG initialized to 0xC466B17C
time on clock: 79.5767
time on wall: 20.3023
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 97:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B243
[+] PRNG initialized to 0xC466B238
[+] PRNG initialized to 0xC466B259
[+] PRNG initialized to 0xC466B24E
time on clock: 79.2346
time on wall: 20.3138
sum = 5.000000
2^(-21.678072)

##########################
Experiment Number 98:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B300
[+] PRNG initialized to 0xC466B316
[+] PRNG initialized to 0xC466B30B
[+] PRNG initialized to 0xC466B321
time on clock: 78.9216
time on wall: 20.1195
sum = 17.000000
2^(-19.912537)

##########################
Experiment Number 99:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B3D3
[+] PRNG initialized to 0xC466B3E9
[+] PRNG initialized to 0xC466B3DE
[+] PRNG initialized to 0xC466B3C8
time on clock: 78.7023
time on wall: 20.0887
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 100:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B4B1
[+] PRNG initialized to 0xC466B4A6
[+] PRNG initialized to 0xC466B49B
[+] PRNG initialized to 0xC466B490
time on clock: 79.7876
time on wall: 20.3716
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 101:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B562
[+] PRNG initialized to 0xC466B578
[+] PRNG initialized to 0xC466B56D
[+] PRNG initialized to 0xC466B583
time on clock: 79.9619
time on wall: 20.4277
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 102:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B640
[+] PRNG initialized to 0xC466B635
[+] PRNG initialized to 0xC466B64B
[+] PRNG initialized to 0xC466B62A
time on clock: 78.6413
time on wall: 20.0176
sum = 17.000000
2^(-19.912537)

##########################
Experiment Number 103:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B6F2
[+] PRNG initialized to 0xC466B713
[+] PRNG initialized to 0xC466B708
[+] PRNG initialized to 0xC466B6FD
time on clock: 79.7293
time on wall: 20.3430
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 104:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B7C5
[+] PRNG initialized to 0xC466B7D0
[+] PRNG initialized to 0xC466B7BA
[+] PRNG initialized to 0xC466B7DB
time on clock: 79.4950
time on wall: 20.2657
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 105:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B88C
[+] PRNG initialized to 0xC466B897
[+] PRNG initialized to 0xC466B8A2
[+] PRNG initialized to 0xC466B8AD
time on clock: 79.3897
time on wall: 20.2625
sum = 6.000000
2^(-21.415037)

##########################
Experiment Number 106:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466B96A
[+] PRNG initialized to 0xC466B954
[+] PRNG initialized to 0xC466B95F
[+] PRNG initialized to 0xC466B975
time on clock: 79.7049
time on wall: 20.3866
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 107:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BA3D
[+] PRNG initialized to 0xC466BA27
[+] PRNG initialized to 0xC466BA32
[+] PRNG initialized to 0xC466BA1C
time on clock: 79.5659
time on wall: 20.2755
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 108:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BB0F
[+] PRNG initialized to 0xC466BB04
[+] PRNG initialized to 0xC466BAF9
[+] PRNG initialized to 0xC466BAEE
time on clock: 80.2868
time on wall: 20.4388
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 109:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BBB6
[+] PRNG initialized to 0xC466BBD7
[+] PRNG initialized to 0xC466BBCC
[+] PRNG initialized to 0xC466BBC1
time on clock: 79.5125
time on wall: 20.2780
sum = 10.000000
2^(-20.678072)

##########################
Experiment Number 110:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BC7E
[+] PRNG initialized to 0xC466BC9F
[+] PRNG initialized to 0xC466BC89
[+] PRNG initialized to 0xC466BC94
time on clock: 78.8467
time on wall: 20.1167
sum = 7.000000
2^(-21.192645)

##########################
Experiment Number 111:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BD46
[+] PRNG initialized to 0xC466BD5C
[+] PRNG initialized to 0xC466BD51
[+] PRNG initialized to 0xC466BD67
time on clock: 80.2141
time on wall: 20.4640
sum = 12.000000
2^(-20.415037)

##########################
Experiment Number 112:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BE39
[+] PRNG initialized to 0xC466BE2E
[+] PRNG initialized to 0xC466BE18
[+] PRNG initialized to 0xC466BE23
time on clock: 79.1846
time on wall: 20.1865
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 113:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BF01
[+] PRNG initialized to 0xC466BEF6
[+] PRNG initialized to 0xC466BEEB
[+] PRNG initialized to 0xC466BEE0
time on clock: 79.7348
time on wall: 20.3556
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 114:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466BFA8
[+] PRNG initialized to 0xC466BFB3
[+] PRNG initialized to 0xC466BFBE
[+] PRNG initialized to 0xC466BFC9
time on clock: 79.8950
time on wall: 20.4376
sum = 8.000000
2^(-21.000000)

##########################
Experiment Number 115:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C09B
[+] PRNG initialized to 0xC466C085
[+] PRNG initialized to 0xC466C07A
[+] PRNG initialized to 0xC466C090
time on clock: 79.1037
time on wall: 20.2782
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 116:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C163
[+] PRNG initialized to 0xC466C158
[+] PRNG initialized to 0xC466C142
[+] PRNG initialized to 0xC466C14D
time on clock: 79.3090
time on wall: 20.2961
sum = 17.000000
2^(-19.912537)

##########################
Experiment Number 117:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C220
[+] PRNG initialized to 0xC466C215
[+] PRNG initialized to 0xC466C22B
[+] PRNG initialized to 0xC466C20A
time on clock: 79.4189
time on wall: 20.3298
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 118:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C2E7
[+] PRNG initialized to 0xC466C2F2
[+] PRNG initialized to 0xC466C2DC
[+] PRNG initialized to 0xC466C2FD
time on clock: 79.0186
time on wall: 20.1459
sum = 19.000000
2^(-19.752072)

##########################
Experiment Number 119:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C3BA
[+] PRNG initialized to 0xC466C3AF
[+] PRNG initialized to 0xC466C3C5
[+] PRNG initialized to 0xC466C3A4
time on clock: 79.5661
time on wall: 20.3025
sum = 14.000000
2^(-20.192645)

##########################
Experiment Number 120:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C48D
[+] PRNG initialized to 0xC466C46C
[+] PRNG initialized to 0xC466C477
[+] PRNG initialized to 0xC466C482
time on clock: 78.4844
time on wall: 20.1380
sum = 11.000000
2^(-20.540568)

##########################
Experiment Number 121:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C54A
[+] PRNG initialized to 0xC466C555
[+] PRNG initialized to 0xC466C534
[+] PRNG initialized to 0xC466C53F
time on clock: 79.1056
time on wall: 20.1994
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 122:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C61D
[+] PRNG initialized to 0xC466C612
[+] PRNG initialized to 0xC466C607
[+] PRNG initialized to 0xC466C5FC
time on clock: 78.8910
time on wall: 20.1130
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 123:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C6CE
[+] PRNG initialized to 0xC466C6EF
[+] PRNG initialized to 0xC466C6D9
[+] PRNG initialized to 0xC466C6E4
time on clock: 79.1500
time on wall: 20.1851
sum = 9.000000
2^(-20.830075)

##########################
Experiment Number 124:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C7B7
[+] PRNG initialized to 0xC466C796
[+] PRNG initialized to 0xC466C7AC
[+] PRNG initialized to 0xC466C7A1
time on clock: 78.8804
time on wall: 20.2120
sum = 15.000000
2^(-20.093109)

##########################
Experiment Number 125:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C874
[+] PRNG initialized to 0xC466C87F
[+] PRNG initialized to 0xC466C869
[+] PRNG initialized to 0xC466C85E
time on clock: 79.1069
time on wall: 20.1825
sum = 16.000000
2^(-20.000000)

##########################
Experiment Number 126:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C947
[+] PRNG initialized to 0xC466C926
[+] PRNG initialized to 0xC466C931
[+] PRNG initialized to 0xC466C93C
time on clock: 78.7115
time on wall: 20.1027
sum = 13.000000
2^(-20.299560)

##########################
Experiment Number 127:
#Rounds: 6 rounds
#Total Queries = (#Parallel threads) * (#Bunches per thread) * (#Queries per bunch) = 4 * 1024 * 4096 = 2^(24.000000)
[+] PRNG initialized to 0xC466C9EE
[+] PRNG initialized to 0xC466C9F9
[+] PRNG initialized to 0xC466CA0F
[+] PRNG initialized to 0xC466CA04
time on clock: 79.6047
time on wall: 20.3133
sum = 12.000000
2^(-20.415037)

##########################
A summary of all results:
2^(-21.00), 2^(-20.00), 2^(-20.19), 2^(-20.68), 2^(-20.19), 2^(-20.09), 2^(-20.68), 2^(-20.54), 2^(-20.42), 2^(-21.00), 2^(-21.19), 2^(-20.30), 2^(-20.09), 2^(-20.68), 2^(-20.42), 2^(-20.19), 2^(-20.30), 2^(-19.83), 2^(-20.30), 2^(-20.83), 2^(-19.83), 2^(-20.54), 2^(-20.83), 2^(-20.68), 2^(-20.83), 2^(-21.00), 2^(-20.68), 2^(-21.19), 2^(-19.83), 2^(-20.68), 2^(-19.83), 2^(-20.09), 2^(-20.19), 2^(-21.00), 2^(-20.54), 2^(-20.30), 2^(-21.42), 2^(-20.00), 2^(-20.30), 2^(-20.30), 2^(-21.42), 2^(-19.75), 2^(-21.19), 2^(-20.54), 2^(-20.54), 2^(-21.00), 2^(-20.42), 2^(-20.19), 2^(-20.19), 2^(-19.91), 2^(-21.42), 2^(-20.19), 2^(-20.19), 2^(-20.42), 2^(-20.30), 2^(-20.42), 2^(-20.68), 2^(-20.42), 2^(-19.48), 2^(-20.09), 2^(-20.42), 2^(-20.30), 2^(-20.42), 2^(-20.42), 2^(-20.09), 2^(-20.68), 2^(-20.83), 2^(-20.42), 2^(-21.42), 2^(-20.54), 2^(-20.09), 2^(-20.09), 2^(-20.30), 2^(-20.00), 2^(-20.68), 2^(-20.54), 2^(-20.68), 2^(-21.42), 2^(-21.68), 2^(-20.83), 2^(-20.83), 2^(-20.68), 2^(-20.42), 2^(-20.19), 2^(-21.00), 2^(-20.30), 2^(-20.68), 2^(-21.19), 2^(-20.83), 2^(-20.30), 2^(-20.54), 2^(-20.68), 2^(-20.68), 2^(-21.19), 2^(-20.68), 2^(-21.00), 2^(-20.54), 2^(-21.68), 2^(-19.91), 2^(-20.19), 2^(-21.19), 2^(-20.68), 2^(-19.91), 2^(-20.68), 2^(-20.83), 2^(-21.42), 2^(-21.19), 2^(-20.09), 2^(-20.68), 2^(-20.68), 2^(-21.19), 2^(-20.42), 2^(-20.19), 2^(-20.09), 2^(-21.00), 2^(-20.54), 2^(-19.91), 2^(-20.19), 2^(-19.75), 2^(-20.19), 2^(-20.54), 2^(-20.30), 2^(-20.30), 2^(-20.83), 2^(-20.09), 2^(-20.00), 2^(-20.30), 2^(-20.42), 
##########################
Average = 2^(-20.4560)
```