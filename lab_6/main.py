from argparse import ArgumentParser
import time
import sympy


class HashRecord:
    def __init__(self, key):
        self.key = key


class HashTable:

    def __init__(self, hash_table_size):
        self.hash_table_size = hash_table_size
        self.hash_table_entry = [None for _ in range(self.hash_table_size)]
        self.collision_number = 0
        self.calculate_hash_count = 0
        self.try_number = 0

    def hash_djb2(self, word):
        init_hash = 5381
        for char in word:
            init_hash = ((init_hash << 5) + init_hash) + ord(char)

        return init_hash % self.hash_table_size

    # Tips for second and final hashes from CLRS
    def second_hash(self, word_hash):
        return (word_hash % (self.hash_table_size - 1)) + 1

    def final_hash(self, word, try_number):
        word_hash = self.hash_djb2(word)
        return (word_hash + try_number * self.second_hash(word_hash)) % self.hash_table_size

    def add(self, word):
        word_hash = self.hash_djb2(word)

        self.calculate_hash_count += 1
        if self.hash_table_entry[word_hash] is None:
            self.hash_table_entry[word_hash] = HashRecord(word)
        else:
            self.try_number = 0
            self.collision_number += 1
            while self.hash_table_entry[word_hash] is not None:
                # print(word)
                self.try_number += 1
                word_hash = self.final_hash(word, self.try_number)
                if self.try_number > self.hash_table_size:
                    raise OverflowError('Not enough space in the table')
            self.hash_table_entry[word_hash] = HashRecord(word)
            self.calculate_hash_count += self.try_number

    def find(self, word):
        word_hash = self.hash_djb2(word)
        if self.hash_table_entry[word_hash] is None:
            return False, -1
        else:
            self.try_number = 0
            while self.hash_table_entry[word_hash].key != word:
                self.try_number += 1
                if self.try_number > self.hash_table_size:
                    return False, -1
                word_hash = self.final_hash(word, self.try_number)
            return True, self.try_number


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--table_size',
        type=int,
        default=700000,
        help='The size of hash table'
    )
    parser.add_argument(
        '--path_to_dict',
        type=str,
        default='large_dict.txt',
        help='Path to dictionary with words for hash table'
    )

    return parser.parse_args()


def main():
    start_time = time.time()
    args = parse_arguments()
    with open(args.path_to_dict, 'r') as file:
        words = file.read().rstrip().split()
    hash_table_size = sympy.nextprime(args.table_size)
    hash_table = HashTable(hash_table_size)
    print('We generate hash table with {} entries'.format(hash_table_size))
    for idx, word in enumerate(words):
        hash_table.add(word)
    print('Collisions number: ', hash_table.collision_number)
    print('We calculated hash function: {} times'.format(hash_table.calculate_hash_count))
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
