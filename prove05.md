# CSE 280 Prove 05

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site. S4.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Sayal Neupane

## Question 1 (5 points)

What is the set that corresponds to the relation given in the arrow diagram below:

![](prove05_diagram1.drawio.png)

**Answer**: $\lbrace (A,3),(A,4),(C,1),(C,3),(D,4) \rbrace$

## Question 2 (6 points)

Determine if the following relations are Reflexive, Anti-Reflexive, or Neither by marking an "X" in the appropriate column of the table.  The domain of each relation $R$ is $\mathbf{R}$.

|Relation Set|Reflexive|Anti-Reflexive|Neither|
|:-:|:-:|:-:|:-:|
|$xRy, \text{ if }x \ge y$|x|||
|$xRy, \text{ if }x \gt y$||x||
|$xRy, \text{ if }x + 1 = y$||x||
|$xRy, \text{ if }x + y = 2$|||x|
|$xRy, \text{ if }\lceil x \rceil \le \lceil y \rceil$|x|||
|$xRy, \text{ if }x^3 = y^3$|x|||

## Question 3 (6 points)

Determine if the following relations (same from Question 2) are Symmetric, Anti-Symmetric, or Neither by marking an "X" in the appropriate column of the table.  The domain of each relation $R$ is $\mathbf{R}$. 

|Relation Set|Symmetric|Anti-Symmetric|Neither|
|:-:|:-:|:-:|:-:|
|$xRy, \text{ if }x \ge y$||x||
|$xRy, \text{ if }x \gt y$||x||
|$xRy, \text{ if }x + 1 = y$||x||
|$xRy, \text{ if }x + y = 2$|x|||
|$xRy, \text{ if }\lceil x \rceil \le \lceil y \rceil$|||x|
|$xRy, \text{ if }x^3 = y^3$|x|||

## Question 4 (6 points)

Determine if the following relations (same from Question 2) are Transitive by marking "Yes" or "No" in the column of the table.  The domain of each relation $R$ is $\mathbf{R}$.

|Relation Set|Transitive|
|:-:|:-:|
|$xRy, \text{ if }x \ge y$|YES|
|$xRy, \text{ if }x \gt y$|YES|
|$xRy, \text{ if }x + 1 = y$|NO|
|$xRy, \text{ if }x + y = 2$|NO|
|$xRy, \text{ if }\lceil x \rceil \le \lceil y \rceil$|YES|
|$xRy, \text{ if }x^3 = y^3$|YES|

## Question 5 (6 points)

Determine if the following relations (same from Question 2) are Equivalences by marking "Yes" or "No" in the column of the table.  The domain of each relation $R$ is $\mathbf{R}$.

|Relation Set|Equivalence|
|:-:|:-:|
|$xRy, \text{ if }x \ge y$|NO|
|$xRy, \text{ if }x \gt y$|NO|
|$xRy, \text{ if }x + 1 = y$|NO|
|$xRy, \text{ if }x + y = 2$|NO|
|$xRy, \text{ if }\lceil x \rceil \le \lceil y \rceil$|NO|
|$xRy, \text{ if }x^3 = y^3$|YES|

## Question 6 (5 points)

Select the relations below that are equivalence relations if the domain is {1, 2, 3, 4} by marking "Yes" or "No" in the column of the table.

|Relation Set|Equivalence Relation|
|:-:|:-:|
|$\lbrace (1,4), (4,1), (2,2), (3,3) \rbrace$|NO|
|$\lbrace (1,4), (4,1), (1,3), (3,1), (2,2) \rbrace$|NO|
|$\lbrace (1,4), (4,1), (1,1), (2,2), (3,3), (4,4) \rbrace$|Yes|
|$\lbrace (1,4), (4,1), (1,3), (3,1), (1,1), (2,2), (3,3), (4,4) \rbrace$|NO|
|$\lbrace (1,4), (4,1), (1,3), (3,1), (3,4), (4,3), (1,1), (2,2), (3,3), (4,4) \rbrace$|YES|

## Question 7 (16 points)

For each directed graph below representing a relation, determine based on its form if its Reflexive, Symmetric, Transitive, and/or an Equivalence relation by marking "Yes" or "No" in the appropriate column of the table.

|Directed Graph of Relation|Reflexive|Symmetric|Transitive|Equivalence|
|:-:|:-:|:-:|:-:|:-:|
|![](prove05_diagram2.gv.png)|NO|YES|NO|NO|
|![](prove05_diagram3.gv.png)|YES|YES|YES|YES|
|![](prove05_diagram4.gv.png)|YES|YES|NO|NO|
|![](prove05_diagram5.gv.png)|YES|YES|YES|YES|
