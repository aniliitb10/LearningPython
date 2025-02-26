from symbol import return_stmt
from unittest import TestCase
from classes.program import Program
import inspect


class TestProgram(TestCase):
    # noinspection DuplicatedCode
    def test_instance_method(self):
        """ Test that instance methods are of type method, for the instances only! """
        self.assertFalse(inspect.ismethod(Program.instance_method))
        self.assertTrue(inspect.isfunction(Program.instance_method))
        self.assertEqual("args: [random_arg ()]", Program.instance_method('random_arg'))

        p = Program()
        self.assertTrue(inspect.ismethod(p.instance_method))
        self.assertFalse(inspect.isfunction(p.instance_method))
        self.assertEqual("args: [Program ('random_arg',)]", p.instance_method('random_arg'))

    def test_class_method(self):
        self.assertTrue(inspect.ismethod(Program.class_method))
        self.assertFalse(inspect.isfunction(Program.class_method))
        self.assertEqual(f"args: [<class 'classes.program.Program'> ('random_arg',)]",
                         Program.class_method('random_arg'))

        p = Program()
        self.assertTrue(inspect.ismethod(p.class_method))
        self.assertFalse(inspect.isfunction(p.class_method))
        self.assertEqual("args: [<class 'classes.program.Program'> ('random_arg',)]", p.class_method('random_arg'))

    def test_static_method(self):
        self.assertFalse(inspect.ismethod(Program.static_method))
        self.assertTrue(inspect.isfunction(Program.static_method))
        self.assertEqual(f"args: [('random_arg',)]", Program.static_method('random_arg'))

        p = Program()
        self.assertFalse(inspect.ismethod(p.static_method))
        self.assertTrue(inspect.isfunction(p.static_method))
        self.assertEqual(f"args: [('random_arg',)]", Program.static_method('random_arg'))

    # noinspection DuplicatedCode
    def test_free_method(self):
        self.assertFalse(inspect.ismethod(Program.free_method))
        self.assertTrue(inspect.isfunction(Program.free_method))
        self.assertEqual("args: [random_arg ()]", Program.instance_method('random_arg'))

        p = Program()
        self.assertTrue(inspect.ismethod(p.free_method))
        self.assertFalse(inspect.isfunction(p.free_method))
        self.assertEqual("args: [Program ('random_arg',)]", p.instance_method('random_arg'))

    def test_instance_lamda(self):
        p = Program()
        p.dynamic_lambda = lambda *args: f'args: [{args}]'
        self.assertFalse(hasattr(Program, 'dynamic_lambda'))
        self.assertTrue(hasattr(p, 'dynamic_lambda'))

        self.assertFalse(inspect.ismethod(p.dynamic_lambda))
        self.assertTrue(inspect.isfunction(p.dynamic_lambda))
        self.assertEqual("args: [('random_arg',)]", p.dynamic_lambda("random_arg"))
