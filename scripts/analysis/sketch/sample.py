#The analysis description in the header
#Author and date created i.e Saleh Sereshki, Oct 30 2023

#loading necessary libraries
import os
import pandas as pd
from scripts.IOmanager.add_resolver import get_file_name, get_git_mark, get_time_mark
from scripts.IOmanager.dt_loader import load_dt
import scripts.code_blocks.test_units as tu

AN = 'sample_sc' #sample sketch
GIT = get_git_mark()

config = {
    'threhold': 0.5,
}

output_plot = f'./output/plots/analysis/{AN}/'
output_tables = f'./output/tables/analysis/{AN}/'
#change the tables output if the analysis generates large tables
os.makedirs(output_plot, exist_ok=True)
os.makedirs(output_tables, exist_ok=True)

#load data adds
sample_dt = pd.read_csv(get_file_name('sample_data'), sep='\t')

#or load the data through the dt_loader
sample_dt = load_dt('sample_data', 'sample_input_reader')

#Test unit -> TU_1
assert tu.TU_1(sample_dt), "Test Unit TU_1 failed: sample_dt is empty"

#To get the number of genes look at code archive CA_1

#perform sample analysis
sample_dt['new_col'] = sample_dt['existing_col'] * config['threhold']

#running a command in bash in the middle of analysis:
import subprocess
cmd = ["athena", "annotate-bins", "--track-list", f'{config["output_folder"]}annotaions_ol_decision.txt', config['TAD_coords'],f'{config["output_folder"]}annotaions_tmp.bed']
subprocess.run(cmd)

#example running an R code in the middle of analysis:
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import numpy2ri, pandas2ri, default_converter
from rpy2.robjects.conversion import localconverter

with localconverter(default_converter + numpy2ri.converter):
    y_r = ro.conversion.py2rpy(y)
with localconverter(default_converter + pandas2ri.converter):
    X_r = ro.conversion.py2rpy(X)
ro.globalenv["X"] = X_r
ro.globalenv["y"] = y_r
ro.globalenv["best_lambda"] = ro.FloatVector([best_lambda])
ro.r("""
final_model <- glmnet(X, y, alpha = 0.5, family = "binomial", lambda = best_lambda)
coefs <- as.data.frame(as.matrix(coef(final_model)))
""")

##################################

#save results
sample_dt.to_csv(f'{output_tables}output1_{GIT}_{get_time_mark()}.tsv', sep='\t', index=False)


#generate plots
import matplotlib.pyplot as plt
plt.figure()
plt.hist(sample_dt['new_col'], bins=50)
plt.title('Histogram of new_col')
plt.xlabel('new_col values')
plt.ylabel('Frequency')
plt.savefig(f'{output_plot}hist_new_col_{GIT}_{get_time_mark()}.png')
plt.close()

#Or write a function in ./plotting/analysis_sample.py and call it here to generate plots
import scripts.plotting.analysis_sample as asp
asp.distribution_plot(sample_dt, 'new_col', f'{output_plot}hist_new_col_{GIT}_{get_time_mark()}.png')

