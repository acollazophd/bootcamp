def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid Material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a nucleic acid sequence."""

    # Initialize empty string
    rev_comp = seq[::-1]

    # Loop through and add new rev comp bases
    rev_comp=rev_comp.replace('G', 'c')
    rev_comp=rev_comp.replace('C', 'g')
    rev_comp=rev_comp.replace('A', 't')
    rev_comp=rev_comp.replace('T', 'a')


    return rev_comp.upper()
