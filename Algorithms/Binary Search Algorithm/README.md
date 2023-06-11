### Usage

You are able to run all of the Algorithms like this:

```bash
python3 BinarySearch.py
```

---

### Binary Search Algorithm (BSA)

Here you can use the simplified BSA algorithm:

```python

def binary_search(number, array):
    if not array:
        return False

    middle_index = len(array) // 2
    middle_item = array[middle_index]

    if number == middle_item:
        return True
    elif number < middle_item:
        return binary_search(number, array[:middle_index])
    else:
        return binary_search(number, array[middle_index + 1:])

```

Run sample code:

```bash
python3 BinarySearch.py
```