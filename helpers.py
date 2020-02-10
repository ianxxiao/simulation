import random
import numpy as np
import math

OPTIONS = ("Welcome Page", "Example 1: Starbucks Operation",
           "Example 2: Advertising Budget", "Example 3: Corporate Valuation")

def get_items(center, N):

    return np.random.normal(size=N, loc=center)


def apply_function(input_items, distribution = 'Uniform'):

    if distribution == 'Uniform':
        return np.sqrt(input_items + 1) * 2 + np.random.uniform(size=len(input_items), low=1, high=5)

    elif distribution == 'Poisson':
        return np.sqrt(input_items+1)*2 + np.random.poisson(size=len(input_items))

    elif distribution == 'Triangular':
        return np.sqrt(input_items + 1) * 2 + np.random.triangular(size=len(input_items), left=1, right=5, mode=2.5)