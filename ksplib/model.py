# classes

class Kerbals:
    def __init__(self, kerbals):
        self.kerbals = kerbals

    # get a list of kerbals per state
    def getKerbals(self,states=["all"]):
        result=[]

        if "all" in states:
            return self.kerbals
        else:
            for kerbal in self.kerbals[:]:
                if kerbal.state in states:
                    result.append(kerbal)

        return result


    # get a single kerbal by name
    def getKerbal(self,name):
        for kerbal in self.kerbals:
            if kerbal.name.find(name)>0:
                return kerbal
                break


class Kerbal:
    def __init__(self, name, trait, state, career):
        self.name = name
        self.trait = trait
        self.state = state
        self.career = career

    def __str__(self):
        return str(self.name + " (" + self.trait + ", " + self.state+")")


class Career:
    def __init__(self, flights, orbit, land):
        self.flights = flights
        self.orbit = orbit
        self.land = land

    def __str__(self):
        return str("Missions = "+str(self.flights) + "\n" + "- Landed:" + self.land + "\n- Orbit:" + self.orbit)
