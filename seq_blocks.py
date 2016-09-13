
"""
function to give GC content
"""
def gc_cont(seq):
    numgc = seq.count('G') + seq.count('C')
    numgc /= len(seq)
    return numgc

"""
Write a function to divide sequence into blocks
"""
def gc_blocks(seq, block_size):
    myblocks = []
    length = len(seq)
    for i in range(0, length//block_size):

        block = seq[i*block_size:(i+1)*block_size]
        myblocks.append(gc_cont(block))

    return myblocks

"""
Function to take sequence, block size and threshold GC
"""
#def mapped_seq = gc_map(seq, block_size, gc_thresh)
