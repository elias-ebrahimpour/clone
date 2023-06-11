def binary_search(number: int, array: list[int]) -> bool:
    """
    This is an example code for Binary Search in python
    """
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



def main():
    print(binary_search(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))   # Will returns "True"
    print(binary_search(66, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Will returns "False"

if __name__ == "__main__":
    main()