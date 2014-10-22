'''
Created on Oct 19, 2014

@author: renato
'''

class Masks:

    def __init__(self):
        print 'lol'


    def convert_number_to_process_mask(self, num_processo):

        pos = [7,10,15,17,20]

        if len(num_processo) == 20:
            hash = num_processo
            hashlist = list(hash)

            for n in pos:
                hashlist.insert(n, '.')

            hash = ''.join(hashlist)
            return hash