from unittest import TestCase

from stack import Stack, EmptyStack


class TestStack(TestCase):
    def test_stack_push(self):
        stack = Stack()
        expected = 1

        stack.push(42)
        actual_stack_size = stack.size

        self.assertEqual(actual_stack_size, expected, f"{actual_stack_size} != {expected}")

    def test_stack_pop(self):
        stack = Stack()
        expected = 0
        item = 42
        stack.push(item)

        result = stack.pop()
        actual_stack_size = stack.size

        self.assertEqual(actual_stack_size, expected, f"{actual_stack_size} != {expected}")
        self.assertEqual(result, item, f"{result} != {item}")

    def test_stack_peek(self):
        stack = Stack()
        expected = 1
        item = 42
        stack.push(item)

        result = stack.peek()
        actual_stack_size = stack.size

        self.assertEqual(actual_stack_size, expected, f"{actual_stack_size} != {expected}")
        self.assertEqual(result, item, f"{result} != {item}")

    def test_peak_when_stack_empty(self):
        stack = Stack()
        expected = None

        result = stack.peek()

        self.assertEqual(result, expected, f"{result} != {expected}")

    def test_pop_when_stack_empty(self):
        stack = Stack()

        self.assertRaises(EmptyStack, stack.pop)
