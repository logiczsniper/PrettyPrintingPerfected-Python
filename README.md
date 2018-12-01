## Pretty Printing Perfected
A tool for classic pretty printing and extreme pretty printing in one. <br> <br>


```
__                     .__        __
'--`      _____________|__| _____/  |_
 _|,--.   \____ \_  __ \  |/    \   __\\
/ `)   \  |  |_> >  | \/  |   |  \  |
\      |  |   __/|__|  |__|___|  /__|
 '.___/   |__|                 \/
```

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

###### prettify_sequence(data, outputTitle)

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

###### prettify_dict(data, outputTitle)

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

###### peachy_print(data, outputTitle)
There is also the option to use this method, which automatically detects which of the above
functions to use in order to prettify the input data structure.

#### Defaults
The user can modify a few defaults.
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
user_data = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
             {'id': '8472883', 'name': 'UserName', 'password': 'Password'}, 'milk (organic)',
             ['hello_four', ['hello_five']],
             'twinkies', 'yogurt', {'id': '456', 'name': ['item one', 'item two', 'item three'], 'password': 'yo'}]
# Output
```
```
Name
____

1) Item one
2) Item two
3) Item three

User data
_________

1) Apples
2) Belvita bars
3) Hello_one
4) Hello_two
5) Hello_three
6) Milk (organic)
7) Hello_four
8) Hello_five
9) Twinkies
10) Yogurt

Id -> 8472883
Name -> UserName
Password -> Password

Id -> 456
Password -> yo
```

Since sets are unordered, the extremely pretty version of them also are not ordered. Here is another example showing nested tuples and sets:
```python
# Input
data = {5: [3, 4, 5, 6, 7], 'hi': [34, 345, 4], '4': '4', 'tuple': ('in tuple one', 'in tuple two'),
        'my set': {'one', 'two', 'three', 'one', 5}}
# Output
```
```
5
_

1) 3
2) 4
3) 5
4) 6
5) 7

Hi
__

1) 34
2) 345
3) 4

Tuple
_____

1) In tuple one
2) In tuple two

My set
______

- Three
- One
- 5
- Two

User data
_________

4 -> 4

```

#### Full Example
The following is how this tool is intended to be used:
```python
from peachy-print import PeachyPrinter

if __name__ == '__main__':
    peachyPrinter = PeachyPrinter()
    data = [('item one', ('in nested tuple', ('hello',), 'yeah'), 'item two',
             'item three'), 70, 90, 'String', True, None,
            {'set item one', 'set item two', ('tuple set one', 'tuple set two'), 'set item three'},
            {'dict list': ['in dict one', 'in dict two', 'in dict three'], 'mighty': 'SEVEN',
             'username': 'USERNAME'}]

    output = peachyPrinter.peachy_print(data, 'all the data in the world')
```

This would print the `data` provided with the heading 'All The Data In The World' in a the peachy way.