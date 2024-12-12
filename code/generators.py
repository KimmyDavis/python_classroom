"""
generators in python
they yield values instead of returning
"""
def sq_gen(N):
    for i in range(N):
        yield(i ** 2)

ten_sqs = sq_gen(10)

print("1st ->", next(ten_sqs))
print("2nd ->", next(ten_sqs))
print("3rd ->", next(ten_sqs))
print("4th ->", next(ten_sqs))