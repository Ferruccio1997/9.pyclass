from utils_exer1 import log_execution

@log_execution
def add(a: float, b: float) -> float:
    return a + b

@log_execution
def divide(a: float, b: float) -> float:
    return a / b

print(add(2,'3'))

print(add(2,'j'))

print(add(2,4))