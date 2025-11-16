from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_empty_basket(self):
        assert CheckoutSolution().checkout([]) == -1

    def test_invalid_item(self):
        assert CheckoutSolution().checkout(['Z']) == -1

    def test_one_of_each(self):
        basket = ['A', 'B', 'C', 'D']
        assert CheckoutSolution().checkout(basket) == 115
