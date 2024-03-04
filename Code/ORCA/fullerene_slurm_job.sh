#!/bin/bash

#SBATCH --job-name=fullemolopt
#SBATCH --partition=rack
#SBATCH
#
#SBATCH -nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --mem=48GB
#SBATCH --mail-user=pomorenor@unal.edu.co
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE

unset SINGULARITY_BINDPATH
export SINGULARITY_BINDPATH="/scratch:/scratch,/home:/home"
singularity run /localapps/centos7.gaussian16.sif /bin/sh He3C60_opt.sh	
