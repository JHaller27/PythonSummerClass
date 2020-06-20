_[Download solution](solution.py)_

# CSV Math

So here's the scenario: you work for a small personal financial planning company.
This morning you received an email from Robin in marketing:

> Hey!
>
> We're talking about running an ad and we want to include how much our clients' assets increase from our services.
Abby is working on finding a baseline - the average amount people's assets increase for comparison,
and Dayna found a bunch of spreadsheets of customer data
(with personal info redacted, mostly just the names have been converted into random ids).
> 
> As you can imagine, there are a LOT of files to go through,
so I'm really hoping your programming skills will come in useful here!
I've attached a .zip file with the spreadsheets (they're .csv files instead of .xlsx, I hope that's okay).
>
> Let me know if there's anything I can help you with. Thanks a ton!<br/>
> &nbsp;&nbsp;&nbsp;&nbsp;Robin


## Phase 1: Read file

**Objective**: Read a file with a list of numbers and print the sum.

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


_Resource: https://docs.python.org/3/library/csv.html - Python documentation on the built-in CSV library_

## Phase 3: Sanitize

## Phase 4: Math!

