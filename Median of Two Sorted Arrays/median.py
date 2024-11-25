class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arrays = nums1 + nums2
        arrays.sort()
        length = len(arrays)
        middle_index = len(arrays) // 2
        if length % 2 != 0:
            middle_element = arrays[middle_index]
            return middle_element
        elif length % 2 == 0:
            last_two = arrays[middle_index - 1:middle_index + 1]
            median = sum(last_two) / 2.0 
            return median