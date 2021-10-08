from toc import read_lines, Header

basic_test_file = """# TEST

This document is a test!

## Numbers

1. One
2. Two
3. Three

#### Pretty Cool Stuff

> Kind of cool...

## And other stuff

### Test 3

#### Test 4

##### Test 5

###### Test 6

Test Document
"""


def test_basic_file():
    doc = read_lines(basic_test_file.split('\n'))
    for (header, test_header) in zip(doc, [
            Header(1, "TEST"),
            Header(2, "Numbers"),
            Header(4, "Pretty Cool Stuff"),
            Header(2, "And other stuff"),
            Header(3, "Test 3"),
            Header(4, "Test 4"),
            Header(5, "Test 5"),
            Header(6, "Test 6"),
    ]):
        assert header.level == test_header.level
        assert header.line == test_header.line
