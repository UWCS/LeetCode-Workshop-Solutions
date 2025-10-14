# Pretty much everything in Python is actually an object
# When objects are manipulated inside a function, they're changed outside too
# (For CS people: Python passes object references rather than copying them)

def ManipulateList(a: List[int]):
    a.append("new item")

b = ["hello"]
ManipulateList(b)
print(b)