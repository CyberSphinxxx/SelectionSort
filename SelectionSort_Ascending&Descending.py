print("Submitted by: John Lemar Gonzales & Jhun Lloyd Boyles")
print("BSIT1-R10 DSA\n")

separator = "------------------------------------"
arr = [int(x) for x in input("Enter 10 numbers separated by spaces:").split()]

print("Ascending Order:")
print(separator)

n = len(arr)
for i in range(n):
    minimum_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[minimum_index]:
            minimum_index = j
    print(arr)
    arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

print(separator)

print("\nDescending Order:")
print(separator)

n = len(arr)
for i in range(n):
    minimum_index = i
    for j in range(i + 1, n):
        if arr[j] > arr[minimum_index]:
            minimum_index = j
    print(arr)
    arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

print(separator)
