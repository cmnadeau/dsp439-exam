import kmer
import pandas as pd
import os.path

def main():
    print("Input file path:")
    path = input()
    str_contents = open(path, "r").read().split('\n')
    for line in str_contents:
        if line != "":
            seq = kmer.kmer(line)
            print(seq.create_dataframe())
            print("-"*20)

def test_answer():
    x=2
    assert x+1 == 3

if __name__ == "__main__":
    main()
