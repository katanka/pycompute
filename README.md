# pycompute

Input
=====

Units
---------

A list of common units is in `units.json`.
The format is list of key value pairs, as such:

`[To unit]: {from : [from unit], factor : [conversion factor]}`

### Examples:

`'in': {from : 'cm', factor : 2.54}`

Constants
---------

Place each constant you want on a seperate line in `constants.txt`.
### Format:
`[Name]	[Value] [Optional: Units]`
The name can be any string which does not contain whitespace.
The value can take the form of an integer, a fraction, a floating point number, or scientific notation.
Please seperate the units using `*` and `/`, and for higher powers, use `^`, e.g. `m^3`.

### Examples:
`hbar	1.054572*10^-34	J*s`
`e	2.714`
`a_1	3/2`
`c 3*10^8	m/s`

Expressions
-----------

Place each expression you want on a seperate line in `expressions.txt`.

### Format:
`[Name] [Expression]`

The expression should be an arithmetic expression involving only the named constants in `constants.txt` 

Output
======