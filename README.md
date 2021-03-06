# DSP 439 Python Exam - Christopher Nadeau

## Files:
- kmer_test.py
- kmer.py
- seq.txt

## kmer_test
- Main code body
- Contains input for file as well as controls output
- Imports the kmer class for creation of individual dataframes for each sequence

### main
- Takes in an input file and iterates through an array that holds the sequences in the file
- Outputs the dataframe created using the `kmer` class
- Creates a csv file for each sequence in the given file containing sequences

### checkInput
- Given a string and the type of sequence, checks for the validity of either DNA or RNA

### test_input
- Generates random sequences to test checkInput for valid and invalid RNA/DNA sequences

### test_complexity
- Checks whether the `kmer` class creates a dataframe that can be used to compute the correct complexity.
NOTE: I could not find a way to incorporate randomness into this, as that would require a separate way of computing kmer complexity.


## kmer
This is the class definition for the `kmer` class. It is imported by the main file kmer_test.

### \_\_init__
Initiation function for the kmer class: takes a string as an argument and turns it into a kmer.

### get_seq
Basic getter function for the kmer class

Enables global access to self.seq, the input sequence

### find_kmers
This is a helper function, called by the function to create the output dataframe.

`find_kmers` takes as an argument the substring length currently being analyzed, and using the stored string from the initialization of the `kmer` class, determines the number of unique kmers detected in the input sequence

### create_dataframe
`create_dataframe` takes no arguments, using only the internally stored sequence given during the instantiation of the `kmer` class.

It begins by defining an empty dictionary object with the required columns `k`, `Observed kmers`, and `Possible kmers`. All of these are keys paired to empty arrays.

This function then loops through each possible substring length, 1 to the length of the given sequence, and appends the relevant values to each respective column's array.
After the conclusion of this loop, the function turns the created dictionary into a Pandas dataframe, and then returns that dataframe.
