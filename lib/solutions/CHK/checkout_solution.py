
from collections import defaultdict

price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}

discounts = { # num of items, discount
    'A': { 3: 20, 5: 50},
    'B': { 2: 15},
    'H': { 5: 5, 10: 20},
    'K': { 2: 10},
    'P': { 5: 50},
    'Q': { 3: 10},
    'V': { 2: 10, 3: 20}
}

freebies = {  # num of items, free item
    'E': { 2: 'B'},
    'F': { 3: 'F'},
    'N': { 3, 'M'},
    'R': { 3: 'Q'},
    'U': { 4: 'U'},
}

# A supermarket checkout that calculates the total price of a number of items
class CheckoutSolution:

    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        if len(skus) == 0: # basket is empty
            return 0
        
        total = 0
        item_tally = defaultdict(int)
        
        for item in skus:
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

            freebies_for_item = sorted(freebies[item].items(), key=lambda x: x[0], reverse=True)
            item_count = item_tally[item]

            for offer_min, free_items in freebies_for_item:
                while item_count >= offer_min: # apply offer multiple times if applicable
                    for free_item in free_items:
                        if free_item in skus:
                            total -= price_table[free_item]
                            item_tally[free_item] -= 1
                    item_count -= offer_min


        # apply eligible discounts
        for item in discounts:
            if item not in item_tally:
                continue

            offers = sorted(discounts[item].items(), key=lambda x: x[0], reverse=True)
            item_count = item_tally[item]

            for offer_min, discount in offers:
                while item_count >= offer_min:
                    total -= discount
                    item_count -= offer_min
    
        return total


