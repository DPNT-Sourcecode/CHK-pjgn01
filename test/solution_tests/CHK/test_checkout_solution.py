from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_empty_basket(self):
        assert CheckoutSolution().checkout([]) == -1

    def test_invalid_item(self):
        assert CheckoutSolution().checkout(['Z']) == -1

    def test_one_of_each(self):
        basket = ['A', 'B', 'C', 'D']
        assert CheckoutSolution().checkout(basket) == 115

    def test_A_offer_once(self):
        basket = ['A', 'A', 'A', 'A']
        # 3A for 130 + 50
        assert CheckoutSolution().checkout(basket) == 180

    def test_B_offer_twice(self):
        basket = ['B', 'B', 'B', 'B']
        # (2B for 45) * 2
        assert CheckoutSolution().checkout(basket) == 90

    def test_3_of_everything(self):
        basket = ['A', 'A', 'A']
        basket.extend()
