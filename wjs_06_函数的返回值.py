def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2
    # 调用函数，并使用 result 变量接收计算结果
    return result
    # 注意：`return` 表示返回，后续的代码都不会被执行


# 利用变量接收返回结果
sum_result = sum_2_num(50, 100)

print("计算结果：%d" % sum_result)
