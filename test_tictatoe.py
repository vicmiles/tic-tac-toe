import unittest

class test_eval(unittest.TestCase):
    def test_x(self):
        self.assertEqual(evaluate("xxxo--------------"), 'x')

    def test_o(self):
        self.assertEqual(evaluate("oox--------------"), 'o')

    def test_not_fin(self):
        self.assertEqual(evaluate("x-o-x-o-x-o-x-o-x-"), '-')

class TestMoveFunction(unittest.TestCase):
    def test_move_x_first_position(self):
        self.assertEqual(move("--------------------", 'x', 0), "x-------------------")

    def test_move_o_last_position(self):
        self.assertEqual(move("--------------------", 'o', 19), "-------------------o")



if __name__ == '__main__':
    unittest.main()


#01. Package can contain multiple modules, module is a single file with code.
#02. Side effect is anything that happens beyond the function. It can affect the state of the program. When a function writes or modifies the contents of a file, it's a side effect.
#03. Exception is an error or an unexpected situation that can happen during the execution of a program. Sometimes third-party code can occure exception, to protect it we can use try, except, print, raise to catch the expectations.
#04. Exception class, raise keyword, try, except.
#05. Tests help to catch bags, debuging, to level up th quality of the code, prevent code from unexpected errors, leaks, crushing.