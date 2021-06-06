fn1 = 1
fn2 = 1

n = input()
print("fabonacci series is ")
print(fn1)
print(fn2)
for i in range(3,int(n)):
    fn = fn1 + fn2
    print(fn)
    fn1 = fn2
    fn2 = fn
