""" 異常處理 """


def readable_error(e, file_name):
    """ 將錯誤訊息轉換成可讀的格式 """

    # print("e:", e)
    # print("type(e).__name__:", type(e).__name__)
    # print("e.__traceback__:", e.__traceback__)
    # print("e.__traceback__.tb_lineno:", e.__traceback__.tb_lineno)
    # print("file_name:", file_name)
    # print("e:", e)

    formatted_message = f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {file_name}: {e}"
    return formatted_message


a = [10, 4, 4, 7, 11, 6, 1, 9, 22, 0]

# 基本的異常處理
try:
    b = [item for item in a if 100 % item == 0]
    print(b)

except Exception as exc:
    formatted_error_message = readable_error(exc, __file__)
    print(formatted_error_message)

print("程式繼續執行")


class MyException(Exception):
    """自訂異常類別"""

    def __init__(self, message):
        super().__init__(message)


# 自訂異常處理
try:
    raise MyException("這是自訂的異常")
except MyException as exc:
    print("exc:", exc)
    formatted_error_message = readable_error(exc, __file__)
    print(formatted_error_message)
