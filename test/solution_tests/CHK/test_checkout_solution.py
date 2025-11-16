from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_empty_basket:
        assert CheckoutSolution().checkout
