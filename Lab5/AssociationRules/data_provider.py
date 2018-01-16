from functools import reduce

FILENAME = 'groceries.txt'


class DataProvider:
    @classmethod
    def get_data(cls):
        data_text = cls.read_text_file()
        data_encoded, codes = cls.encode_data(data_text)
        data_minimized = cls.minimize_data(data_encoded)

        return data_minimized, codes

    @classmethod
    def read_text_file(cls):
        print('Parsing dataset...')
        with open(FILENAME) as file:
            lines = file.read().splitlines()
            lines_wo_ending = [line.strip('\\') for line in lines]
            items_per_line = [line.split(',') for line in lines_wo_ending]

            return items_per_line

    @classmethod
    def encode_data(cls, data):
        print('Encoding retrieved data')
        itemset = list(reduce((lambda tx1, tx2: set(tx1) | set(tx2)), data))
        data_encoded = [[itemset.index(item) for item in tx] for tx in data]

        return data_encoded, itemset

    @classmethod
    def minimize_data(cls, data):
        print('Minimizing retrieved data into sets')
        return [set(tx) for tx in data]
