#!/usr/bin/env python3
def revcomp():
    seq=input()
    assert type(seq)==str, "The sequence you entered is not a string"
    seq=list(seq)
    bases=['A','G','C','T','a','g','c','t']
    for i in range(len(seq)):
        assert seq[i] in bases, "\nThe sequence you entered is invalid.\nYour sequence may only contain A, G, C, and T characters (case insensitive) and no spaces."
    output=[]
    leng=len(seq)
    for i in range(len(seq)):
        if seq[leng-1] in ['A','a']:
            output.append('T')
        elif seq[leng-1] in ['G','g']:
            output.append('C')
        elif seq[leng-1] in ['C','c']:
            output.append('G')
        else:
            output.append('A')
        leng-=1
    print('\n\nReverse complement:\n'+''.join(output))
revcomp()
