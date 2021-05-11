
from scrapy.cmdline import execute

import sys
import os

# sys.path 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# 比如import引入模块的时候就会在sys.path的目录中查找相应的模块
# sys.path 返回值是一个list,则我们如果想导入一个自定义模块下面的的包或者是模块则可以使用list的append方法增加相应的路径。

# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.split(path)  将path分割成目录和文件名二元组返回

# __file__是当前文件的绝对路径
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 在scrapy中，为了避免每一次运行或调试都输入一串命令，可以在项目文件下新建一个.py文件，每次运行爬虫只需要运行此脚本即可。且运行调试模式也需要设置此启动脚本。
# execute的参数是一个列表
execute(["scrapy","crawl","dangdang"])
