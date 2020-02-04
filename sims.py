import math
class AdSim():

    def __init__(self):
        print("setting up advertising class")
        self.ad_budget = 40000
        self.price = 36.0
        self.cost = 31.0
        self.seasonal_var = {"Q1": {
                        "unit_sold_adj": 0.9,
                        "sales_overhead": 8000},
            "Q2": {
            "unit_sold_adj": 1.1,
            "sales_overhead": 8000},
            "Q3": {
                "unit_sold_adj": 0.8,
                "sales_overhead": 9000},
            "Q4": {
                "unit_sold_adj": 1.2,
                "sales_overhead": 9000}
                        }

    def run_sim(self):

        unit_sales = 35 * self.seasonal_var['Q1']['unit_sold_adj'] * math.sqrt(3000 + self.ad_budget)

        print("running simulation ...")
        print(f'expected unit sales ${unit_sales:.2f}')

    def _set_budget(self, new_budget):
        print(f'setting new advertising budget to ${new_budget}')
        self.ad_budget = new_budget