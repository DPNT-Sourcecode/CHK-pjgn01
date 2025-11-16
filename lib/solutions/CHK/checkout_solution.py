
from collections import defaultdict

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

discounts = { # num of items, discount
    'A': { 3: 20, 5: 50},
    'B': { 2: 15},
}

freebies = {  # num of items, free item
    'E': { 2: 'B'}
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
                n = item_count
                offers = sorted(discounts[item].items(), key=lambda x: x[0], reverse=True)

                for offer_min, discount in offers:
                    while n >= offer_min:
                        total -= discount
                        n -= offer_min

            if item in freebies:
                n = item_count
                freebie_offers = sorted(freebies[item].items(), key=lambda x: x[0], reverse=True)
        
                for offer_min, free_items in freebie_offers:
                    while n >= offer_min:
                        for free_item in free_items:
                            if free_item in skus:
                                total -= price_table[free_item]
                            else:
                                skus = skus + free_items
                        n -= offer_min

    
        return total



