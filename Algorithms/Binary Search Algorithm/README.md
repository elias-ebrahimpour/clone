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

Time Complexity:

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(log n)   |
| Worst Case   | O(n)       |

---

### Linear Search Algorithm (LSA)

Here you can use the simplified LSA algorithm:

```python

def linear_search(number, array):
    for item in array:
        if number == item:
            return True
    return False

```

Run sample code:

```bash
python3 LinearSearch.py
```

Time Complexity:

| Case         | Complexity |
| ------------ | ---------- |
| Best Case    | O(1)       |
| Average Case | O(n)       |
| Worst Case   | O(n)       |
