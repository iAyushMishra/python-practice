"""Basic Python practice examples.

This file is a learning index. The actual runnable examples are separated into
their own files so each program has one clear purpose.
"""

EXAMPLES = [
    "area_of_circle.py",
    "surface_area_cuboid.py",
]


def show_examples():
    print("Basic Python examples:")
    for example in EXAMPLES:
        print(f"- basics/{example}")


if __name__ == "__main__":
    show_examples()
