import sys
from typing import IO

def helloworld(output_stream: IO[str]) -> None:
    """
    Print a hello world message to the world of Python.

    Args:
        output_stream: Output stream to write the message to.
    """
    try:
        output_stream.write("Hello world of Python\n")
    except AttributeError:
        print("Invalid output stream provided.")

def test_helloworld() -> None:
    """
    Test the helloworld function.
    """
    from io import StringIO
    output = StringIO()
    helloworld(output)
    assert output.getvalue() == "Hello world of Python\n"

if __name__ == "__main__":
    helloworld(sys.stdout)