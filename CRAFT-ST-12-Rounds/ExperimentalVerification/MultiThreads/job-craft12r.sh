#!/bin/sh
# Beginning of PBS batch script.
#PBS -o $PBS_JOBID.log
#PBS -e $PBS_JOBID.err
#PBS -N test
#PBS -q batch
#PBS -l walltime=23:59:00
### Request "select" nodes, each with "mpiprocs" MPI task and "ompthreads" threads
#PBS -l nodes=1:ppn=32
### Send email on abort, begin and end
#PBS -m abe
### Specify mail recipient
#PBS -M hsn.hadipour@gmail.com

/lustre/home/2020057/craft-12r

