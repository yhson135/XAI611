# How to run

### Pretraining dataset
main_PCQM4.py   
--train_subset: Whether to use only fraction of train data  
--gnn: gin-virtual or gru  

### Finetuning dataset
main_bbbp.py
train/val/test dataset is already in the folder.

## Colab Installing Example
### There was a problem when intalling ogb before the torch-geometry. Please install in order by torch-geometry > rdkit > ogb   

import os

import torch

os.environ['TORCH'] = torch.__version__

print(torch.__version__)

!pip install -q torch-scatter -f https://data.pyg.org/whl/torch-${TORCH}.html 

!pip install -q torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}.html 

!pip install -q git+https://github.com/pyg-team/pytorch_geometric.git 



!pip install rdkit-pypi

!pip install ogb

