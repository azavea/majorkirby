import unittest

from majorkirby import GlobalConfigNode, StackNode
from troposphere import Output
from moto import mock_cloudformation_deprecated


class FirstStackNode(StackNode):
    INPUTS = {"test": ["global:test"]}

    def set_up_stack(self):
        super(FirstStackNode, self).set_up_stack()

        self.add_output(Output("test", Value="First %s" % self.get_input("test")))


class SecondStackNode(StackNode):
    INPUTS = {"test": ["FirstStackNode:test"]}

    def set_up_stack(self):
        self.add_output(Output("test", Value="Second %s" % self.get_input("test")))


class TestStackNode(unittest.TestCase):
    @mock_cloudformation_deprecated
    def test_stack_threading(self):
        global_config = GlobalConfigNode(**{"test": "joker"})

        first = FirstStackNode(globalconfig=global_config)
        second = SecondStackNode(globalconfig=global_config, FirstStackNode=first)

        second.go()

        self.assertEqual(first.stack_outputs["test"], "First joker")
        self.assertEqual(second.stack_outputs["test"], "Second First joker")


if __name__ == "__main__":
    unittest.main()
