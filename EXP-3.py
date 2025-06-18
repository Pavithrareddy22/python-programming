# Input values again
a = int(input("\nEnter value of a: "))
b = int(input("Enter value of b: "))

# Swapping without a temporary variable
a, b = b, a

print("\nAfter swapping without using temporary variable:")
print("a =", a)
print("b =", b)
