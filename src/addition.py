# app.py
# This is a test commit
# Adding Multiplication function

def add(a, b):
    return a + b
def mul(c, d):
    return c * d
    
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_mul():
    assert mul(2, 2) == 4
    
