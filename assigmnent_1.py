import os
import argparse
import logging #impara ad usare
import time
import re
import numpy as np
import matplotlib.pyplot as plt
logging.basicConfig(level=logging.INFO)


_description = 'program that prints the relative frequence of each letter of the alphabet in the book.'

def process(file_path):
    #test di verifica
    assert file_path.endswith('.txt')       #se una string finisce con una sottostringa
    assert os.path.isfile(file_path)        #se è un file che esiste

    #contest management: usciti dal blocco il file è automaticamente chiuso
    logging.info('Opening file %s', file_path)
    with open(file_path) as input_file:
        data = input_file.read()
    logging.info('Done.')         #: %d character found.', len(data))

    #prepare a dictionary and initialize to zero.
    letters = 'abcdefghijklmnopqrstuvxyz'
    freq_dict = {}

    for ch in letters:
        freq_dict[ch] = 0

    logging.info('Loop over the .txt')
    for ch in data.lower():
        '''
        try:
            frequency_dict[ch]+=1
        except KeyError:
            pass
        '''
        if ch in letters:
            freq_dict[ch] += 1
    #print (freq_dict)
    #normalizzare le occorrenze
    num_characters = float(sum(freq_dict.values()))
    for ch in letters:
        freq_dict[ch] /= num_characters

    #prepare list for printing [var,ff]
    x = []
    y = []

    #print output
    print('Relative frequence of each letters.')
    for ch, freq in freq_dict.items():
        print('{}:{:.3f}%'.format(ch, freq * 100.))
        x.append(ch)
        y.append(freq*100)

    #optional display histogram
    if args.histogram != None:
        logging.info('Display the histogram of the frequencies ')
        plt.title('Bar plot of frequencies')
        plt.ylabel('Frequencies')
        plt.bar(x, y)
        plt.show()
        logging.info('Done.')

    #print out the basic book stats
    if args.counting != None:
        logging.info('Printing stats')
        n_ch = len(data)
        n_words = len(re.findall(r'\w+', data))
        with open(file_path) as input_file:
            n_lines = input_file.read().count('\n')
        print ('Number of: characters: {}, words: {}, lines: {}'.format(n_ch,n_words, n_lines))
        logging.info('Done.')

    logging.info('Process function ended.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = _description)
    parser.add_argument('-i', '--input', help='path to imput file')
    parser.add_argument('-hist', '--histogram', help='Do you want to to display a histogram of the frequencies? Answare: yes o no')
    parser.add_argument('-count', '--counting', help='Do you want print out the book stats? Answare: yes o no')
    args = parser.parse_args()
    start = time.time()
    process(args.input)
    end = time.time()
    elasped = end - start
    print('Total elasped time: {} s'.format(elasped))
