import numpy as np

class TransLoc:

    def __init__(self):
        self.trans_loc = []

        x = [10 , 15 ]
        y = [0 , 10]
        z = [18]


        for i in x:
            for j in y:
                for k in z:
                    self.trans_loc.append([i,j,k])