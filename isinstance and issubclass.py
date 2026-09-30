class Animal:
    pass

class Tiger(Animal):
    pass
 
t = Tiger()

print(isinstance(t, tiger))
print(isinstance(t, Animal))
print(issubclass(Tiger, Animal))
