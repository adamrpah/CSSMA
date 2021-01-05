# Before class prep

Before class you need to have anaconda 3.7+ installed and download the course documents.

You should download the v1.01 tag of the course from this git repository.

# Installation

Before class starts we'll need to make sure that we're all on the same page. To do that we'll need
to install a few extra modules. On the command line of this folder execute:

Packages were create using:

`conda list -e > requirements_conda.txt`

To install create a new onda environment:

`conda create --name kphd`

Activate the environment:

`conda activate kphd`

Install the conda packages:

`conda install -c conda-forge --file requirements_conda.txt`

Next install the pip packages:

`pip install -r requirements_pip.txt`

After that, we can install data. The first bit is easy in the same folder execute:

`pip install -r requirements_data.txt`

After that we need to execute a script from the command line

`python requirements_nltk.py`
