from lib.control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

def test_admin_login():
    assert admin_login("sudo", "12345") == "Access denied"
    assert admin_login("admin", "12345") == "Access granted"
    assert admin_login("ADMIN", "12345") == "Access granted"
    assert admin_login("user", "password") == "Access denied"

def test_hows_the_weather():
    assert hows_the_weather(33) == "It's brisk out there!"
    assert hows_the_weather(55) == "It's a little chilly out there!"
    assert hows_the_weather(99) == "It's too dang hot out there!"
    assert hows_the_weather(75) == "It's perfect out there!"

def test_fizzbuzz():
    assert fizzbuzz(0) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(2) == 2

def test_calculator():
    assert calculator("+", 1, 2) == 3
    assert calculator("-", 1, 2) == -1
    assert calculator("*", 1, 2) == 2
    assert calculator("/", 1, 1) == 1
    assert calculator("/", 1, 0) == float('inf')
    assert calculator("a", 1, 2) is None

    # Check if invalid operation prints correctly
    import io
    import sys
    captured_out = io.StringIO()
    sys.stdout = captured_out
    calculator("a", 1, 2)
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Invalid operation!\n"
