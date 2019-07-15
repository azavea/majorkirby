import unittest

from majorkirby import GlobalConfigNode


class TestGlobalConfigNode(unittest.TestCase):
    def test_stack_outputs(self):
        stack_inputs = {"test": "joker"}

        global_config = GlobalConfigNode(**stack_inputs)
        self.assertEqual(global_config.stack_outputs, stack_inputs)


if __name__ == "__main__":
    unittest.main()
