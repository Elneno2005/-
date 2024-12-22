class MyClass:
    def __init__(self, name, value):
        
        self.name = name
        self.value = value
    
    def __str__(self):
    
        return f"MyClass(name={self.name}, value={self.value})"
    
    def __add__(self, other):

        if isinstance(other, MyClass):
            return MyClass(self.name + other.name, self.value + other.value)
        raise TypeError("Unsupported type for addition")
    
    def __eq__(self, other):
        
        if isinstance(other, MyClass):
            return self.name == other.name and self.value == other.value
        return False
    
    def __len__(self):

        return len(self.name)


obj1 = MyClass("Apple", 10)
obj2 = MyClass("Banana", 20)

print(obj1)  # MyClass(name=Apple, value=10)

obj3 = obj1 + obj2
print(obj3)  # MyClass(name=AppleBanana, value=30)
print(obj1 == obj2)  # False

print(len(obj1))  # 5 (طول السلسلة النصية "Apple")
