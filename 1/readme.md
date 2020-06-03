_[Download solution](solution.py)_

# Reverse Polish Notation

_**Objective:** Write a basic 4-function Reverse Polish Notation calculator._

Reverse Polish Notation (RPN) is one way computers can do basic calculator operations. We tend to work in "in-fix" notation, meaning the operation goes in between the operands:

> 1 + 2

> <operand 1> \<operation\> <operand 2>

RPN works by reading the operands first, then performing some operation on them:

> 1 2 +

> <operand 1> <operand 2> \<operation\>

Thus, this is also called "post-fix" notation.

## Phase 1: Addition

For the first stage we'll start easy. Output, input, convert text to numbers, and perform math.

### Print hello world

_**Objective:** Write a program (you only need 1 line of code) to print "Hello World"._

It's much easier and more satisfying to program when you can see the result of your code.

In Python, we print to the console by using the `print()` function. The first (and only) argument/parameter for the `print()` function is the text you want to display.

So, to display the text "Hello":

```python
print('Hello')
```

_Note: Python lets you use single quotes - `'Hello'` - or double quotes - `"Hello"`. They work exactly the same._

### Print hello, \<name\>

_**Objective:** Ask the user for their name, get the text the user inputs, then display their name._

Python is sometimes known as a beginner's language partially because some things that are complicated in other languages are very easy in Python.
Getting input from the user is one of those things. Below is an example comparing Java to Python. You don't need to know Java, everything you need to know is explained afterwards, but it's a good way to show off why Python is so cool!

If you're not interested, just look at the Python example and move on to the _Objective_.

In Java:
```java
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text;

        // Get input
        System.out.print("Enter a value: ");
        text = scanner.nextLine();

        // Display it
        System.out.println("You entered: " + text);
    }
}
```

In Python:
```python
text = input("Enter a value: ")
print("You entered: " + text)
```

In both Java and Python examples, you would enter some text, then hit \[Enter\] to continue the program.

Notice how in Java, you have to explictly display the prompt "Enter a value: " _then_ get input, but in Python, the parameter for the `input()` function is the prompt, and will display before the user can type in the console.

It's always a good idea to include some kind of prompt (I like to use "> " when it's not important). Sometimes your program will freeze for a moment - including that prompt makes sure you always know when the program is waiting on you or on something else.

Also notice how in Java, we had to create the `text` variable to store whatever the user input. It could have been done in one line like `String text = scanner.nextLine();`, but this highlights that in Java, variables must be _created_ which is a separate process from assigning a value. In Python, just the line `text` makes no sense - variables are created and given a value at the same time, i.e. you cannot have a variable that does not have a value (...with an exception that we can talk about later, or you can google Python's `None` value).

You may find it convenient to modify your code from the _Hello World_ step.

Example output:

> **What's your name?** _John Smith_
>
> **Hello, John Smith**

### Prompt and convert to number

**Objective** Get a number from the user, convert it to an `int`, add 1, then print the sum.

I'm not gonna lie, this one is pretty boring and you can probably just skip it. However, there is some useful and interesting information about _data types_ here.

So far we've only dealt with text - called **strings** in programming because they are "strings" of characters (letters, numbers, spaces, special characters, even some invisible characters that the computer uses!).

Arguably the second most common data type is an **integer** meaning a whole number like 5, or 0, or -254, or 1534086484351. Without going too deep into programming theory, most languages are limited in how large a number can be (each number is limited in the number of bits it can use), but Python isn't.

If you were in Java, you can do this neat trick:
```java
int x = 2147483647;  // Importantly, this is the same as 2^(31) - 1
System.out.println(x + 1);
```
You'd expect this to print `2147483648`, but instead it prints `-2147483648`! There's a perfectly good, somewhat advanced reason for this, but suffice to say that you're trying to add 1 to the largest number Java knows how to handle, so it handles it by looping around to the negatives.

In Python, this trick works the way math says it should and is thus much less exciting, but much more useful:
```python
x = 2147483647
print(x + 1)  # Actually prints 2147483648

# In fact...
x = 2147483647
print(x + x)  # Correctly prints 4294967294. Java would have printed -2...
```

---

_Anyway, back to the task at hand!_

You've probably had enough Java vs. Python by now, so I'll keep things focused on Python from now on.

In Python, it's really easy to convert text to numbers...

```python
text = "123"
number = int(text)
```

...and numbers to text...

```python
number = 123
text = str(number)
```

This is useful if you have a number as a string (e.g. from the `input()` function), but want to do math.

Running this...
```python
text = input("Give me a number: ")
one_more = text + 1
print(one_more)
```
...will throw an error (a TypeError).

An interesting thing to note is that the error messages says that you can't **concatenate** an int to a str.
Concatenate means to add a string on to the end of another string. For lists, you _append_ values to the end.
The terms are _technically_ distinct, but "concatenate" vs "append" vs "add on to the end" pretty much all mean pretty much the same thing.

To make this work, you need to tell Python that it's a number, not text...

```python
text = input("Give me a number: ")
number = int(text)
one_more = number + 1
print(one_more)
```

> **Give me a number:** _123_
>
> **124**

Okay, so I gave you the code for this one... It's pretty boring anyway. The next step is where it becomes useful!

### Add numbers together

**Objective** Get two numbers from the user, add them together, then print the sum.

Example output:
> **1st number:** _5_
>
> **2nd number:** _7_
>
> **Sum: 12**

Bonus points if the last line (instead of "Sum: 12") looks like

> **5 + 7 = 12**

---

Note that while programming this, you may choose to create a `sum` variable and wonder why it's highlighted the same color as `print` and `input`.
This is because `sum()` is a built-in function just like `print()` and `input()`. If you're curious, feel free to google what Python's `sum()` function does, it can be really useful!

You _can_ still use it as a variable (you just can't then use it as the built-in `sum()` function), but it's usually best to avoid these kinds of built-in functions as variable names.
Sometimes, Python is _too_ easy and uses common names for things that you may want to use a different way. Consider `answer = a + b` to avoid `sum = a + b`.

## Phase 2: Conditional math

Arguably the _most_ common data type in programming is the boolean. True or False. That's it; those are the only possible values.

You know how computers store things as bits, 0s and 1s? It's the same as low vs high voltage. Off vs On. True vs False.

In order for a computer to do anything really useful, it has to be able to decide _for itself_ what to do. It would be awful if you had a separate program for each of a calculator's functions. So the computer needs to be able to decide which operation to perform. Because computers are _really_ good at True vs False, it's very common to use "if this is True, do this thing; optionally, otherwise, do this other thing".

This is called an if-statement or an if-else-statement.

In Python, this looks like...
```python
if True:
    print('Yes')

# Not every if-statement needs an else-statement
else:
    print('No')

print('Done')
```

You can "chain" and "nest" these together
```python
if True:
    print('Yes 1')
else:
    # This is nesting because it's "nesting" inside another if-else
    if True:
        print('Yes 2')
    else:
        print('No')

print('Done')

# Or use elif, short for "else-if"

# This is chaining because they're on the same level
# and they're evaluated one at a time, like links in a chain,
# until one (in this case the first one) executes
if True:
    print('Yes 1')
elif True:
    print('Yes 2')
else:
    print('No')

print('Done')
```

**Important** Notice how the `print()` statements inside the if-else-statements are indented? That's how Python knows that they should _only_ run in those certain cases. Since the `print('Done')` is not indented, it will always run, regardless of the operation of the if-else-statement.

To get a boolean (True vs False), we use "conditional operations" like "equals" or "greater than" or "less than or equal to" or "not equal".

This table show how we can compare two variables `a` and `b`.

| Python | English |
|:------:|:--------|
| `a == b` | A **equals** B ? |
| `a != b` | A does **not equal** B ? |
| `a < b` | A is **less than** B ? |
| `a > b` | A is **greater than** B ? |
| `a <= b` | A is **less than or equal to** B ? |
| `a >= b` | A is **greater than or equal to** B ? |

There's also the `not` operator which sometimes is useful, though it's rarely used right next to these operators because you can always change them to not need `not`. The `not` operator goes _before_ a conditional and inverts it: True becomes False and False becomes True.

For example: `5 < 2` is False, but `not 5 < 2` is True.

This is how every boolean operator can be rewritten to not need `not`:
| Negated Python | Rewritten Python |
|:---------------|:-----------------|
| `not a == b` | `a != b` |
| `not a != b` | `a == b` |
| `not a < b` | `a >= b` |
| `not a > b` | `a <= b` |
| `not a <= b` | `a > b` |
| `not a >= b` | `a < b` |

You may have noticed that we're checking if things are equal using `==` and you may be wondering we can't use `=`. That's because `=` means "assign" not "compare". In some languages, this is valid code, but will be True when the assignment is successful or when the assigned value is not 0 rather than comparing them. Python just says "this is an error".

Remember that a boolean is just another data type, so it can be stored in a variable, just like strings or integers!

Combined with good variable names, this makes the `not` operator very nice.

For example:

```python
temp = input('What is the temperature? ')
too_hot = temp > 80

if not too_hot:
    print('We should go to the beach!')
```

### Handle 4 basic operations: + - * /

**Objective** Ask the user for two numbers, then an operation (+, -, *, or /). Then, perform the calculation and print the result.

Note: `1 / 2 = 0.5`

But an integer is a whole number, so how can this be?

There's a fourth data type you should know about: the **float** meaning a "floating-point" number. E.g. `float(1)` becomes `1.0`.
To convert a float to an int, it's as easy as `int(3.14159)`, but there's a catch. Instead of rounding, it "truncates", which is computer-speak for the mathematical floor function. I.e. `int(3.0)` = `int(3.1)` = `int(3.9)` = `int(3.999999999)` = `3`.

If you're doing division, there's a shortcut:

`1 / 2 = 0.5` but `1 // 2 = 0`

`5 / 3 = 1.6666666666666667` but `5 // 3 = 1`
* `/` is called "floating-point-division" or "float-division"
* `//` is called "integer-division" or "int-division"

Floats in computers are... weird.
Computers don't handle floats very well, especially if they have infinite digits; so don't be surprised if you see wrong math with the last digit of a float.
If you need to be precise, use integers and convert to a float later.
E.g. Instead of tracking dollars (`123.45`), track cents (`12345`) and divide by 100 later.

For this project, you only need to handle float-division, but for bonus points you can include int-division as a 5th operation.

For more bonus points, consider adding more operations, e.g. `^` for power.

### Loop

_**Objective:** Now that you can do 4+ math operations, put all of it under/inside an infinite while-loop._

There are 2 kinds of loops: **while-loops** and **for-loops**.

**For-loops** in Python act like what other languages call a _foreach-loop_, though most languages _also_ have _for-loops_ which are slightly different from Python's for-loops. That's kinda confusing so we'll cover for-loops in another project.

For now, let's only talk about **while-loops**. Simply put, while-loops loop _while_ something is True. Remember `not`?
Sometimes, the logic in a program can get confusing and it's easier to read something like `while not done:` than `while can_continue:`.

While-loops can use any boolean - a variable whose value is True or False, or a boolean operation like "==" or ">" - to determine whether to run the block of code one more time.

A fun feature is the "infinite loop" - a loop that will continuously run until you make it stop. If you're not careful, it can hog your computer's processing power and slow everything down, and is rarely the result you want anyway.

For example...
```python
while True:
    print('hello')
```
...will print "hello" to the screen infinite times, and will slow down your computer a bit while it does so.
If you run into this, press `[Ctrl + C]` on Windows & Linux or `[Command + .]` (dot/period) on Mac. This kills the program and forces it stop wherever it is in its program execution.

Python will get angry with you (something like this...)
```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```
...but if you're in an infinite loop, you just need to kill the program.

Note: if you really panick, closing the terminal also works, but then you need to set up your terminal again.

Infinite loops CAN be okay if there's something that makes it wait for the user to input... such as `input()`!

```python
while True:
    text = input('> ')
    # Do something with 'text'
```
This will accept the user's input, do something with it, then immediately ask for more input.

### Exit

_**Objective:** Modify the code inside the loop to check if the user entered the text "exit" before handling other numbers or math. If so, then exit the loop and end the program._

It's kind of annoying to have to kill the program every time. Let's add a way to exit the program "gracefully".

Example output:
> **#1>** _5_
>
> **#2>** _7_
>
> **op>** _+_
>
> **= 12**
>
> **#1>** _5_
>
> **#2>** _7_
>
> **op>** _-_
>
> **= -2**
>
> **#1>** exit
>
> **Good bye**
