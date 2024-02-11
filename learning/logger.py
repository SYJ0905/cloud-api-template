""" logger 模組"""

# print 使用優劣
# 1. print 可以直接印出變數的值
# 2. print 不能紀錄日誌
# 3. print 不能指定輸出位置
# 4. print 不能指定輸出格式
# 5. print 不能指定輸出等級
# 6. print 不能指定輸出時間
# 7. print 不能指定輸出檔案
# 8. print 不能指定輸出檔案大小
# 9. print 不能指定輸出檔案數量
# 10. print 不能指定輸出檔案格式
# 11. print 不能指定輸出檔案位置
# 12. print 不能指定輸出檔案等級
# 13. print 不能指定輸出檔案時間

# logging 使用優劣
# 1. logging 可以紀錄日誌
# 2. logging 可以指定輸出位置
# 3. logging 可以指定輸出格式
# 4. logging 可以指定輸出等級
# 5. logging 可以指定輸出時間
# 6. logging 可以指定輸出檔案
# 7. logging 可以指定輸出檔案大小
# 8. logging 可以指定輸出檔案數量
# 9. logging 可以指定輸出檔案格式
# 10. logging 可以指定輸出檔案位置
# 11. logging 可以指定輸出檔案等級
# 12. logging 可以指定輸出檔案時間
# 13. logging 不能直接印出變數的值


# ----------------------------- Standard Imports ----------------------------- #
import logging

# 設置日誌的配置。這將配置root logger。
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    # filename='app.log',  # 將日誌消息輸出到名為app.log的文件
                    # filemode='w',  # 'w'代表寫模式，每次啟動都會覆蓋文件。用'a'代表追加模式。
                    encoding='utf-8')  # 指定文件編碼為utf-8

# 創建一個自定義的logger
logger = logging.getLogger('my_logger')

# 使用不同的日誌級別來記錄消息
logger.debug('這是一個 debug 等級的日誌消息')
logger.info('這是一個 info 等級的日誌消息')
logger.warning('這是一個 warning 等級的日誌消息')
logger.error('這是一個 error 等級的日誌消息')
logger.critical('這是一個 critical 等級的日誌消息')

# 這將只將警告及以上級別的日誌輸出到控制台，因為預設級別是WARNING。
# 所有級別的日誌都會寫入到文件中，因為我們將文件的日誌級別設置為DEBUG。
