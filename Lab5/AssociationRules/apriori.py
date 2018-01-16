from collections import Iterable
from copy import deepcopy
from functools import reduce
from itertools import combinations


class Apriori:
    @classmethod
    def calc(cls, data, min_sup, min_conf):
        itemset = cls.get_itemset(data)

        freq_itemset = cls.calc_freq_itemset(itemset, data, min_sup)
        rules = cls.calc_rules(freq_itemset, data, min_conf)

        return freq_itemset, rules

    @classmethod
    def calc_freq_itemset(cls, itemset, data, min_sup):
        print('Calculating frequent itemset...')
        k = 2
        itemset_old = []

        while True:
            print(f'Current itemset: {itemset}')
            itemset = cls.reduce_itemset(itemset, data, min_sup)

            if not itemset:
                break

            itemset_old = deepcopy(itemset)
            itemset = cls.subsets(itemset, k)
            itemset = cls.prune_itemset(itemset, itemset_old)

            k += 1

        return itemset_old

    @classmethod
    def calc_rules(cls, freq_itemset, data, min_conf):
        print('Calculating rules...')
        rules = []

        k = len(freq_itemset[0])
        while k > 1:
            for item in freq_itemset:
                subs = cls.subsets(item, k - 1)
                res = filter(lambda sub: cls.conf(item, sub, data) >= min_conf, subs)
                pairs = [(item - sub, sub, cls.conf(item, sub, data)) for sub in res]
                rules += pairs

            k -= 1
            print(f'Current rules: {rules}')

        return rules

    @classmethod
    def conf(cls, item, subset, data):
        support_item = cls.calc_support(item, data)
        support_sub = cls.calc_support(subset, data)

        return support_item / support_sub

    @classmethod
    def get_itemset(cls, data):
        items_set = reduce((lambda x, y: x.union(y)), data)
        items_list = [{item} for item in items_set]
        return items_list

    @classmethod
    def reduce_itemset(cls, itemset, data, min_sup):
        result = filter(lambda its: cls.calc_support(its, data) >= min_sup, itemset)

        return list(result)

    @classmethod
    def prune_itemset(cls, itemset_new, itemset_old):
        pruned = []
        for item in itemset_new:
            subs = cls.subsets(item, len(item) - 1)
            if all([sub in itemset_old for sub in subs]):
                pruned.append(item)

        return pruned

    @classmethod
    def calc_support(cls, item, data):
        item = {item} if type(item) is not set else item

        entries = sum([1 for tx in data if item.issubset(tx)])

        return entries / len(data)

    @classmethod
    def subsets(cls, itemset, length):
        elements = set()
        [elements.update(s) if isinstance(s, Iterable) else elements.update([s])
         for s in itemset]
        combis = [set(combo) for combo in combinations(elements, length)]

        return combis
