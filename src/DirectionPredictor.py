import numpy as np 

class Orientations:

    def __init__(self):
        roll = [-90 , 90]
        pitch = [-30 , 30]
        yaw = [-180 , 180]

        receiver_roll = np.linspace(roll[0] , roll[1] , 5)
        receiver_yaw = np.linspace(yaw[0] , yaw[1] , 5)
        receiver_pitch = np.linspace(pitch[0] , pitch[1] , 5)

        transmitter_roll = np.linspace(roll[0] , roll[1] , 5)
        transmitter_pitch =  np.linspace(pitch[0] , pitch[1] , 5)
        transmitter_yaw = np.linspace(yaw[0] , yaw[1] , 5)


        self.reciever_orientations = []
        self.transmitter_orientations = []

        for i in range(5):
            for j in range(5):
                for k in range(5):
                    self.reciever_orientations.append([receiver_roll[i] , receiver_pitch[j] , receiver_yaw[k]])
                    self.transmitter_orientations.append([transmitter_roll[i] , transmitter_pitch[j] , transmitter_yaw[k]]) 

