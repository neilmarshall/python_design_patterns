from copy import deepcopy

class Book():
    def __init__(self, title, author, **kwargs):
        self.title = title
        self.author = author
        self.__dict__.update(kwargs)

    def __repr__(self):
        args = ", ".join(f"{k}={self.__dict__[k]}" for k in sorted(self.__dict__.keys()) if k not in {"title", "author"})
        return f"""Book({self.title}, {self.author}{", " + args if args else ""})"""


class Prototype():
    def __init__(self):
        self.objects = dict()

    def register(self, obj):
        self.objects[id(obj)] = obj

    def deregister(self, obj_id):
        del self.objects[obj_id]

    def clone(self, obj, **attrs):
        if id(obj) not in self.objects:
            raise ValueError(f"Object ID '{id(obj)}' not recognised")
        obj = deepcopy(self.objects[id(obj)])
        obj.__dict__.update(attrs)
        return obj


if __name__ == '__main__':
    b1 = Book("test title", "test author", isbn="1234-5678")
    proto = Prototype()
    proto.register(b1)
    b2 = proto.clone(b1, pages=424)
    print(id(b1), "::", b1)
    print(id(b2), "::", b2)
