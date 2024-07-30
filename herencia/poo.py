class Mago:
    def hechizos(self):
        return "Lanzando hechizo"

class Guerrero:
    def defensa(self):
        return "Defendiendo con escudo"

class Elfo:
    def aura(self):
        return "Aura mágica activada"

class DarkLord(Guerrero, Elfo):
    pass

darklord = DarkLord()
print(darklord.defensa()) 
print(darklord.aura())    

print(DarkLord.__mro__)

class DarkLord2(Elfo, Guerrero):
    pass

darklord2 = DarkLord2()
print(darklord2.defensa())  
print(darklord2.aura())   
print(DarkLord2.__mro__)
