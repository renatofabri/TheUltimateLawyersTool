'''
Created on Oct 19, 2014

@author: renato
'''

class Masks:

    def __init__(self):
        pass


    def convert_number_to_process_mask(self, num_processo):
        '''
        TODO: add method description
        '''
        pos = [7,10,15,17,20]

        if len(num_processo) == 20:
            hash_number = num_processo
            hashlist = list(hash_number)

            for n in pos:
                hashlist.insert(n, '.')

            hash_number = ''.join(hashlist)
            return hash_number