
# Duet esolang notes

## Basics
* Duet is a memory register esolang 
* There are 8 resigers for storing integers
* Register 0 is uesd for I/O
* Operations are perfoemed in working memory, which is effectively another register
* Currently, the followig math oerators are supported:
    * Math operators +, -, *, / , %

## Rules
1. All lines consist of 3 tokens
1. The first token (called the "Left") will always consist of an integer
1. The middle token (called the "Median") determines what is impacted or references
    1. A "|" indicates that the Left of that line is a value
    1. A ":" indicates that a number will be input into the register indicated by the Left
    1. A "." indicates that the Left is reference to a register
1. The third token (called the "Right") determines the operation performed
1. Comments begin with "<", end with ">" and can only be a single line
1. Numbers will only appear in the third place (called the "Right") will only be a number if the line is an assertation
1. Writing to a register directly will overwrite the value
1. All registers are initilaized to 0 and null values do not exist
1. Only whole numbers are supported

### Derived Rules
1. ":" can only be used with ">"
1. If a ":" or "." is in the Median, the Left must be between 1 and 8
1. Once an = appears, all operations are performed in the working memory until a > or = operator appears


## Sintax

### Median Operators
`|` denotes a value
`.` denotes a pointer to a value
`:` denotes an input
`< comment >` denotes a comment

### Right Operators
`+` Addition
`-` Subtraction
`*` Multiplication
`/` Integer Division
`%` Modulo Division

### Assertations
7 | 9 assert that 9 is value in register 7
7 . 6 assert that the value in register 6 equals the value in register 7

## Examples
```
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
```
