from Animal import *
obj1 = Cachorro("Totó", 50)
print("cachorro: ", obj1.getNome())
obj1.enterrarOsso()
print(obj1.getNome(), obj1.dormir())

obj2 = Galinha("Tontona", 5)
print("galinha: ", obj2.getNome())
obj2.botarOvo()
print(obj2.getNome(), obj2.dormir())