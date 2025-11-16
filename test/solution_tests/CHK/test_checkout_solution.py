from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_empty_basket(self):
        assert CheckoutSolution().checkout("") == 0

    def test_invalid_item(self):
        assert CheckoutSolution().checkout('Z') == -1

    def test_one_of_each(self):
        basket = 'ABCDE'
        assert CheckoutSolution().checkout(basket) == 155

    def test_A_offer_1(self):
        basket = 'AAAA'
        # 3A for 130 + 50
        assert CheckoutSolution().checkout(basket) == 180

    def test_A_offer_2(self):
        basket = 'AAAAA'
        # 3A for 130 + 50
        assert CheckoutSolution().checkout(basket) == 180

    def test_B_offer_twice(self):
        basket = 'BBBB'
        # (2B for 45) * 2
        assert CheckoutSolution().checkout(basket) == 90

    def test_3_of_everything(self):
        basket = 'AAA' # 3A for 130
        basket = basket + 'BBB' # 2B for 45+30 = 75
        basket = basket + 'CCC' # 20 * 3 = 60
        basket = basket + 'DDD' # 15 * 3 = 45
        assert CheckoutSolution().checkout(basket) == 310
