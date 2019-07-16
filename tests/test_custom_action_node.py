import unittest

from majorkirby import GlobalConfigNode, CustomActionNode


class TitleCustomActionNode(CustomActionNode):
    INPUTS = {"test": ["global:test"]}

    def action(self):
        self.stack_outputs = {"test": self.get_input("test").title()}


class TestCustomActionNode(unittest.TestCase):
    def test_action(self):
        stack_inputs = {"test": "joker"}

        custom_action = TitleCustomActionNode(
            globalconfig=GlobalConfigNode(**stack_inputs)
        )
        custom_action.go()

        self.assertEqual(custom_action.stack_outputs["test"], "Joker")


if __name__ == "__main__":
    unittest.main()
