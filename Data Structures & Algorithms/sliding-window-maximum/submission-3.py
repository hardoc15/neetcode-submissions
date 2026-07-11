import numpy as np

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_arr = np.array(nums)

        # This creates the matrix of windows you described
        # Shape will be (len(nums) - k + 1, k)
        shape = (nums_arr.size - k + 1, k)
        strides = (nums_arr.itemsize, nums_arr.itemsize)
        window_matrix = np.lib.stride_tricks.as_strided(
            nums_arr, shape=shape, strides=strides
        )

        # Call the max function just one time total across the rows (axis=1)
        return np.max(window_matrix, axis=1).tolist()
        