import timeit

class test1:
    def test_perf_dict(self):
        first = timeit("s = dict(name='catherine', shares=100, price=100)" )
        print(first)
        ## 0.291458129883
 
        second = timeit("s = {'name':'catherine', 'shares':100, 'price':100}" )
        print(second)
        ## 0.140990972519

        print(id(self))

test = test1()
test.test_perf_dict()
print(id(test))

