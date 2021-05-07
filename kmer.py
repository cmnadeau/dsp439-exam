import pandas as pd
class kmer():
    """
    A class to process DNA sequences into kmer data
    Requires the Pandas library to function
    """
    def __init__(self, seq):
        """
        Init function for the kmer class
        Takes in the sequence
        Assumes valid input sequence; filtering taken care of in main function
        """
        self.seq = seq
    def get_seq(self):
        """
        Getter function for the kmer class
        """
        return self.seq
    def find_kmers(self, k):
        """
        Define a function to count kmers of size k, where k is specified as an argument
        """
        unique_kmers = []
        if k==1:
            for char in self.seq:
                if char not in unique_kmers:
                    unique_kmers.append(char)
            return len(unique_kmers)
        else:
            for i in range(0,len(self.seq)):
                if (len(self.seq[i:i+k]) == k) and (self.seq[i:i+k] not in unique_kmers):
                    unique_kmers.append(self.seq[i:i+k])
            return len(unique_kmers)
    def create_dataframe(self):
        """
        Define a function to create a pandas data frame containing all possible k and the associated
number of observed and expected kmers (see above table) for each sequence in the file
        """
        kmerdict = {'k':[],'Observed kmers':[],'Possible kmers':[]}
        if not len(self.seq) == 0: #Ignore empty lines
                for k in range(1,len(self.seq)+1):
                                  kmerdict['k'].append(str(k))
                                  kmerdict['Observed kmers'].append(self.find_kmers(k))
                                  kmerdict['Possible kmers'].append(min(len(self.seq)-k+1, 4 ** k))
                kmerdict['Observed kmers'].append(sum(i for i in kmerdict['Observed kmers']))
                kmerdict['Possible kmers'].append(sum(i for i in kmerdict['Possible kmers']))
                kmerdict['k'].append("Total:")
        return pd.DataFrame(kmerdict)
