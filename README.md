# Before class prep

Before class you need to have anaconda installed and download the course documents.

You should download the v1.5 tag of the course from this git repository.

# Installation

Before class starts we'll need to make sure that we're all on the same page. To do that we'll need
to install a few extra modules and get a better package solver. On the command line of this folder execute:

Update anaconda to make sure we can find the new libmamba solver:

`conda update -n base conda`

Then install the libmamb solver:

`conda install -n base conda-libmamba-solver
conda config --set solver libmamba`

To install create a new conda environment:

`conda create --name cssma`

Activate the environment:

`conda activate cssma`

Install the conda packages:

`conda install -c conda-forge --file requirements_conda.txt`

