""" 裝飾器範例 """
# ----------------------------- Standard Imports ----------------------------- #
import time
from functools import wraps


def timeit_decorator(func):
    """計算函數執行時間的裝飾器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} 花費時間：{elapsed_time}秒")
        return result
    return wrapper
