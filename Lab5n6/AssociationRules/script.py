from Lab5.AssociationRules.apriori import Apriori
from Lab5.AssociationRules.data_provider import DataProvider
from Lab5.AssociationRules.printer import Printer


def print_result(freq_itemset, rules, codes):
    print(f'Frequent Itemsets:')
    print([(', ').join([codes[e] for e in s]) for s in freq_itemset])
    print('Rules: Antecedent -> Consequence : Confidence')
    [print_rule(codes, r) for r in rules]


def print_rule(codes, rule):
    consequence = (', ').join([codes[e] for e in rule[0]])
    antecedent = (', ').join([codes[e] for e in rule[1]])
    confidence = rule[2]

    print(f'\t{antecedent} -> {consequence} : {confidence:.3f}')


if __name__ == '__main__':
    support = 0.001
    confidence = 0.8

    data, codes = DataProvider.get_data()
    Printer.print_histogram(data)
    # freq_itemset, rules = Apriori.calc(data, support, confidence)
    # print_result(freq_itemset, rules, codes)
