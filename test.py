# Function that prints a countdown from a given number to 1
def countdown(n):
    """Prints a countdown from n to 1."""
    while n > 0:
        print(f"Countdown: {n}")
        n -= 1
    print("Blast off!")

# Unit test for the countdown function
def test_countdown():
    import io
    import sys

    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    countdown(3)
    
    sys.stdout = sys.__stdout__
    
    expected_output = "Countdown: 3\nCountdown: 2\nCountdown: 1\nBlast off!\n"
    assert captured_output.getvalue() == expected_output, "Test failed!"
    print("Test passed!")

# Running the function and the test
if __name__ == "__main__":
    countdown(5)
    test_countdown()

