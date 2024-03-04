# Den här testmodulen är bara till för att testa exempelprogrammen
# och är inte en del av grundkursen. Testning går vi igenom i den
# avancerade kursen.

from unittest import TestCase
from unittest.mock import Mock, patch

from Exempel.Lektion04 import cafe1, cafe2, cafe3


class CafeOrderTestMixin:
    def test_kaffe(self):
        self.order("kaffe")
        self.assert_prompts(["Vad vill du beställa? "])
        self.assert_messages(["Varsågod, här är ditt kaffe.",
                              "Det blir 20 kr, tack."])

    def test_te(self):
        self.order("te")
        self.assert_prompts(["Vad vill du beställa? "])
        self.assert_messages(["Varsågod, här är ditt te.",
                              "Det blir 15 kr, tack."])

    def test_öl(self):
        self.order("öl")
        self.assert_prompts(["Vad vill du beställa? "])
        self.assert_messages(["Tyvärr har vi sålt slut på öl."])

    def order(self, product):
        self.cafe.order(product)

    def assert_prompts(self, prompts):
        self.assertEqual(prompts, self.cafe.prompts)

    def assert_messages(self, messages):
        self.assertEqual(messages, self.cafe.messages)


class Cafe1Test(CafeOrderTestMixin, TestCase):
    def setUp(self):
        self.cafe = Cafe(cafe1)


class Cafe2Test(CafeOrderTestMixin, TestCase):
    def setUp(self):
        self.cafe = Cafe(cafe2)


class Cafe3Test(CafeOrderTestMixin, TestCase):
    def setUp(self):
        self.cafe = Cafe(cafe3)


class Cafe:
    def __init__(self, module):
        self._module = module
        self._print = Mock()
        self._input = Mock()
        self.prompts = []
        self.messages = []

    def order(self, product):
        with patch.multiple(self._module,
                            print=self._print,
                            input=self._input):
            self._input.return_value = product
            self._module.main()

        input_calls = self._input.call_args_list
        print_calls = self._print.call_args_list
        self.prompts = [c[0][0] for c in input_calls]
        self.messages = [" ".join(map(str, c[0])) for c in print_calls]
