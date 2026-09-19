# Linear search
def linear_search(arr, target): # T.C. = O(N)

    # Check every element of the array
    for num in arr:

        # If target is found
        if num == target:
            return True

    # Target was not found
    return False


# Brute force solution
def Longest_consecutive_sequence_brute(arr):   # T.C. = O(N)

    n = len(arr)

    # Stores the longest sequence found so far
    longest = 0

    # Try every element as the starting point
    for i in range(0, n):

        # Current element
        x = arr[i]

        # At least the current element itself
        # is part of the sequence
        count = 1

        # Look for the next consecutive number
        # x + 1
        while linear_search(arr, x + 1) == True: # T.C. = O(n) * o(n) = O(N^2)

            # Move to the next number
            x = x + 1

            # Increase sequence length
            count = count + 1

        # Compare current sequence length
        # with the longest sequence found so far
        longest = max(longest, count)

    return longest


arr = [102, 4, 100, 1, 1, 101, 3, 2, 2, 1, 1]

print(Longest_consecutive_sequence_brute(arr))

         



