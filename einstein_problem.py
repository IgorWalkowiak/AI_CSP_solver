
COLORS = ['ZOLTY', 'NIEBIESKI', 'CZERWONY', 'ZIELONY', 'BIALY']
NATIONS = ['NORWEG', 'DUNCZYK', 'ANGLIK', 'NIEMIEC', 'SZWED']
LIQUITS = ['WODA', 'HERBATA', 'MLEKO', 'KAWA', 'PIWO']
SMOKES = ['CYGARO', 'LIGHT', 'BEZ_FILTRA', 'FAJKA', 'MENTOL']
PETS = ['KOT', 'KON', 'PTAK', 'RYBA', 'PIES']

vars = [(COLORS[i % 5],
        NATIONS[int((i/5)) % 5],
        LIQUITS[int((i/25)) % 5],
        SMOKES[int((i/125)) % 5],
        PETS[int((i/625)) % 5])
       for i in range(5*5*5*5*5)]


class Einstein_problem:
    def __init__(self):
        self.domain = vars
        self.variables = list(range(1, 6))

    def constrains_function(self, assignments):


        #1. Norweg zamieszkuje pierwszy dom
        try:
            if assignments[1][1] != 'NORWEG':
                #print("1")
                return False
        except:
            pass


        #2. Anglik mieszka w czerwonym domu
        for house in assignments.values():
            if house[1] =='ANGLIK' and house[0] !='CZERWONY':
                #print("2")
                return False


        #3. Zielony dom znajduje się bezpośrednio po lewej stronie domu białego.
        if assignments[1][0] =='BIALY':
            #print("3")
            return False
        try:
            for x in range(2,6):
                if assignments[x][0] == 'BIALY' and assignments[x-1][0] != 'ZIELONY':
                    #print("3")
                    return False
        except:
            pass

        #4. Duńczyk pija herbatkę.
        for house in assignments.values():
            if house[1] =='DUNCZYK' and house[2] !='HERBATA':
                #print("4")
                return False

        #5. Palacz papierosów light mieszka obok hodowcy kotów.
        for house in assignments.values():
            if house[3] =='LIGHT' and house[4] =='KOT':
                return False

        inFront = True
        frontChecked = False

        inBack = True
        backChecked = False
        try:
            for x in range(2,6):
                if assignments[x][3] == 'LIGHT' and assignments[x-1][4] != 'KOT':
                    backChecked = True
                    inBack = False
                    break
        except:
            pass

        try:
            for x in range(1,5):
                if assignments[x][3] == 'LIGHT' and assignments[x+1][4] != 'KOT':
                    frontChecked = True
                    inFront = False
                    break
        except:
            inFront = True


        if (backChecked and not inBack and not frontChecked) or (frontChecked and not inFront and not frontChecked) or ((backChecked and frontChecked) and (not inFront and not inBack)):
            #print("5")
            return False




        #6. Mieszkaniec żółtego domu pali cygara.
        for house in assignments.values():
            if house[0] =='ZOLTY' and house[3] !='CYGARO':
                #print("6")
                return False

        #7. Niemiec pali fajkę
        for house in assignments.values():
            if house[1] =='NIEMIEC' and house[3] !='FAJKA':
                #print("7")
                return False





        #8. Mieszkaniec środkowego domu pija mleko
        try:
            if assignments[3][2] !='MLEKO':
                #print("8")
                return False
        except:
            pass

        #9. Palacz papierosów light ma sąsiada, który pija wodę.
        for house in assignments.values():
            if house[3] =='LIGHT' and house[2] =='WODA':
                return False

        inFront = True
        frontChecked = False

        inBack = True
        backChecked = False
        try:
            for x in range(2, 6):
                if assignments[x][3] == 'LIGHT' and assignments[x - 1][2] != 'WODA':
                    backChecked = True
                    inBack = False
                    break
        except:
            pass

        try:
            for x in range(1, 5):
                if assignments[x][3] == 'LIGHT' and assignments[x + 1][2] != 'WODA':
                    frontChecked = True
                    inFront = False
                    break
        except:
            inFront = True

        if (backChecked and not inBack and not frontChecked) or (frontChecked and not inFront and not frontChecked) or ((backChecked and frontChecked) and (not inFront and not inBack)):
            #print("9")
            return False


        #10.Palacz papierosów bez filtra hoduje ptaki
        for house in assignments.values():
            if house[3] =='BEZ_FILTRA' and house[4] !='PTAK':
                #print("10")
                return False


        #11.Szwed hoduje psy.
        for house in assignments.values():
            if house[1] =='SZWED' and house[4] !='PIES':
                #print("11")
                return False

        #12.Norweg mieszka obok niebieskiego domu
        for house in assignments.values():
            if house[1] =='NORWEG' and house[0] =='NIEBIESKI':
                return False

        inFront = True
        frontChecked = False

        inBack = True
        backChecked = False
        try:
            for x in range(2, 6):
                if assignments[x][1] == 'NORWEG' and assignments[x - 1][0] != 'NIEBIESKI':
                    backChecked = True
                    inBack = False
                    break
        except:
            pass

        try:
            for x in range(1, 5):
                if assignments[x][1] == 'NORWEG' and assignments[x + 1][0] != 'NIEBIESKI':
                    frontChecked = True
                    inFront = False
                    break
        except:
            inFront = True

        if (backChecked and not inBack and not frontChecked) or (frontChecked and not inFront and not backChecked) or ((backChecked and frontChecked) and (not inFront and not inBack)):
            #print("12")
            return False


        #13.Hodowca koni mieszka obok żółtego domu
        for house in assignments.values():
            if house[4] =='KON' and house[0] =='ZOLTY':
                return False

        inFront = True
        frontChecked = False

        inBack = True
        backChecked = False
        try:
            for x in range(2, 6):
                if assignments[x][4] == 'KON' and assignments[x - 1][0] != 'ZOLTY':
                    backChecked = True
                    inBack = False
                    break
        except:
            pass

        try:
            for x in range(1, 5):
                if assignments[x][4] == 'KON' and assignments[x + 1][0] != 'ZOLTY':
                    frontChecked = True
                    inFront = False
                    break
        except:
            inFront = True


        if (backChecked and not inBack and not frontChecked) or (frontChecked and not inFront and not frontChecked) or ((backChecked and frontChecked) and (not inFront and not inBack)):
            #print("13")
            return False


        #14.Palacz mentolowych pija piwo.
        for house in assignments.values():
            if house[3] =='MENTOL' and house[2] !='PIWO':
                #print("14")
                return False

        #15.W zielonym domu pija się kawę.
        for house in assignments.values():
            if house[0] =='ZIELONY' and house[2] !='KAWA':
                #print("15")
                return False



        col =[]
        nat =[]
        liq =[]
        smo =[]
        pet =[]
        for assignment in assignments.values():
            if col.count(assignment[0]) == 0:
                col.append(assignment[0])
            else:
                return False
            if nat.count(assignment[1]) == 0:
                nat.append(assignment[1])
            else:
                return False
            if liq.count(assignment[2]) == 0:
                liq.append(assignment[2])
            else:
                return False
            if smo.count(assignment[3]) == 0:
                smo.append(assignment[3])
            else:
                return False
            if pet.count(assignment[4]) == 0:
                pet.append(assignment[4])
            else:
                return False


        return True