
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
        
        # apply freebie offers first
        for item in freebies:
            if item not in item_tally:
                continue

            offers_for_item = sorted(freebies[item].items(), key=lambda x: x[0], reverse=True)
            item_count = item_tally[item]

            for offer_min, free_items in offers_for_item:
                while item_count >= offer_min:
                    for free_item in free_items:
                        if free_item in skus:
                            total -= price_table[free_item]
                            item_tally[free_item] -= 1
                        else:
                            skus = skus + free_items
                    item_count -= offer_min


        # apply eligible discounts
        for item, item_count in item_tally.items():
            if item in discounts:
                offers = sorted(discounts[item].items(), key=lambda x: x[0], reverse=True)

                for offer_min, discount in offers:
                    while item_count >= offer_min:
                        total -= discount
                        item_count -= offer_min
    
    
        return total

