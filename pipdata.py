from camelcase import CamelCase

c = CamelCase()
txt = "a aa aaa aaaaa aa a aaa a aaa a_b a.aa am is be go"
print(c.hump(txt))
