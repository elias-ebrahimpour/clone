def non_binary_search(number: int, unlisted_array: list[int]):
    for item in unlisted_array:
        if number == item:
            print(item)



def main():
    non_binary_search(9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == "__main__":
    main()