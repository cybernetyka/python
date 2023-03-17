
# Materia (proporcje relacji cech)
class Property:

    # typ:  wygląd
    # relacja: czarny/biały
    # proporcja: 2/3 dotyczy pierwszego elementu relacji, drugi ma 1/3

    def __init__(self, type, relation, proportion):
        self.type = type
        self.relation = relation
        self.proportion = proportion

    # sprawdz czy zawiera typ, sumowanie proporcji i relacji
    # dodaj jesli nie ma typu i relacji
    # jesli istnieje to zmien wagi proporcji
    def add(self, Property):
       # if(Property.relation != self.relation) {
       # self.type = Property.type
       # self.relation = Property.relation
       # self.proportion = Property.proportion
       # } else {
       # self.type = Property.type
       # self.relation = Property.relation
       # self.proportion = Property.proportion
       # }


# Biton - Zbiór relacji
class Biton:

    def __init__(self):
        self.property = []

    def addProperty(self, Property):
        self.property.append(Property)

    # sprawdz czy zawiera typ, sumowanie proporcji i relacji
    # dodaj jesli nie ma typu i relacji
    # jesli istnieje to zmien wagi proporcji

    ## Jeśli znajdzie już istniejące, to nie zastępuje, tylko dopisuje i potem liczy wagę dynamicznie

    def sum(self, Property):
        list_similiar_types = self.property.find(Property.type)

        for Property2 as list_similiar_types:
           # if(Property2.relation === self.property.find(Property.relation).relation){ # if TYPE && RELATION
           # self.property.find(Property.type).sum(Property)
           # else {
           # self.property.find(Property.type).
           # }

    def listProperty(self):
        ## calculate the proportions dynamic        
        return self.property

    def calcProperty(self):
        ## calculate the proportions dynamic,
        # za każdym razem, gdy już istnieje porperty z tym samym typem i relacją, zmieniaj proporcje biorąc pod uwagę ilośc prób, porporcja = nowa proporcja  = jeśli proporcja mniejsza to odejmij, jeśli większa to zwiększ, ale wczesniej podziel przez ilość prób 
        return self.property

    def filter(self, key):
        #properties()->filtrowanie(energia)

    # find array of Objects another object with param 
    #def filter(self, key)


# properties()->filtrowanie(energia)      


# CoBit - świadomy organizm, składa się z materii z Bitonów
class Cobit:

    def __init__(self):
        self.biton = []

    def addBiton(self, Biton):
        self.biton.append(Biton)
        # sprawdz czy zawiera typ, sumowanie proporcji i relacji
        # dodaj jesli nie ma typu i relacji
        # jesli istnieje to zmien wagi proporcji

    def listBiton(self):
        return self.biton

    def listType(self):
        return self.biton # get        all        types        of        biton
    def listProperty(self, key)
        #return self.biton.filter()->filtrowanie(energia) #
        # grupuj        po        typach, zmien        proporcje, jesli        typy        i        relacje        są        te        same


Property1 = Property()
Property2 = Property()

Biton1 = Biton(Property1)
Biton2 = Biton(Property2)

ListBiton = [Biton1, Biton2]

myCobit = Cobit()
myCobit.addBiton(Biton1)
print( Cobit.values() )


for Biton  ListBiton:
  CoBit.addBiton(Biton)

print( CoBit.listProperty() )