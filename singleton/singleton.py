class Singleton():
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance
        return cls._instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)