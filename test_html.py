import unittest

class TestHTML(unittest.TestCase):
    def test_h1_line(self):
        with open("index.html", "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("<h1>Práctica Final: DevOps CI/CD con GitHub</h1>", content)


if __name__ == "__main__":
    unittest.main()
