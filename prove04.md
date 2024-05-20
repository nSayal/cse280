# CSE 280 Prove 04

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Sayal Neupane

## Question 1 (24 points)

For each of these functions, determine if they are well-defined, one-to-one, and/or onto.  Put "Yes" or "No" in the appropriate columns.  For the first 4 problems, let $A=\lbrace 1,2,3,4 \rbrace$ and $B=\lbrace a, b, c, d \rbrace$. If a function is not well defined, then mark no for both one-to-one and onto. For the last 4 functions written in the format $f(x)=$ you may find it helpful to graph the function on [Desmos](https://www.desmos.com/).  The first one is done for you.

|Function|Well-Defined Function|One-to-One Function|Onto Function|
|:-:|:-:|:-:|:-:|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(3,c),(4,d) \rbrace$|Yes|Yes|Yes|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,a),(3,b),(4,d) \rbrace$|Yes|No|No|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(3,c) \rbrace$|No|No|No|
|$f : A \to B, \text{ where } f = \lbrace (1,a),(2,b),(2,c),(3,a),(4,a) \rbrace$|No|No|NO|
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = x^3-x$|Yes|NO|Yes|
|$f : \mathbf{Z} \to \mathbf{Z}, \text{ where } f(x) = -x+2$|Yes|Yes|Yes|
|$f : \mathbf{Z}^+ \to \mathbf{Z}^+, \text{ where } f(x) = \lceil \frac {x}{2} \rceil$|Yes|NO|Yes|
|$f : \mathbf{R} \to \mathbf{R}, \text{ where } f(x) = \frac{5}{x-5}$|NO|No|NO|
|$f : \lbrace x \mid x \in \mathbf{R} , x \ne 5 \rbrace \to \mathbf{R}, \text{ where } f(x) = \frac{5}{x-5}$|Yes|Yes|Yes|

## Question 2 (9 points)

Explain why $f : \mathbf{R} \to \mathbf{R} \text{ where } f(x) = x^2$ is a well defined funtion but is niether one-to-one nor onto (with counterexamples as needed).

**Answers**:
* Is Well Defined because for any real number x, there exists a only one f(x), ensuring that every domain has a corresponding value.
* Not One-to-One because multiple domains can give the same value in this function. Such as, f(2) = $2^2$ = 4 and f(-2) = $(-2)^2$ 4, showing that distinct inputs map to the same output.
* Not Onto because not every real number is covered by the function's mapping. For example, there is no real number whose square is negative since squaring real number always gives non-negative result.

## Question 3 (9 points)

Find the inverse of each of the following functions, calculate $f(3)$, and then calculate the composition of $(f^{-1} \circ f)(3)$ (which will prove that you have found the correct inverse).

|Domain|$f(x)$|$f^{-1}(x)$|$f(3)$|$(f^{-1} \circ f)(3)$
|:-:|:-:|:-:|:-:|:-:|
|$f : \mathbf{R} \to \mathbf{R}$|$2x+3$|$\frac{x-3}2$|9|3|
|$f : \lbrace x \in \mathbf{R} : x \gt 0 \rbrace \to \mathbf{R}$|$3^x$|$log_3(x)$|27|3|
|$f : \lbrace x \in \mathbf{R} : x \ge -2 \rbrace \to \mathbf{R}^+$|$x^2-2$|$\sqrt{x+2} \ or -\sqrt{x+2}$|7|3, -3|


## Question 4 (8 points)

Create lambda functions to implement the following functions that have domain of $\mathbf{R}$ and co-domain of $\mathbf{R}$:

* $f_1(x) = x^3+x^2+x+1$
* $f_2(x) = 3x+5$
* $f_3(x) = \frac{x(x+1)}{2}$

The test code below will use the lambda functions to generate the set of all $(X, f(X))$ where $X=\lbrace x \in \mathbf{Z} : -5 \le x \le 5 \rbrace$:

```python
f1 = lambda x : x ** 3 + x ** 2 + x + 1 
f2 = lambda x : 3 * x + 5 
f3 = lambda x : (x * ( x+ 1))/ 2

domain = range(-5,6)
f1_points = {(x,f1(x)) for x in domain}
f2_points = {(x,f2(x)) for x in domain}
f3_points = {(x,f3(x)) for x in domain}

# Expected results below may be sorted differently
print(f1_points)
# {(3, 40), (-1, 0), (4, 85), (2, 15), (5, 156), (-2, -5), (-5, -104), (1, 4), (-4, -51), (-3, -20), (0, 1)}
print(f2_points)
# {(-5, -10), (-1, 2), (5, 20), (3, 14), (1, 8), (2, 11), (-3, -4), (0, 5), (4, 17), (-2, -1), (-4, -7)}
print(f3_points)
# {(0, 0.0), (-1, 0.0), (-3, 3.0), (1, 1.0), (3, 6.0), (4, 10.0), (2, 3.0), (-4, 6.0), (5, 15.0), (-2, 1.0), (-5, 10.0)}
```

