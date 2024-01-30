# Selection Sort


class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr) - 1):
            minimum = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    minimum = j
            if i != minimum:
                arr[i], arr[minimum] = arr[minimum], arr[i]

        return arr


test = Solution()
print(test.selection_sort([64, 25, 12, 22, 11]))
