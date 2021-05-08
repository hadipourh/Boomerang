#!/bin/sh
# Beginning of PBS batch script.
#PBS -e Error
#PBS -N craft-jobarray-11r
#PBS -q batch 
#PBS -l walltime=1:59:00
#PBS -t 0-31
### Request "select" nodes, each with "mpiprocs" MPI task and "ompthreads" threads
### Send email on abort, begin and end
#PBS -m abe
### Specify mail recipient
#PBS -M hsn.hadipour@gmail.com

cd $PBS_O_WORKDIR
./craft-jobarray-11r ${PBS_ARRAYID}


