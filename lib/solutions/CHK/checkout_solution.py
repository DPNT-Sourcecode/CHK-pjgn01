
from collections import defaultdict
from .data import price_table, discounts, freebies, three_for_n_bundles


# A supermarket checkout that calculates the total price of a number of items
class CheckoutSolution:

    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        if len(skus) == 0: # basket is empty
            return 0
        
        total = 0
        item_tally = defaultdict(int)

        # get total price without offers
        for item in skus:
            if item not in price_table:
                return -1
            
            total += price_table[item]
            item_tally[item] +=1
        
        # apply group discount offers first
        for (eligible_items, offer_price) in three_for_n_bundles:
            if len(skus) < 3:
                continue

            eligible_basket_items = 0
            for item in eligible_items:
                eligible_basket_items += item_tally[item]
            
            while eligible_basket_items >= 3: 
                bundle_items = ""
                for item in eligible_items:
                    if item in item_tally and item_tally[item] > 0:
                        bundle_items += item

                    if len(bundle_items) == 3:
                        total += offer_price

                        for bundle_item in bundle_items:
                            total -= price_table[bundle_item]
                            item_tally[bundle_item] -= 1
                        
                        bundle_items = ""
                        eligible_basket_items = 0

                for item in eligible_items:
                    eligible_basket_items += item_tally[item]

        # apply freebie offers
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






