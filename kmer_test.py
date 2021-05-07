import kmer
import pandas as pd
import math as mth
import os.path

def main():
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



def test_answer():
    assert 1==1

if __name__ == "__main__":
    main()
