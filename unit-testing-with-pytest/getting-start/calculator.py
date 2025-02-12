from another_class import AnotherClass

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return "divisor can not be zero" if b == 0 else a / b

    def use_capsys_fixture(self):
        print("hello world!")

    def use_external(self, value):
        class_obj = AnotherClass()
        return class_obj.some_method(value)

    def use_object(self,value,some_obj):
        return some_obj.fetch(value)