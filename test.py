def adder(A, B):
    result = A ^ B

    carry = A & B
    return (result, carry)

print(f"0 + 0 = {adder(0,0)}")  # 0 + 0 = (0, 0)
print(f"0 + 1 = {adder(0,1)}")  # 0 + 1 = (1, 0)
print(f"1 + 0 = {adder(1,0)}")  # 1 + 0 = (1, 0)
print(f"1 + 1 = {adder(1,1)}")  # 1 + 1 = (0, 1)