
price_table = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

# A supermarket checkout that calculates the total price of a number of items
class CheckoutSolution:

    def checkout(self, skus):
        if len(skus) == 0:
            return -1
        
        for item in skus:
            if item not in price_table:
                return -1
        



