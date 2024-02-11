""" 函數 """
# ----------------------------- Standard Imports ----------------------------- #
from functools import reduce
# ------------------------------ 3-Praty Imports ----------------------------- #
import pydash as py_

# 1. 列表推導式
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newMaps_1 = list(map(lambda x: x * 2, arr))
newMaps_2 = py_.map_(arr, lambda x: x * 2)

print(newMaps_1)
print(newMaps_2)

# 2. 過濾器
newMaps_3 = list(filter(lambda x: x > 9, arr))
newMaps_4 = py_.filter_(arr, lambda x: x > 9)

print(newMaps_3)
print(newMaps_4)

# 3. 累加器
newMaps_5 = reduce(lambda x, y: x + y, arr)
newMaps_6 = py_.reduce_(arr, lambda x, y: x + y)

print(newMaps_5)
print(newMaps_6)

# 4. 列表推導式
newMaps_7 = [x * 2 for x in arr]
newMaps_8 = py_.map_(arr, lambda x: x * 2)

print(newMaps_7)
print(newMaps_8)

# 5. 過濾器
newMaps_9 = [x for x in arr if x > 9]
newMaps_10 = py_.filter_(arr, lambda x: x > 9)

print(newMaps_9)
print(newMaps_10)

# 6. 累加器
newMaps_11 = sum(arr)
newMaps_12 = py_.sum_(arr)

print(newMaps_11)
print(newMaps_12)
