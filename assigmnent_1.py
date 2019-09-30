import numpy as np
import matplotlib.pyplot as plt
import os
import argparse
import logging #impara ad usare
logging.basicConfig(level=logging.INFO)


_description = 'program that prints the relative frequence of each letter of the alphabet in the book.'

def process(file_path):
    "test di verifica"
    assert file_path.endswith('.txt')       #se una string finisce con una sottostringa
    assert os.path.isfile(file_path)        #se è un file che esiste

    "contest management: usciti dal blocco il file è automaticamente chiuso"
    logging.info('Opening file %s', file_path)
    with open(file_path) as input_file:
        data=input_file.read()
    logging.info('DOne %d character found.', len(data))


    "dictionary"
    letters='abcdefghijklmnopqrstuvxyz'
    freq_dict={}

    for ch in letters:
        freq_dict[ch]=0

    logging.info('Loop over the txt.')
    for ch in data.lower():
        '''
        try:
            frequency_dict[ch]+=1
        except KeyError:
            pass
        '''
        if ch in letters:
            freq_dict[ch]+=1
    #print (freq_dict)
    "normalizzare le occorrenze"
    num_characters = float(sum(freq_dict.values()))
    for ch in letters:
        freq_dict[ch]/=num_characters

    "print output"
    var=[]
    ff=[]
    for ch,freq in freq_dict.items():
        print('{}:{:.3f}%'.format(ch,freq * 100.))
        var.append(ch)
        ff.append(freq*100)
    var=np.asarray(var)
    ff=np.asarray(ff)
    plt.bar(var,ff)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = _description)
    parser.add_argument('infile', help = "path to imput file txt")
    args = parser.parse_args()
    process(args.infile)
    
