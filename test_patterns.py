from Patterns.Singleton.singleton import Singleton
from Patterns.FactoryMethod.factory_method import LoggerFactory, FileLoggerFactory, ConsoleLoggerFactory
from Patterns.AbstractFactory.abstract_factory import Application, WindowsFactory, MacFactory
from Patterns.Builder.builder import PizzaDirector, HawaiianPizzaBuilder

def test_singleton():
    print("=== Testing Singleton ===")
    s1 = Singleton()
    s2 = Singleton()
    print(f"Singleton test: {s1 is s2}")
    print()

def test_factory_method():
    print("=== Testing Factory Method ===")
    file_factory = FileLoggerFactory()
    console_factory = ConsoleLoggerFactory()
    
    file_result = file_factory.log_message("Hello Factory")
    console_result = console_factory.log_message("Hello Factory")
    
    print(f"File logger: {file_result}")
    print(f"Console logger: {console_result}")
    print()

def test_abstract_factory():
    print("=== Testing Abstract Factory ===")
    windows_app = Application(WindowsFactory())
    mac_app = Application(MacFactory())
    
    print("Windows style:")
    for result in windows_app.paint():
        print(f"  {result}")
    
    print("Mac style:")
    for result in mac_app.paint():
        print(f"  {result}")
    print()

def test_builder():
    print("=== Testing Builder ===")
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)
    
    director.construct_pizza()
    pizza = builder.get_result()
    
    print(f"Built pizza: {pizza}")
    print()

if __name__ == "__main__":
    test_singleton()
    test_factory_method()
    test_abstract_factory()
    test_builder()
    print("all patterns tested successfully!")
