# test_types.py
from core.types import Integer, Text

def main():
    print("Testing Integer and Text types")

    i = Integer()
    t = Text()

    # Test Integer
    try:
        print("Validating 42 as Integer:", i.validate(42))
        print("Validating 'hello' as Integer:")
        i.validate("hello")
    except ValueError as e:
        print("Caught error:", e)

    # Test Text
    try:
        print("Validating 'world' as Text:", t.validate("world"))
        print("Validating 123 as Text:")
        t.validate(123)
    except ValueError as e:
        print("Caught error:", e)

if __name__ == "__main__":
    main()
