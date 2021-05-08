#!/bin/sh
# Beginning of PBS batch script.

#$ -e Error
#$ -l h_rt=23:30:0
#$ -t 1-625
### Request "select" nodes, each with "mpiprocs" MPI task and "ompthreads" threads
###$ -l select=1:ncpus=1:mpiprocs=1:ompthreads=1
#$ -cwd
#$ -N afirouz

#module load compilers/gnu/4.9.2
#module load gcc-libs/4.9.2

echo "Array number: $(expr ${SGE_TASK_ID} - 1)"
echo "###"
./GenMatrix8re $(expr ${SGE_TASK_ID} - 1)
