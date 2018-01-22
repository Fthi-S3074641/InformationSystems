from copy import deepcopy
from itertools import combinations

import numpy as np
from functools import reduce


class Apriori:
    @classmethod
    def calc(cls, data, min_sup, min_conf):
        freq_itemset = cls.calc_freq_itemset(data, min_sup)
        rules = cls.calc_rules(freq_itemset, data, min_conf)

        return freq_itemset, rules

    @classmethod
    def calc_freq_itemset(cls, data, min_sup):
        print('Calculating frequent itemset...')
        itemset = range(0, data.shape[1])

        k = 2
        itemset_old = []

        while True:
            print(f'Current itemset - Itemset : {itemset}')
            itemset = cls.reduce_itemset(itemset, data, min_sup)

            if not itemset:
                break

            itemset_old = deepcopy(itemset)
            itemset = cls.subsets(itemset, k)

            if k > 2:
                itemset = cls.prune_itemset(itemset, itemset_old)

            k += 1

        return itemset_old

    @classmethod
    def calc_rules(cls, freq_itemset, data, min_conf):
        print('Calculating rules...')
        rules = []

        # If the frequent itemset consists of only single items, return no rules
        if type(freq_itemset[0]) is int:
            return rules

        k = len(freq_itemset[0])
        while k > 1:
            for item in freq_itemset:
                subs = cls.subsets(item, k - 1)
                res = filter(lambda sub: cls.conf(item, sub, data) >= min_conf, subs)
                pairs = [(set(item) - set(sub), sub, cls.conf(item, sub, data))
                         for sub in res]
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
    def calc_support(cls, itemset, data):
        # If there's only a single element in the itemset
        if type(itemset) is int:
            return sum(data[:, itemset]) / data.shape[0]

        entries = np.sum(np.all(data[:, itemset], axis=1))

        return entries / data.shape[0]

    @classmethod
    def subsets(cls, itemset, length):
        if length > 2 and type(itemset) is list:
            itemset = reduce(lambda x, y: set(x).union(set(y)), itemset)

        return combinations(itemset, length)
