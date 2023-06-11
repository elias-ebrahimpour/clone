def linear_search(number: int, array: list[int])-> bool:
    """
    This is an example code for Linear Search in python
    """
    for item in array:
        if number == item:
            return True
    return False



def main():
    print(linear_search(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))    # Will returns "True"
    print(linear_search(29, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))   # Will returns "False"

if __name__ == "__main__":
    main()