import random
import numpy as np
import math

OPTIONS = ("Welcome Page", "Example 1: Advertising Budget",
           "Example 2: Starbucks Operation", "Example 3: Corporate Valuation")


def get_break_even_prob(profit_item):

    # Probability of break-even = number of item > 0 / total number of items
    prob = 1.0

    return prob


def ad_calc_profit(price_item, cost_item, ad_budget):

    profit_item = []

    for i in range(len(price_item)):

        # Get all key factors
        unit_price = price_item[i]
        unit_cost = cost_item[i]
        sales_expense = 37000
        unit_sold = ad_budget*1000*0.7

        # Calculate total profit
        profit = unit_sold * (unit_price - unit_cost) - sales_expense
        print("------")
        print(f"unit sold: {unit_sold}")
        print(unit_price, unit_cost, profit)

        profit_item.append(profit)

    return profit_item


def get_items_ad_triangular(unit_price, unit_cost, N):

    price_item = np.random.triangular(size=N, left=unit_price-10.0, right=unit_price+10.0, mode=unit_price)
    cost_item = np.random.triangular(size=N, left=unit_cost-5.0, right=unit_cost+5.0, mode=unit_cost)

    return price_item, cost_item


def get_items(center, N):

    return np.random.normal(size=N, loc=center)


def apply_function(input_items, distribution = 'Uniform'):

    if distribution == 'Uniform':
        return np.sqrt(input_items + 1) * 2 + np.random.uniform(size=len(input_items), low=1, high=5)

    elif distribution == 'Poisson':
        return np.sqrt(input_items+1)*2 + np.random.poisson(size=len(input_items))

    elif distribution == 'Triangular':
        return np.sqrt(input_items + 1) * 2 + np.random.triangular(size=len(input_items), left=1, right=5, mode=2.5)