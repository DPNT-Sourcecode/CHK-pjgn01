
from collections import defaultdict

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

discounts = { # items, discount
    'A': { 3: 20, 5: 50},
    'B': { 2: 15},
}

# A supermarket checkout that calculates the total price of a number of items
class CheckoutSolution:

    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        
        total = 0
        item_tally = defaultdict(int)
        
        for item in skus:
            if item == "":
                continue
            if item not in price_table:
                return -1
            
            total += price_table[item]
            item_tally[item] +=1

        if len(discounts) == 0:
            return total
        
        # apply any offers
        for item, item_count in item_tally.items():
            if item in discounts:
                offer_min, discount = discounts[item]

                while item_count >= offer_min:
                    total -= discount
                    item_count -= offer_min
        
        return total

