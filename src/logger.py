import numpy as np


class LocationsReceiver:

    def __init__(self) :

        max_x , min_x = 50 , -50
        max_y  , min_y= 50 , -50
        max_z , min_z = 50 , -50 

        self.locations = []

        x_range = [50 - (i*10) for i in range(11)]
        y_range = [50 - (i*10) for i in range(11)]
        z_range = [50 - (i*10) for i in range(11)]

        for i in range(11):
            self.locations.append(np.array([x_range[i], y_range[i] , z_range[i]]))

        # x_range = np.linspace(min_x , max_x , 10)
        # y_range = np.linspace(min_y , max_y , 10)
        # z_range = np.linspace(min_z , max_z , 10)

        # for i in x_range:
        #     for j in y_range:
        #         for k in z_range:
        #             self.locations.append(np.array([i,j,k]))