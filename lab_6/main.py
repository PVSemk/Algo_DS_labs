from argparse import ArgumentParser
import time
import hashlib
import os

class HashRecord:
    def __init__(self, key):
        self.key = key


class HashTable:

    def __init__(self, hash_table_size, use_djb2):
        self.hash_table_size = hash_table_size
        self.hash_table_entry = [None for _ in range(self.hash_table_size)]
        self.collision_number = 0
        self.calculate_hash_count = 0
        self.try_number = 0
        self.use_djb2 = use_djb2

    def hash_djb2(self, word):
        init_hash = 5381
        for char in word:
            init_hash = ((init_hash << 5) + init_hash) + ord(char)

        return init_hash % self.hash_table_size

    def hash_md5(self, word):

        hash_value = hashlib.md5(word.encode())
        return int(hash_value.hexdigest(), 16) % self.hash_table_size

    def default_hash(self, word):
        return hash(word) % self.hash_table_size

    def add(self, word):
        word_hash = self.hash_djb2(word) if self.use_djb2 else self.hash_md5(word)

        self.calculate_hash_count += 1
        if self.hash_table_entry[word_hash] is None:
            self.hash_table_entry[word_hash] = HashRecord(word)
        else:
            self.try_number = 0
            self.collision_number += 1
            while self.hash_table_entry[word_hash] is not None:
                # print(word)
                self.try_number += 1
                word_hash = self.hash_djb2(word + str(self.try_number)) if self.use_djb2 else self.hash_md5(word + str(self.try_number))
                if self.try_number > self.hash_table_size:
                    raise OverflowError('Not enough space in the table')
            self.hash_table_entry[word_hash] = HashRecord(word)
            self.calculate_hash_count += self.try_number

    def find(self, word):
        word_hash = self.hash_djb2(word) if self.use_djb2 else self.hash_md5(word)
        if self.hash_table_entry[word_hash] is None:
            return False, -1
        else:
            self.try_number = 0
            while self.hash_table_entry[word_hash].key != word:
                self.try_number += 1
                if self.try_number > self.hash_table_size:
                    return False, -1
                word_hash = self.hash_djb2(word + str(self.try_number)) if self.use_djb2 else self.hash_md5(word + str(self.try_number))
            return True, self.try_number


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--table_size',
        default=700000,
        type=int,
        help='Size of hash table which will be created'
    )
    parser.add_argument(
        '--path_to_dict',
        type=str,
        default='large_dict.txt',
        help='Path to dictionary with words for hash table'
    )
    parser.add_argument(
        '--use_djb2',
        type=bool,
        default=True,
        help='Use djb2 hash function or md5 hash in hasqh table'
    )

    return parser.parse_args()


def main():
    a = 'road'
    if a != 'road':
        pass
    start_time = time.time()
    args = parse_arguments()
    with open(args.path_to_dict, 'r') as file:
        words = file.read().rstrip().split()
    hash_table = HashTable(args.table_size, args.use_djb2)
    for idx, word in enumerate(words):
        hash_table.add(word)
    print('Collisions number: ', hash_table.collision_number)
    print('We calculated hash funtion: {} times'.format(hash_table.calculate_hash_count))
    print('Total taken time for generating table: {:.5f}'.format(time.time() - start_time))
    while True:
        word_to_search = input('Please, enter word to search in table (or q for exit): ')
        if word_to_search == 'q':
            break
        search_time = time.time()
        result = hash_table.find(word_to_search)
        print('The word was found, we needed to calculate hash {} extra times to find the word'.format(result[1])) if result[0] else print('The word wasn\'t found')
        print('It took {:.5f} to find the word'.format(time.time() - search_time))
if __name__ == '__main__':

    main()
