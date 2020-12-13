nums_in_list = [1, 45, 12, 32, 6, 8]
nums_in_tuple = {5, 12, 6, 4, 18, 1}
sym_diff = nums_in_tuple.symmetric_difference(nums_in_list)
diff = nums_in_tuple.difference(nums_in_list)
result = sym_diff.difference(diff)
print(result)
