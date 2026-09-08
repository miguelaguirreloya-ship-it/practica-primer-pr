import unittest

from saludo import saludar


class TestSaludo(unittest.TestCase):
    def test_saludar_incluye_nombre(self):
        self.assertIn("Ana", saludar("Ana"))

    def test_saludar_incluye_hola(self):
        self.assertIn("Hola", saludar("Ana"))


if __name__ == "__main__":
    unittest.main()
