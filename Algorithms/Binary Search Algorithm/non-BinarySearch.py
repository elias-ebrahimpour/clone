def non_binary_search(number: int, array: list[int]):
    for item in array:
        if number == item:
            print(item)



def main():
    non_binary_search(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == "__main__":
    main()