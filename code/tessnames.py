# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, print_function, division
import pandas as pd
from numpy.random import seed, choice
from numpy import loadtxt, floor

from itertools import islice, product


class nameYield():

    def __init__(self, inputnum):
        self.seedset = 0
        self.reset_seed()
        self.read_nounlist()
        n_nouns = self.nounlist.shape[0]
        self.read_adjectivelist()
        n_adjectives = self.adjectivelist.shape[0]
        self.sorted1 = choice(self.adjectivelist, n_adjectives,
                              replace=False, )
        self.reset_seed()
        self.sorted2 = choice(self.adjectivelist, n_adjectives,
                              replace=False, )
        self.reset_seed()
        self.sorted3 = choice(self.nounlist, n_nouns,
                              replace=False, )
        self.validate_inputnum(inputnum)
        self.inputnum = inputnum

        # # create the iterator object

        # combinations = product(range(n_adjectives),
        #                        range(n_adjectives), range(n_nouns))
        # combination = [x for x in islice(combinations,
        #                                  inputnum, inputnum + 1)][0]
        # self._word1 = self.sorted1[combination[0]]
        # self._word2 = self.sorted2[combination[1]]
        # self._word3 = self.sorted3[combination[2]]

        # refactor
        self._word3 = self.sorted3[int(inputnum % n_nouns)]
        self._word2 = self.sorted2[int(floor(inputnum / n_nouns %
            n_adjectives))]
        self._word1 = self.sorted1[int(floor(inputnum / n_nouns /
            n_adjectives % n_adjectives))]

    def phrase(self):
        return self._word1, self._word2, self._word3

    def read_nounlist(self):
        filename = '../data/nounlist.txt'
        self.nounlist = loadtxt(filename, dtype=str, )

    def read_adjectivelist(self):
        filename = '../data/adjectivelist.txt'
        self.adjectivelist = loadtxt(filename, dtype=str, )

    def validate_inputnum(self, inputmum):
        pass

    def reset_seed(self):
        if self.seedset == 0:
            self.seed = seed
            self.seed(8191)
            self.seedset = 1
        elif self.seedset == 1:
            self.seedset = 2
            self.seed(131071)
        elif self.seedset == 2:
            self.seedset = 3
            self.seed(524287)
        else:
            raise('too man loops')
