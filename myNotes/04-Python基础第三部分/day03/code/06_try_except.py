

# 此示例示意try-except语句的用法

def div_apple(n):
    print('%d个苹果您想分给几个人?' % n)
    s = input('请输入人数: ')
    cnt = int(s)  # <<= 可能触发ValueError错误异常
    # 以下一行可能触发ZeroDivisionError错误异常
    result = n / cnt
    print("每人个分了", result, '个苹果')

# 以下是调用者
# 我try-except语句来捕获并处理 ValueError类型的错误
try:
    print("开始分苹果")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('div_apple内出现了ValueError错误，已处理')
    print('用户输入不合法，苹果退回来不分了')
except:
    print("除ValueError类型的错误外,其它错误都可以被捕获")

print("程序正常退出")