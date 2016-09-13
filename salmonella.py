def fasta_to_string():

    with open('data/salmonella_spi1_region.fna', 'r') as f:

        """Print file to string with no space"""
        salseq = ''

        counter = 0
        for line in f:
            if counter != 0:
                salseq += line.rstrip()

            else:
                counter = 1

    return (salseq)
