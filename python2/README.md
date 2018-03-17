
conda env create -f py27.yml

conda-env export -f env.yml

conda env list

conda create --name py27 python=2.7

# Create virtual environment using env.yml
conda env create -f env.yml
