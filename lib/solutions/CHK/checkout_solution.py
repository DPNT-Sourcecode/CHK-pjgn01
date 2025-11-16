
from collections import defaultdict

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

offers = {
    'A': (3, 130),
    'B': (2, 45),
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
            
            item_tally[item] +=1

        for item, count in item_tally.items():
            total += price_table[item]

        return total



