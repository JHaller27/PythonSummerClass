_[Download solution](solution.py)_

# CSV Math

So here's the scenario: you work for a small personal financial planning company.
This morning you received an email from Robin in marketing:

> Hey!
>
> We're talking about running an ad and we want to include how much our clients' assets have increased from our services per year over the past 5 years (2014-2019, since 2020 isn't over and numbers will be weird anyway).
Abby is working on finding a baseline - the average amount people's assets increase for comparison,
and Dayna found a bunch of spreadsheets of customer data
(with personal info redacted, mostly just the names have been converted into random ids).
>
> As you can imagine, there are a LOT of files to go through,
so I'm really hoping your programming skills will come in useful here!
I've attached a .zip file with the spreadsheets (they're .csv files instead of .xlsx, I hope that's okay).
Also, the transactions in each file aren't sorted at all.
Normally we can sort by date, but Dayna says the UI is buggy and it won't let her download them sorted.
>
> Let me know if there's anything I can help you with. Thanks a ton!<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Robin


## Phase 1: Read file

_[Download data file](data/phase_1.txt)_

**Objective**: Read `data/phase_1.txt` which contains a list of numbers, and print the sum of those numbers.

> Tip: Use the provided solution to check your answer.

---

Even if you haven't opened and manipulated files in Python,
it's super easy.

```python
filename = "somefile.txt"

fin = open(filename)
# fin is a common abbreviation for file-in
# (and fout is short for file-out)

for line in fin:
    print(line)

fin.close()
```

This short program opens a file (for reading, you can't write to it), then loops over each line in the file, and prints it.

Although Python will usually close the file for you, sometimes things don't go as planned and the program will end before the computer knows that the file is done being used.
Thus, next time you try to open it, the computer won't let it happen. It's rare, but it's super annoying when it happens.

Instead of the open/close process, a shorter way to do it is:

```python
with open(filename) as fin:
    for line in fin:
        print(line)
```

The `with` statement will automatically close the file for you at the end of its block. If you need to do more complex things with the files, and there aren't too many lines in the file, you can do something like this:

```python
lines = []
with open(filename) as fin:
    for line in fin:
        lines.append(line)
do_something(lines)
```

This will read each line of the file, insert it into the `lines` list, then close the file.
Now you can `do_something()` with those lines and the file is open only for a short time, which is generally best, especially if you need to force-kill the program in the middle (which often happens while developing).

## Phase 2: Read CSV

_[Download data file](data/phase_2.csv)_

**Objective**: Read a CSV, and calculate the net profit.

Read data from `data/phase_2.csv` using the CSV library,
and calculate the net profit.

_Resource: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html) - Python documentation on the builtin `csv` library._

---

A CSV file (which stands for "Comma-Separated Values" file) is really no different from a .txt file.
However, it IS special in that it has a consistent, well-known format.

Computers are really good at handling data that is **consistent** (because it can repeat one process many times, very fast),
and the "**well-known**" means that there's probably someone out there that has written helpful code for us.

In fact, CSV files are so well known, that Python has a builtin library (cleverly called `csv`) for handling them.

The csv library has Readers and Writers (these are "Classes", if you don't know what that means, feel free to check them out on your own, but the details don't matter for this project).
In this project, we'll only use Readers, but similar concepts will apply to Writers.

csv.Readers accept an already-opened file, and do some fancy things for us in the background. For example:

```python
import csv

# Read the csv file, and store each row in a list
rows = []
with open(filename) as fin:
    reader = csv.Reader(fin)  # Btw, csv.Reader is a Class
    for row in reader:
        rows.append(row)

# Do_something with each cell
for row in rows:
    for cell in row:
        do_something(cell)  # Each cell is a string
```

We could easily write this ourselves by reading line-by-line, and using `line.split(',')` before appending to the list of rows, but it's kinda nice that we don't have to.
Plus, sometimes CSV files have slightly different formats that this library handles well (though this project will only use the default CSV format to keep things simple).

Here's where the csv library becomes super useful: `csv.DictReader`. The DictReader works exactly the same as a Reader, but instead of producing a list of rows, which are _lists of cells_ (as in the `csv.Reader` example),
each row is a _dict of cells_ where the keys are the columns (we can set the column names ourselves, or let the `DictReader` read them from the first row).

For example...
```python
import csv

# Read the csv file, and store each row in a list
rows = []
with open(filename) as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        rows.append(row)

# Do_something with each row's cells
for row in rows:
    do_something(row['Column 1'], row['Column 2'], ...)
```

Clearly, there are better ways for `do_something()` to work, but this should illustrate that each `row` is a _dict_ and you can access each cell by its column name.

It's up to you to decide the best to improve `do_something()` but here are some suggestions.

1. Pass the entire row, and let `do_something()` sort it out.

```python
# Do_something with each row
for row in rows:
    do_something(row)

def do_something(row):
    return row['Column 1'] + row['Column 2'] - row['Column 3']
```

This is nice because we only have to pass the row (1 parameter), but if we want to run `do_something()` on its own for testing, we have to construct the `row` dict param.

2. The function expects each cell separately (as in the example), but we can _dereference_ the row.

```python
# Do_something with each row
for row in rows:
    do_something(**row)
    # We use ** for dicts (matching params by name)
    #  but we can do something similar with tuples using *
    #  (matching params by position/order)

def do_something(column1, column2, column3):
    return column1, column2, column3
```

This is nice because testing is slightly easier because we can pass in each parameter and know exactly what it is without needing to build a dict first
(e.g. `do_something(1, 2, 3)`).
However, it's not scalable - e.g. what happens if we have 20 columns? - and it requires that the column names follow Python variable naming rules (e.g. 'Column1' is fine but 'Column 1' would not work for this example).

For this particular project, either option will work equally well.
So use the second option if you want to experiment, but option 1 generally works better.

Pro tip: If you ever have a function that has way too many parameters, passing in a dict can clean it up significantly.
It's very rare that this is helpful, because the function usually should instead be split into more, smaller functions.
(In fact, CS/math theory says that _any_ program can be minimally written as a composition of functions that accept 1-2 parameters.
So it's always _possible_ to simplify functions that need 3+ parameters.
6 parameters is usually the point at which you should think about splitting the function).

However, passing Objects (instead of dicts) is very common, very clean, and generally preferred with newer practices - called Object-Oriented Design (OOD).

## Phase 3: Lots of files + math!

_[Download zip file](data/phase_3_reports.zip)_

**Objective**: Read from many CSV files, find the net profit for each "client file", then find the average net profit overall.

This is more of a real-world example.
Now that you can read files, and handle CSV files, let's do something "interesting" with it.

The scenario described at the start of these instructions say that
you'll have a .zip file containing MANY CSV files.
Each CSV file represents client data (with personally-identifiable information redacted).

Each CSV file is named as 'report-{year}-{uid}.csv' where {year} is the year the client's record starts, and {uid} is the client's unique id (instead of their name).

Each client file has 4 columns - year, month, day, and amount.
Year/month/day represents the date of a transaction,
and the amount is the amount of that transaction.
Negative transactions represent financial loss (a purchase, etc.),
and positive transactions represent financial gains (income, etc.).

Not all of this information is necessary, e.g. the name of the file doesn't much matter, and we only care about the year the transaction was made (the exact day doesn't matter).

You're only interested in accumulating transactions occurring during the years 2014-2019 (inclusive).

Since you don't know the exact names of the files
and it would be ridiculous to expect you to type them all out,
here's a function that will list all files in a given directory
(plus example usage).
Copy+paste this at the top of your program, or use it as a base to start from.

```python
import os


def list_files(directory_name):
    '''
    Generator function that returns the names of all files in a directory
    '''
    for f in os.listdir(directory_name):
        full_path = os.path.join(directory_name, f)
        if os.path.isfile(full_path):
            yield full_path


# Example usage
for file in list_files('/home/jhaller/Documents/project2/data/reports'):
    do_something_with(file)
```

_[Code credit](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)_

To clarify, what we're looking for is this:
* For each file, for each year, find the sum of all transactions
* Calculate and print the average of all of these sums, i.e. the sum of each year's sum for each file

As always, feel free to run the solution code to check your results.

You may also consider working incrementally:
* Open one file (one way is to use `filename = next(list_files(...)))` to get only the first file)
* List/print all transactions in the year range
* Find the sum of those transactions
* Repeat for a second file, and find the average
* Replace "handle file 1 + handle file 2" with for-looping over all files
