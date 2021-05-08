#!/bin/sh
# Beginning of PBS batch script.
#PBS -e Error-rumi-64-128-17r
#PBS -N rumi-64-128-17r
#PBS -q batch 
#PBS -l walltime=23:59:00
#PBS -t 0-511
### Request "select" nodes, each with "mpiprocs" MPI task and "ompthreads" threads
### Send email on abort, begin and end
#PBS -m abe
### Specify mail recipient
#PBS -M hsn.hadipour@gmail.com

cd $PBS_O_WORKDIR
./rumi-64-128-17r ${PBS_ARRAYID}


