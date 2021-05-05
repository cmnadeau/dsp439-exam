import pandas as pd
seq = "ATTTGGATT"


def find_kmers(seq, k):
    unique_kmers = []
    if k==1:
        for char in seq:
            if char not in unique_kmers:
                unique_kmers.append(char)
        return len(unique_kmers)
    else:
        for i in range(0,len(seq)):
            if (len(seq[i:i+k]) == k) and (seq[i:i+k] not in unique_kmers):
                unique_kmers.append(seq[i:i+k])
        return len(unique_kmers)
def create_df(seq):
    kmerdict = {'k':[],'Observed kmers':[],'Possible kmers':[]}
    if not len(seq)==0:
        for k in range(1,len(seq)+1):
            kmerdict['k'].append(k)
            kmerdict['Observed kmers'].append(find_kmers(seq,k))
            kmerdict['Possible kmers'].append(min(len(seq)-k+1,4**k))
    return pd.DataFrame(kmerdict)
print(create_df(seq))
