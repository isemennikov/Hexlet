from timeit import timeit

data = [i for i in range(10 ** 4)]

def method1(nums):
    lst = []
    for i in nums:
        if i % 2 == 0:
            lst.append(i)
    return lst
def method2(nums):
    return [i for i in nums if i  % 2 == 0]

repeat = 10_000
for_time = timeit (lambda: method1(data), number=repeat)
gen_time = timeit(lambda: method2(data), number=repeat)

print(f'Цикл выполняется за {for_time:.f} секунд')
print(f'Генераторное вврожение выполняется за {grn_time:.2f} секунд')
