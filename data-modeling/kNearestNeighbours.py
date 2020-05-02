#!/bin/bash
#
##SBATCH --nodes=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=10:00:00
#SBATCH --mem=16GB
#SBATCH --job-name=Knn
#SBATCH --mail-type=END
##SBATCH --mail-user=sb7261@nyu.edu
#SBATCH --output=slurm_%j.out

module purge
conda activate airbnb-pred
python3 knn.py
