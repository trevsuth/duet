Code | Data
8 Storage Registers
1 I/O register (register 0)
1 Working (temp) register
Math operators +, -, *, / , %

| denotes a value
. denotes a pointer to a value
: denotes an input
< comment >

7 | 9 assert that 9 is value in register 7
7 . 6 assert that the value in register 6 equals the value in register 7

Rules:
1. All lines consist of 3 tokens
2. The first token (called the "Left") will always consist of an integer
3. The middle token (called the "Median") will be one of the set { | : .}
    3a. A | indicates that the Left of that line is a value
    3b. A : indicates that a number will be input into the register indicated by the Left
    3c. A . indicates that the Left is reference to a register
4. Comments begin with "<", end with ">" and can only be a single line
6. Numbers will only appear in the third place (called the "Right") will only be a number if the line is an assertation
7. Writing to a register directly will overwrite the value


Derived Rules:
1. ":" can only be used with ">"
2. If a ":" or "." is in the median, the Left must be between 1 and 8

null values do not exist    
only whole numbers can be used
once an = appears, all operations are performed in the working memory until a > or = operator appears


Examples:
write the sum of 3 +4 to register 1
3 | =
4 | +
1 | >

Write 5 to register 2
5 | =
2 | >

Divide the value in register 3 by 4
4 | /
3 | >

Take value input to register 6
6 : >

Add the value in register 6 to the value in register 7 and store the result in register 7
6 . =
7 . +
7 | >

Write the value in register 6 to IO
6 . =
0 | >



