from string import ascii_uppercase
from random import random, randint, choice as randchoice

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
 = ["normal", "rapid", "subtle"]

class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self,length,terrain,complexity):
        self.lenght = random.randint(0,10)
        self.terrain = random.randchoice(TERRAINS)
        self.complexity = random.randchoice(COMPLEXITIES)

class Track:
    """This class is creating the racetrack by adding 20 parts from TrackPart"""

    
        
