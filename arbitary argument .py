# def fun(*x):
#     for i in x:
#         print(i)
# fun(1,2,3,4)
# fun(7,5)
# fun("khushbu","katyura")


# def fun(*y):
#     for i in y:
#         print(i)
# fun("khushbu","katyura")
# fun("ayushi","sharma")
# fun("tanu","kumari")
# fun("usha","bisht")

def add(*b):
    result=0
    for i in b:
        result=result+i
    print(result)
add(1,2,2,3,4,89)
