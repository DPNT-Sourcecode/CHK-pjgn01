from solutions.CHK.checkout_solution import CheckoutSolution

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
        # mostly from server deploy
        test_cases = [
            ["A", 50],
            ["B", 30],
            ["C", 20],
            ["D", 15],
            ["E", 40],
            ["F", 10],
            ["G", 20],
            ["H", 10],
            ["I", 35],
            ["J", 60],
            ["K", 80],
            ["L", 90],
            ["M", 15],
            ["N", 40],
            ["O", 10],
            ["P", 50],
            ["Q", 30],
            ["R", 50],
            ["S", 30],
            ["T", 20],
            ["U", 40],
            ["V", 50],
            ["W", 20],
            ["X", 90],
            ["Y", 10],
            ["Z", 50],
            ["AAAAAAAAAA", 400],
            ["EE", 80],
            ["EEB", 80],
            ["EEEB", 120],
            ["ABCDEABCDE", 280],
            ["CCADDEEBBA", 280],
            ["AAAAAEEBAAABB", 455],
            ["ABCDECBAABCABBAAAEEAA", 665],
            ["HHHHH", 45],  # 5H for 45
            ["HHHHHHHHHH", 80]  #10H for 80
            ["KK", 150] # 2K for 150 
            ["NMNN", 120] # 3N get one M free 
            ["PPPPP", 200] # 5P for 200
            [ ]
        ]

        for basket, expected in test_cases:
            assert CheckoutSolution().checkout(basket) == expected



