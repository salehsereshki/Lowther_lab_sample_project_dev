import sys
import argparse

AN = 'sample' #Analysis name.
VN = 'v1' # If the analysis is updated that with the same input gives different results, change the version number. and don't forget to git commit

# Read inputs from command line
parser = argparse.ArgumentParser()
parser.add_argument('-g','--gene_list',help='A text file, One gene name per line', required=True)
parser.add_argument('-t','--threshold',default='0.05',help='FDR threshold for significance') #It is not required, default is 0.05
args = parser.parse_args()
gene_list_add = args.gene_list
threshold = args.threshold

print(AN, sys.argv)

#perform sample analysis



#write the processed data to data/processed/analysis/
result.to_csv(f'./data/processed/analysis_{AN}/output_{VN}.tsv', sep='\t', index=False)
