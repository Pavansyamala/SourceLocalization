import numpy as np


class LocationsReceiver:

    def __init__(self) :

        max_x , min_x = 50 , -10
        max_y  , min_y= 50 , -10
        max_z , min_z = 50 , -10 

        self.locations = []

        x_range = np.linspace(min_x , max_x , 10)
        y_range = np.linspace(min_y , max_y , 10)
        z_range = np.linspace(min_z , max_z , 10)

        for i in x_range:
            for j in y_range:
                for k in z_range:
                    self.locations.append(np.array([i,j,k]))