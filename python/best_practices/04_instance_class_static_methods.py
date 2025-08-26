
import logging

logging.basicConfig(level=logging.INFO)

class ExampleClasss:
    class_level = "i live in class"

    def __init__(self, instance_name):
        self.instance_name = instance_name

    @classmethod
    def class_method(cls):
        # throught the cls can access attributes that are shared accross instances
        logging.info(f"Called a class_method, {cls.class_level}")

    @staticmethod
    def static_method():
        logging.info("Called a static_method")

    def instance_method(self):
        logging.info(f"My name is {self.instance_name}")


if __name__ == '__main__':

    ex1 = ExampleClasss("ex1")
    ex1.instance_method()

    ex1.class_method()
    
    ExampleClasss.static_method()