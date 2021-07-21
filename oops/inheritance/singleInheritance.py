class Father:
    fatherProprety = 10_00_000

    def faterMethod(fatherProprety):
        print("total father's property: ", Father.fatherProprety)


class Son(Father):
    sonProperty = Father.fatherProprety+50_000

    def sonMethod(sonProperty):
        print(
            "property of son is father's property and son's own property: ", Son.sonProperty)


property = Son()
property.sonMethod()
property.faterMethod()
