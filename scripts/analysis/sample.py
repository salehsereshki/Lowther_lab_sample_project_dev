import sys

AN = 'sample' #Analysis name.
VN = 'v1' # If the analysis is updated that with the same input gives different results, change the version number. and don't forget to git commit

# Read inputs from command line
sample_input1 = sys.argv[1]
sample_input2 = sys.argv[2]

print(AN, sys.argv)

#perform sample analysis



#write the processed data to data/processed/analysis_sample/
result.to_csv(f'./data/processed/analysis_{AN}/output_{VN}.tsv', sep='\t', index=False)
