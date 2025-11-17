from solutions.CHK.checkout_solution import CheckoutSolution, price_table

class TestCheckout():
    def test_empty_basket(self):
        assert CheckoutSolution().checkout("") == 0

    def test_invalid_item(self):
        assert CheckoutSolution().checkout('-') == -1

    def test_one_of_each(self):
        basket = 'ABCDE'
        assert CheckoutSolution().checkout(basket) == 155

    def test_A_offer_1(self):
        basket = 'AAAA'     # 3A for 130 + 50

        assert CheckoutSolution().checkout(basket) == 180

    def test_A_offer_2(self):
        basket = 'AAAAAA'   # 5A for 200 + 50
        assert CheckoutSolution().checkout(basket) == 250

    def test_A_offer_3(self):
        basket = 'AAAAA'    # 5A for 200
        basket = basket + 'AAA' # 3A for 130,
        basket = basket + 'A' # 50 
        assert CheckoutSolution().checkout(basket) == 380

    def test_B_offer_twice(self):
        basket = 'BBBB'     # (2B for 45) * 2
        assert CheckoutSolution().checkout(basket) == 90

    def test_3_of_everything(self):
        basket = 'AAA' # 3A for 130
        basket = basket + 'BBB' # 2B for 45+30 = 75
        basket = basket + 'CCC' # 20 * 3 = 60
        basket = basket + 'DDD' # 15 * 3 = 45
        basket = basket + 'EEE' # 40 * 3 = 120, plus get one B free so -30
        assert CheckoutSolution().checkout(basket) == 400

    def test_free_items(self):
        basket = 'EEEEBB' # 40 * 4  (2E get one B free)
        assert CheckoutSolution().checkout(basket) == 160

    def test_free_items2(self):
        basket = 'BEBEEE' # 40 * 4. (2E get one B free)
        assert CheckoutSolution().checkout(basket) == 160

    def test_free_items3(self):     
        basket = 'ABCDEABCDE' # 'ABCDE' = 155, 155*2 - 30   (2E get one B free)
        assert CheckoutSolution().checkout(basket) == 280

    def test_buy_two_get_one_free(self):
        basket = 'FFF'  # 2F get one F free 
        assert CheckoutSolution().checkout(basket) == 20

    def test_quick_test_cases(self):
        # test cases from server deploy
        test_cases = [
            ["AAAAAAAAAA", 400],
            ["EE", 80],
            ["EEB", 80],
            ["EEEB", 120],
            ["ABCDEABCDE", 280],
            ["CCADDEEBBA", 280],
            ["AAAAAEEBAAABB", 455],
            ["ABCDECBAABCABBAAAEEAA", 665],
        ]

        for basket, expected in test_cases:
            assert CheckoutSolution().checkout(basket) == expected

    def test_prices(self):
        for item, price in price_table.items():
            assert CheckoutSolution().checkout(item) == price

    def test_discount_offers(self):
        test_cases = [
            # 5H for 45, 10H for 80
            ["HHHHH", 45],
            ["HHHHHHH", 65],
            ["HHHHHHHHHH", 80], # 10H
            ["HHHHHHHHHHHH", 100], # 12H
            ["HHHHHHHHHHHHHHH", 125], # 15H

            # 3N get one M free 
            ["NNN", 120], 
            ["NMNN", 120], 
            ["NMNMN", 135], 

            ["KK", 120], # 2K for 120   
            ["PPPPP", 200], # 5P for 200
            ["QQQ", 80], # 3Q for 80 

            # 3R get one Q free
            ["RRQR", 150], 
            ["RRQRRRQRRRQR", 450],
            ["RRRQQQ", 210],
            ["RRRQQQQ", 230], # plus 3Q for 80
                     
            ["UUUU", 120], # 3U get one U free 

            # 2V for 90, 3V for 130
            ["VV", 90], 
            ["VVV", 130], 
            ["VVVV", 180], 
            ["VVVVV", 220], 
            ["VVVVVV", 260], 
        ]

        for basket, expected in test_cases:
            assert CheckoutSolution().checkout(basket) == expected

    def test_bundle_offers(self):
        test_cases = [
            ["STX", 45],
            ["STY", 45],
            ["STZ", 45],
            ["XYZ", 45],
            ["XYZS", 62], # 45 + 17
            ["XYZSY", 82], # 45 + 17 + 20
            ["XYZSYY", 90]
        ]

        for basket, expected in test_cases:
            assert CheckoutSolution().checkout(basket) == expected