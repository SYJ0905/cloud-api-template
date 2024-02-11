""" collections module """
# ----------------------------- Standard Imports ----------------------------- #
from collections import (
    Counter,
    defaultdict,
    namedtuple, OrderedDict
)
# collections 是 Python 標準庫中的一個模組，提供了許多有用的集合類型。
# 這些類型是 Python 內建類型 dict、list、set 和 tuple 的替代選擇。


# namedtuple
Student = namedtuple("Student", ["name", "age"])
student1 = Student("Cloud", 30)
print(student1.name, student1.age)
# 這個類似於一個簡單的類定義，但是它的實例是不可變的。
# 這使得它更加輕量和高效，並且更容易理解和使用。


# defaultdict
word_list = ["is", "who", "when", "it", "is", "who", "is"]
result_dict = dict()

for word in word_list:
    result_dict.setdefault(word, 0)
    result_dict[word] += 1

print("result_dict:", result_dict)


# defaultdict
result_defaultdict = defaultdict(int)
for word in word_list:
    result_defaultdict[word] += 1

print("result_defaultdict:", result_defaultdict)


# Counter
result_counter = Counter(word_list)
print("result_counter:", result_counter)
print(result_counter.most_common(1))


# OrderedDict
d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
d.move_to_end("a")
print(d)
