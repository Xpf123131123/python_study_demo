# !/usr/bin/python

from Lib.prfilehooks import profile

class SampleClass:

    def silly_fibonacci_example(self, n):
        if n < 1:
            raise ValueError('n must be >= 1, got %s', n)
        if n in (1, 2):
            return 1
        else:
            return (self.silly_fibonacci_example(n - 1) +
                    self.silly_fibonacci_example(n - 2))
    silly_fibonacci_example = profile(silly_fibonacci_example)

if __name__ == '__main__':
    fib = SampleClass().silly_fibonacci_example
    print(fib(1))