"""
Rotate and array k times in either direction
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Rotate Right
def rotate(array, k, rightOrLeft=True):
    k = k % len(array)
    start = 0
    count = 0
    while count < len(array):
        do = True
        current = start
        prev = array[start]
        while start != current or do:
            if do: do = False
            next = (k * (1 if rightOrLeft else -1) + current) % len(array)
            temp = array[next]
            array[next] = prev
            current = next
            prev = temp
            count += 1
        start += 1
    return array

print("Rotating Right...")
for x in range(6):
    print(rotate([1, 2, 3, 4, 5], x))
print("Rotating Left...")
for x in range(6):
    print(rotate([1, 2, 3, 4, 5], x, False))
