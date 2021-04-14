import datetime

# print(dir(datetime))
# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)
# print(datetime.date.today())
# print(datetime.datetime.now())
from importlib._bootstrap import ModuleSpec
from importlib._bootstrap_external import SourceFileLoader

a = datetime.datetime.now()
# print(type(a))
# print(a.now())
# print(a.date())
# print(a.ctime())
# print(a.day)
# print(a.today())
# print(a.year)
# print(a.month)
# print(a.astimezone())
# print(dir(a))
# for i in dir(a):
#     print(i)
#     print(type(i))
#     func = getattr(a, i)
#     print(type(func))
#     print(callable(func))
#     if callable(func):
#         print("===========")
#         continue
#     elif isinstance(func, (dict, str, int, SourceFileLoader, ModuleSpec)):
#         print(func)
#     elif not func:
#         print("object is None")
#     else:
#         print("What the F*** happened?")
#
#     print("======")

# print(a.strftime("%c/ %a/ %A/ %b/ %B/ %C/ %d/ %D"))
b = datetime.datetime(2020, 2, 10, 12, 34, 56)
print(b)



