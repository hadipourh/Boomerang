#!/bin/sh
# Beginning of PBS batch script.
#PBS -e ErrorGenMatrix7rNew
#PBS -N test
#PBS -q batch 
#PBS -l walltime=23:59:00
#PBS -t 0-624
## PBS -l nodes=1:ppn=1
### Send email on abort, begin and end
###PBS -m abe
### Specify mail recipient
###PBS -M hsn.hadipour@gmail.com

cd $PBS_O_WORKDIR
./GenMatrix7re ${PBS_ARRAYID}


