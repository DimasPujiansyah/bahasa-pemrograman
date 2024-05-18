def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Fungsi untuk mencetak array
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Array yang akan diurutkan
arr = [12, 11, 13, 5, 6]

print("Array sebelum diurutkan:")
print_array(arr)

insertion_sort(arr)

print("Array setelah diurutkan:")
print_array(arr)
