
from collections import defaultdict

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

offers = { # items, discount
    'A': (3, 20),
    'B': (2, 15),
}

# A supermarket checkout that calculates the total price of a number of items
class CheckoutSolution:

    def checkout(self, skus):
        if len(skus) == 0:
            return -1
        
        total = 0
        item_tally = defaultdict(int)
        
        for item in skus:
            if item not in price_table:
                return -1
            
            total += price_table[item]
            item_tally[item] +=1

        for item, item_count in item_tally.items():
            if item in offers:
                offer_min, discount = offers[item]

                while item_count > offer_min:
                    total -= discount
                    item_count -= offer_min
        

        return total
