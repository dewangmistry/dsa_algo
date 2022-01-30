def binary_search(numbers, number_to_find):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if number_to_find < mid_number:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1

# Function to find index of all occurences of a number in a sorted list
def find_all_occurences(numbers, number_to_find):
    mid_index = binary_search(numbers, number_to_find)
    output = [mid_index]
    left_index, right_index = mid_index - 1, mid_index + 1

    while numbers[left_index] == number_to_find:
        output.append(left_index)
        left_index -= 1

    while numbers[right_index] == number_to_find:
        output.append(right_index)
        right_index += 1

    return sorted(output)
        
# main function
if __name__ == "__main__":
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    index = binary_search(numbers, number_to_find)
    all_index = find_all_occurences(numbers, number_to_find)
    print(f"Number {number_to_find} found at index {index}")
    print(f"Number {number_to_find} found at index {all_index}")