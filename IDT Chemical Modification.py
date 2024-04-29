# https://www.idtdna.com/site/catalog/modifications/category/7
# https://www.neb.com/en-us/tools-and-resources/feature-articles/the-effect-of-nucleic-acid-modifications-on-digestion-by-dna-exonucleases
# https://www.idtdna.com/site/catalog/modifications/category/8
# https://www.idtdna.com/pages/education/decoded/article/an-aso-modification-that-enhances-nuclease-resistance-lowers-toxicity-and-increases-binding-affinity
# https://www.idtdna.com/pages/products/functional-genomics/antisense-oligos

fwd_primer = input("forward primer: ")
rev_primer = input("reverse primer: ")

# Phosphorothioate (PS) bonds modification
fwd_primer_PS = '*'.join(fwd_primer)
rev_primer_PS = '*'.join(rev_primer)

# Phosphorothioated 2' O-methyl bases modification
base_mapping = {'A': 'mA', 'T': 'T', 'G': 'mG', 'C': 'mC'}
# Replace bases using a list comprehension
fwd_primer_mPS = ''.join([base_mapping[base] + '*' if index != len(fwd_primer) - 1 else base_mapping[base] for index, base in enumerate(fwd_primer)])
rev_primer_mPS = ''.join([base_mapping[base] + '*' if index != len(rev_primer) - 1 else base_mapping[base] for index, base in enumerate(rev_primer)])

# Phosphorothioated Affinity Plus (locked nucleic acid) bases modification
base_mapping = {'A': 'A*', 'T': 'T*', 'G': 'G*', 'C': 'C*'}
num_bases_to_process = 20

# Process only the last 20 bases from 3'
fwd_primer_LNA_PS = ''.join([base_mapping[base] + '+' if index >= len(fwd_primer) - num_bases_to_process and index != len(fwd_primer) - 1 else base_mapping[base] for index, base in enumerate(fwd_primer)])
rev_primer_LNA_PS = ''.join([base_mapping[base] + '+' if index >= len(rev_primer) - num_bases_to_process and index != len(rev_primer) - 1 else base_mapping[base] for index, base in enumerate(rev_primer)])
fwd_primer_LNA_PS = fwd_primer_LNA_PS[:-1]
rev_primer_LNA_PS = rev_primer_LNA_PS[:-1]

# Add 2'-MOE modification to the entire primer
def modify_dna_sequence(sequence):
    modified_sequence = ""
    for index, base in enumerate(sequence):
        if index == 0:  # 5' base
            modified_sequence += "/52MOEr" + base + "/*"
        elif index == len(sequence) - 1:  # 3' base
            modified_sequence += "/32MOEr" + base + "/"
        else:  # Internal base
            modified_sequence += "/i2MOEr" + base + "/*"
    return modified_sequence

fwd_primer_MOE_PS = modify_dna_sequence(fwd_primer)
rev_primer_MOE_PS = modify_dna_sequence(rev_primer)

# Place order using ASO page in IDT website will be much cheaper
print(f"\nforward primer with PS:\n{fwd_primer_PS}")
print(f"reverse primer with PS:\n{rev_primer_PS}")
print(f"\nforward primer with 2'MOE:\n{fwd_primer_MOE_PS}")
print(f"reverse primer with 2'MOE:\n{rev_primer_MOE_PS}")
print(f"\nforward primer with 2'O-methyl and PS:\n{fwd_primer_mPS}")
print(f"reverse primer with 2'O-methyl and PS:\n{rev_primer_mPS}")
print(f"\nforward primer with LNA and PS:\n{fwd_primer_LNA_PS}")
print(f"reverse primer with LNA and PS:\n{rev_primer_LNA_PS}")

