"""Apply a discount based on purchase amount."""


def calculate_discounted_total(amount):
    if amount > 4000:
        discount = 0.15
    elif amount > 2000:
        discount = 0.10
    else:
        discount = 0

    return amount - discount * amount


try:
    amount = float(input("Enter purchase amount: "))

    if amount < 0:
        print("Amount cannot be negative.")
    else:
        total = calculate_discounted_total(amount)
        print(f"Pay: {total:.2f}")
except ValueError:
    print("Please enter a valid number.")
