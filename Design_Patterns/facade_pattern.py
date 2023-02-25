"""Facade Pattern

The Facade pattern is used to provide a simplified interface to a 
complex system.

Suppose you have a complex library that provides a set of functions for 
performing various tasks. Some of the functions have complex dependencies 
and require a lot of configuration to use correctly. You want to simplify 
the library by providing a simpler interface that hides the complexity and 
makes it easier to use the library without understanding all of the details.
"""


class Dependency1:
    def setup(self) -> str:
        print("Library setting up....")


class Dependency2:
    def prepare(self) -> str:
        print("Loading library...")


class Dependency3():
    def run(self) -> str:
        print("Library running!")


class ComplexLibrary:
    def __init__(self) -> None:
        self._dependecy_1 = Dependency1()
        self._dependecy_2 = Dependency2()
        self._dependecy_3 = Dependency3()
    
    def do_something(self) -> str:
        self._dependecy_1.setup()
        self._dependecy_2.prepare()
        self._dependecy_3.run()


class Facade:
    def __init__(self) -> None:
        self._library = ComplexLibrary()
    
    def do_something_simple(self) -> str:
        self._library.do_something()

"""Facade Pattern

The Facade pattern is used to provide a simplified interface to a 
complex system.

Suppose you have a complex library that provides a set of functions for 
performing various tasks. Some of the functions have complex dependencies 
and require a lot of configuration to use correctly. You want to simplify 
the library by providing a simpler interface that hides the complexity and 
makes it easier to use the library without understanding all of the details.
"""


class Dependency1:
    def setup(self) -> str:
        print("Library setting up....")


class Dependency2:
    def prepare(self) -> str:
        print("Loading library...")


class Dependency3():
    def run(self) -> str:
        print("Library running!")


class ComplexLibrary:
    def __init__(self) -> None:
        self._dependecy_1 = Dependency1()
        self._dependecy_2 = Dependency2()
        self._dependecy_3 = Dependency3()
    
    def do_something(self) -> str:
        self._dependecy_1.setup()
        self._dependecy_2.prepare()
        self._dependecy_3.run()


class Facade:
    def __init__(self) -> None:
        self._library = ComplexLibrary()
    
    def do_something_simple(self) -> str:
        self._library.do_something()

facade = Facade()
facade.do_something_simple()


# Output
# Library setting up....
# Loading library...
# Library running!