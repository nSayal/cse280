# CSE 280 Prove 11

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Sayal Neupane

## Question 1 (9 points)

Find the $gcd$ for each of the following by hand using Eulid's Algorithm  Show your work in the tables below.  The first one is done for you.  Add more rows to each table as needed.  You can check your work with a calculator.

**Problem A**: $gcd(43,57)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|43|57|14|
|14|43|1|
|1|14|0|

Answer: 1

**Problem B**: $gcd(39,501)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|39|501|33|
|33|39|6|
|6|33|3|
|3|6|0|

Answer: 

**Problem C**: $gcd(110,765)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|110|765|105|
|105|110|5|
|5|105|0|

Answer: 

**Problem D**: $gcd(493,899)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|493|899|406|
|406|493|87|
|87|406|58|
|58|87|29|
|29|58|0|

Answer: 

## Question 2 (10 points)

Find the $gcd$ for the first three problems from Question 1 using the Extended Eulcid Algorithm to express the answer as a linear combination.  The first one is done for you.

|Problem|$gcd = s*x + t*y$|
|:-:|:-:|
|$gcd(43,57)$|$1 = 4*43 - 3*57$|
|$gcd(39,501)$|$3=-77*39+6*501$|
|$gcd(110,765)$|$5=7*110-1*765$|


## Question 3 (8 points)

Find the multiplicative inverse for $x \text{ mod } n$ in the table below.  These numbers are smaller so you don't need to use the Extended Euclidean Algorithm to solve.  You can check your answers by verifying that $sx \text{ mod } n = 1$ where $s$ is the multiplicative inverse you calculated.

|$x$|$n$|Multiplicative Inverse|
|:-:|:-:|:-:|
|2|7|4|
|5|11|9|
|7|20|23|
|3|13|9|

## Question 4 (9 points)
Use the Extended Euclidean Algorithm to find the multiplicative inverse of $83 \text{ mod } 96$.  

Answer:
* $s = -37$
* $t = 32$
* Multiplicative Inverse = 59

## Question 5 (15 points)

### Part 1 

Create the private RSA keys by using the following inputs for RSA:

* Prime numbers:
    * $p = 137$
    * $q = 211$
* Public Key:
    * $e = 19$
    
You can use the following python code to do part of the calculations needed. This code implements the Extended Eculidean Algorithm and provides the GCD and the linear combination for the GCD.  If `x` and `y` are provided to the function, it will return a tuple `(r,s,t)` where `r` is the GCD and $r = s*x + t*y$.

```python
def gcd_ext(x,y):

    (old_r, r) = (x, y)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    while r != 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    return (old_r, old_s, old_t)
```

Answer:
* d (private key) = 9019

### Part 2

Write code in Python do the following using the values from Part 1 above:

1. Encrypt the value $5465$ and display the encrypted result
2. Decrypt the value previously displayed and verify that it is $5465$ again.


```python
def gcd_ext(x, y):
    if x == 0:
        return y, 0, 1
    else:
        g, a, b = gcd_ext(y % x, x)
        return g, b - (y // x) * a, a

# Given values
p = 137
q = 211
e = 19

# Calculate (p-1)(q-1)
modulus = (p - 1) * (q - 1)

# Use the gcd_ext function to find d
_, d, _ = gcd_ext(e, modulus)

print(f"The private key d is: {d}")

# Encryption
m = 5465
n = p * q
c = pow(m, e, n)
print(f"Encrypted value c is: {c}")

# Decryption
decrypted_m = pow(c, d, n)
print(f"Decrypted value is: {decrypted_m}")

```
  
