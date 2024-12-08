from functions import salary, hello_who
def test_hello_who_other():
    assert hello_who('Max') == 'Hello, Max'
    assert hello_who('Ura') == 'Hello, Ura'
    assert hello_who('Sasha') == 'Hello, Sasha'
    assert hello_who('Lesha') == 'Hello, Lesha'
def test_salary():
    assert(2, 2) != 5
    assert(3, 1) != 6