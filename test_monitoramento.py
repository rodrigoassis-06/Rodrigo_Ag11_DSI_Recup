import unittest
from colorama import Fore
from main import obter_cor_nivel, niveis_reservatorio

class TestMonitoramento(unittest.TestCase):
    def test_niveis_cores(self):
        self.assertEqual(obter_cor_nivel(1), Fore.RED)
        self.assertEqual(obter_cor_nivel(2), Fore.YELLOW)
        self.assertEqual(obter_cor_nivel(3), Fore.GREEN)
        self.assertEqual(obter_cor_nivel(4), Fore.CYAN)
        self.assertEqual(obter_cor_nivel(5), Fore.BLUE)

    def test_quantidade_niveis(self):
        self.assertEqual(len(niveis_reservatorio), 5)

if __name__ == "__main__":
    unittest.main()
