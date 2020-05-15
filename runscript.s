#!/bin/bash
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --time=03:00:00
#SBATCH --mem=50000
#SBATCH --job-name=bds
#SBATCH --mail-user=sb7261@nyu.edu
#SBATCH --output=slurm_%j.out

conda env create -f req.yml
conda activate BDS1
pip install uszipcode
pip install xgboost
python3 data-cleaning/airbnb-cleaning/clean.py
python3 data-cleaning/311-dataset-cleaning/311_complaints_only.py
python3 visualisation/airbnb-visualisation/visualise-airbnb.py
python3 data-integration/dataintegration.py
python3 feature-selection/handpicking.py
python3 feature-selection/correlation.py
python3 feature-selection/rfe.py
python3 feature-selection/forward-selection/forward-selection.py
python3 feature-selection/forward-selection/forward-selection-intersection.py
python3 feature-selection/forward-selection/forward-selection-topcomplaints.py
python3 data-modeling/run_models.py 
python3 results-analysis/modeling_results.py
python3 results-analysis/featureselection_results.py

