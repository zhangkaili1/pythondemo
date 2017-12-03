import  unittest


if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
    unittest.TextTestRunner().run(suite)