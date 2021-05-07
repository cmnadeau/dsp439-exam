import kmer
import pandas as pd
import math as mth
import os.path
import filecmp
import random
import string

def main():
    """
    Takes input file containing multiple sequences, and uses the kmer package to process sequences. Also outputs each sequences' dataframe to seperate files
    and computes complexity of each sequence.
    """
    print("Input file path:")
    path = input()
    str_contents = open(path, "r").read().split('\n')
    n=1
    for line in str_contents:
        if line != "" and checkInput(line, "DNA"):
            seq = kmer.kmer(line)
            df = seq.create_dataframe()
            cpl = df.iloc[-1,1]/df.iloc[-1,2]
            print("Complexity for string " + str(n) + " is: " + str(round(cpl,3)))
            print("-"*20)
            print(df)
            print("-"*20 + '\n')
            path='./results-seq'+str(n)+".txt"
            df.to_csv(path, index=False)
            n+=1



def checkInput(line, type="DNA"):
    """
    Checks a sequence of DNA or RNA bases. Default usage is for DNA
    Arguments are the sequence as a string and the type, which should be either DNA or RNA, and specified as a string
    """
    if type!= "DNA" and type !="RNA":
        print("Invalid Type")
        return False
    valid_chars_DNA=["A","G","T","C"]
    valid_chars_RNA=["A","G","U","C"]
    if type=="DNA":
        for char in line:
            if char not in valid_chars_DNA:
                print('\n')
                print("Invalid DNA Sequence")
                print('\n')

                return False
        return True
    elif type=="RNA":
        for char in line:
            if char not in valid_chars_RNA:
                print('\n')
                print("Invalid DNA Sequence")
                print('\n')
                return False
        return True



def test_input():
    assert checkInput(''.join(random.choice(["A","T","G","C","B"]) for i in range(10)) + "ATGC", "DNA") == False #test whether checkInput will filter based on DNA bases
    assert checkInput(''.join(random.choice(["A","T","G","C"]) for i in range(10)) + "ATCGU", "RNA") == False #check whether checkInput will filter based on DNA input for RNA
    assert checkInput(''.join(random.choice(["A","U","G","C"]) for i in range(10)) + "AUGC", "RNA") == True  #Check whether checkInput correctly identifies proper RNA sequence
    assert checkInput(''.join(random.choice(['A','T','G','C']) for i in range(10)) + "ATCG", "DNA") == True  #Check whether checkInput correctly identifies proper DNA sequence
def test_complexity():
    sequence = ''.join(random.choice(["A","T","G","C"]) for i in range(10))
    givenseq = "ATTTGGATT"
    gkmer = kmer.kmer(givenseq)
    gdf = gkmer.create_dataframe()
    assert round(gdf.iloc[-1,1]/gdf.iloc[-1,2],3) == 0.875 #Test complexity for given test case
if __name__ == "__main__":
    main()
