''' The GC-content of a DNA string is given by the percentage of symbols in the string 
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. 
Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format. In this format,
the string is introduced by a line that begins with '>', 
followed by some labeling information. Subsequent lines contain the string itself; 
the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the
ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
'''
DNA = input("enter your DNA string: ")
count_C = 0
count_G = 0
for i in range(len(DNA)):  
    if DNA[i] == "G" :
        count_G += 1
    elif DNA[i] == "C" :
        count_C += 1
        
result = (count_G + count_C )/ len(DNA) * 100 
 
 
 



