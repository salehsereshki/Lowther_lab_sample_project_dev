#This file keeps all the test units, each test unit must have an identifier and a description

#TU_1
#TU_1 checks if all the genes are longer than 200 bases
def TU_1(annot_df):
    gene_lengths = annot_df['End'] - annot_df['Start']
    return all(gene_lengths > 200)
