# def adder(A, B):
#     result = A ^ B

#     carry = A & B
#     return (result, carry)

# print(f"0 + 0 = {adder(0,0)}")  # 0 + 0 = (0, 0)
# print(f"0 + 1 = {adder(0,1)}")  # 0 + 1 = (1, 0)
# print(f"1 + 0 = {adder(1,0)}")  # 1 + 0 = (1, 0)
# print(f"1 + 1 = {adder(1,1)}")  # 1 + 1 = (0, 1)


Set1 = {1/n for n in {2,4,8,16}}
Set2 = {n**2 for n in {-2,-1,0,1,2}} 
Set3 = {n for n in range(1,25) if 24 % n == 0} 
Set4 = {n for n in range(-10, 11) if n % 2 !=0}

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)