# Input values
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Swapping with a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using temporary variable:")
print("a =", a)
print("b =", b)
