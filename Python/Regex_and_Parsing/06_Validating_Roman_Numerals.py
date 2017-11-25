import re
s = input()
exp = '^M{0,3}(CM|DC{0,3}|CD|C{0,3})(XC|LX{0,3}|XL|X{0,3})(IX|VI{0,3}|IV|I{0,3})$'
exp = re.compile(exp)
print(bool(exp.search(s)))
