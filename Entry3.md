<link rel="stylesheet", href="index.css">

# Finding files ending in a certain extension (python) {#gradient}

---

Okay, So you're just making a server just as normal programmers do, but then you want to find files with certain extensions. No places you seem to search provide an easy way to do this.

Here is the solution:

- First import the glob module

```python
import glob
```

- Then look for the files you want (i.e .py files)

```python
import glob
files = glob.glob('*.py')
# do something with files
```

[Previous Page](Entry2.md) [Next Page](Entry4.md)
