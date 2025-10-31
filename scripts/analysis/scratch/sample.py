#The analysis description in the header
#Author and date created i.e Saleh Sereshki, Oct 30 2023

#loading necessary libraries
import os
import pandas as pd
from scripts.IOmanager.add_resolver import get_file_name, get_git_mark, get_time_mark
from scripts.IOmanager.dt_loader import load_dt

AN = 'sample_sc' #sample scratch
GIT = get_git_mark()

config = {
    'threhold': 0.5,
}

output_plot = f'./output/plots/{AN}/'
output_tables = f'./output/tables/{AN}/'
#change the tables output if the analysis generates large tables
os.makedirs(output_plot, exist_ok=True)
os.makedirs(output_tables, exist_ok=True)



#load data adds
sample_dt = pd.read_csv(get_file_name('sample_data'), sep='\t')

#or load the data through the dt_loader
sample_dt = load_dt('sample_data', 'sample_input')

#Test unit -> TU_1

#To get the number of genes look at code archive CA_1

#perform sample analysis
sample_dt['new_col'] = sample_dt['existing_col'] * config['threhold']


#save results
sample_dt.to_csv(f'{output_tables}filtered-by-threh_{GIT}_{get_time_mark()}.tsv', sep='\t', index=False)

