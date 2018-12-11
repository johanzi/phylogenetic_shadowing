#!/usr/bin/python
import sys

#Written by Johan Zicola, 15/06/2016

#Function to call if '-h' is given
def usage():
    print sys.argv[0],"[-h] <input.file>"
    print '''
    Reads a clustal omega file and prepare a input file for BOXSHADE (http://www.ch.embnet.org/software/BOX_form.html) analysis

    
    -h              print this message

    <input.file>      the file has to be in clustal format

    Example:
    python clustalOmega2BoxShade.py <input.file> > <output.file>
    
    NB: In order to make BoxShade work, the name of each sequence should not contain more than 16 characters and should not contain spaces
    
    '''

def parseClustal(file):
    seqs = {} #Initialize dictionary
    with open(file) as f:
        f.next() #Skip first line
        f.next() #Skip second line
        for line in f:
            line = line.partition('*')[0] #remove lines starting with *
            line = line.rstrip() #strip empty lines
            if line.rstrip():
                data = line.strip().split() #Split line in two elements separated by spaces
                seqID = data[0] #Species is the key
                seq = data[1] #Sequence is the value
                if not seqs.has_key(seqID): #Check of the dictionary has already the key
                    seqs[seqID] = seq #if not, create a new key
                else: #If yes
                    seqs[seqID] += seq #append the sequence to the existing key
               
    for seqID, seq in seqs.items():
        print ">" + seqID    #Print the key with '>' prefix
        print ''.join(seq.split()) #Print the joined sequences matching with the same key and remove separators

if len(sys.argv) == 1 or  sys.argv[1] == '-h':
    usage()
else:
    parseClustal(sys.argv[1]) #Call the function


