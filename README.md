## Pretty Printing Perfected
A tool for classic pretty printing and extreme pretty printing in one.

#### Definitions
For reference in the code and in this file, here is how I define classic
pretty printing versus extreme.

###### Classic
NOTE: All classic pretty printing is handled by the built in python library: pprint.

When I refer to classic pretty printing, it means what is normally accepted
as pretty printing; the syntax for the actual data structure is kept but
the data is spaced in a neat way. Here is an example:

```python
# Input
groceries_list = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
                  'donuts', 'milk (organic)', ['hello_four', ['hello_five']],
                  'twinkies', 'yogurt']

# Output
```
```
[   'apples',
    'belvita bars',
    ['hello_one', 'hello_two', 'hello_three'],
    'donuts',
    'milk (organic)',
    ['hello_four', ['hello_five']],
    'twinkies',
    'yogurt']
```


###### Extreme
This is the unique functionality of the package. It completely converts the
data structure to a string that could be presented straight to a user in
some way. Here is an example:

```python
# Input
groceries_list = ['apples', 'belvita bars', 'donuts', 'milk (organic)']

# Output
```
```
Groceries List
______________

1) Apples
2) Belvita Bars
3) Donuts
4) Milk (organic)
```

#### Functions
There are a range of functions to convert specific data structures into
pretty strings.

###### prettify_list()

```python
# Input
groceries_list = ['apples', 'belvita bars', 'donuts', 'milk (organic)']

# Output
```
```
Groceries List
______________

1) Apples
2) Belvita Bars
3) Donuts
4) Milk (organic)
```

###### prettify_dict()

```python
# Input
user_data = {'id': '8472883', 'name': 'UserName', 'password': 'Password'}

# Output
```
```
User Data
______________

Id -> 8472883
Name -> UserName
Password -> Password
```

#### Defaults
The user can modify the two defaults.
1. `regular_print`
This determines whether or not to convert to a normal pretty print string
or to an extreme version which only this package offers. It defaults to
`False`, resulting in use of the extreme functions.
2. `return_string`
This determines whether to return a string or print the output automatically.
It defaults to `False`, resulting in automatic printing.
3. `iterate_nested`
This determines whether or not the printer will iterate through each nested
data structure it finds or completely ignore it and continue.
4. `capitalize`
This determines whether or not to the printer will automatically capitalize
strings when printed.
5. `indent`
Changing this only effects the output of a regular print action. It determines
the indent of the classic pretty printed data structure. It defaults to
0, resulting in no indent.

#### Nested Data Structures (same type)
If `iterate_nested` is set to `True`(see above), nested data structures
of the same type are treated as if they are not nested at all;
the output will closely resemble the same data structure with no
nesting. Here is an example:

```python
# Input
groceries_list = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
                  'donuts', 'milk (organic)', ['hello_four', ['hello_five']],
                  'twinkies', 'yogurt']

# Output
```
```
Groceries List
______________

1) Apples
2) Belvita bars
3) Hello_one
4) Hello_two
5) Hello_three
6) Donuts
7) Milk (organic)
8) Hello_four
9) Hello_five
10) Twinkies
11) Yogurt

```

#### Nested Data Structures (different type)
If `iterate_nested` is set to `True`(see above), nested data structures
of different types automatically separate themselves from each other and
are printed in their own blocks. Here is an example:

```python
# Input
nested_data = ['apples', {'id': '8472883', 'name': {'hello': 'world'}, 'password': 'Password'}, 'donuts', 'milk (organic)']

# Output
```
```
Nested Party
_____

1) Apples
2) Donuts
3) Milk (organic)

Id -> 8472883
Hello -> world
Password -> Password
```
