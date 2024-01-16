import sys, unittest
from pathlib import Path

import cafe4

sys.path.append(str(Path(__file__).resolve().parent / "../Lektion08"))
lek8_test_cafe = __import__("test_cafe")  # lura PyCharm


class Cafe4Test(lek8_test_cafe.CafeOrderTestMixin, unittest.TestCase):
    def test_finöl(self):
        self.order("finöl")
        self.assert_prompts(["Vad vill du beställa? "])
        self.assert_messages(["Varsågod, här är ditt finöl.",
                              "Det blir 70 kr, tack."])

    def setUp(self):
        self.cafe = lek8_test_cafe.Cafe(cafe4)


if __name__ == '__main__':
    unittest.main()
