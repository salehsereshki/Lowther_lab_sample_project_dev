#reusable pieces of code that were deleted from other scripts but might be useful later
#each block should have an identifier

#CA_1
#CA_1 Function to check if a genomic range overlaps with any ranges in the annotation dataframe
print(len(annot_df[(annot_df.Chromosome == chr) & (annot_df['Start'] < pos) & (annot_df['End'] > pos)]) > 0)
