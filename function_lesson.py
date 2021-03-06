def ratio(x, y):
    """The ratio of 'x' to 'y'."""
    return x / y

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
    rev_comp = ''

    # Loop through and add new rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)

    return rev_comp


def answer_to_the_utlimate_question_of_life_the_universe_and_everything():
    return 42

def think_too_much():
    """Express Caesar had for Brutus."""

    print("""Yond Cassius has a lean and hungry look,
    He think_too_much.""")
