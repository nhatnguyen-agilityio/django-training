class A:
    def f(self) -> int:
        return 2
    
class B:
    def f(self) -> int:
        return 3
    def g(self) -> int:
        return 4
    
def foo(a: B) -> None:
    print(a.f())
    a.g()

foo(B())
