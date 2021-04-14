from importlib._bootstrap import ModuleSpec
from importlib._bootstrap_external import SourceFileLoader
from mymodule import human


# print(mymodule.greeting())
# a = mymodule.human["name"]
a = human["name"]
# print(a)
# print(mymodule.human)
print(human)
# mymodule.human["name"] = "Parvane"
human["name"] = "Parvane"
# print(mymodule.human)
print(human)
# print(dir(mymodule))
# print(type(mymodule.greeting()))
# for i in dir(mymodule):
#     print(i)
#     func = getattr(mymodule, i)
#     if callable(func):
#         print(func())
#     elif isinstance(func, (dict, str, SourceFileLoader, ModuleSpec)):
#         print(func)
#     elif not func:
#         print("object is None")
#     else:
#         print("What the F*** happened?")


