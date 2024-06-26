import numpy as np 
import pandas as pd 
from src.DirectionPredictor import Orientations 
from src.logger import LocationsReceiver
from src.customexception import TransLoc
import time 


def setup_data(tran_ori , rec_ori , pr, pt , m_vec = np.array([1, 0, 0])):
    num_points = 1000
    B_scalar = 0
    B_vectors = [] 

    roll_t = (np.pi/180)*tran_ori[0]  # Roll angle of transmitter 
    pitch_t = (np.pi/180)*tran_ori[1]  # Pitch angle of transmitter 
    yaw_t = (np.pi/180)*tran_ori[2]  # Yaw angle of transmitter 
    R_t_to_i = np.array([
        [np.cos(pitch_t)*np.cos(yaw_t), np.sin(roll_t)*np.sin(pitch_t)*np.cos(yaw_t) - np.cos(roll_t)*np.sin(yaw_t), np.cos(roll_t)*np.sin(pitch_t)*np.cos(yaw_t) + np.sin(roll_t)*np.sin(yaw_t)],
        [np.cos(pitch_t)*np.sin(yaw_t), np.sin(roll_t)*np.sin(pitch_t)*np.sin(yaw_t) + np.cos(roll_t)*np.cos(yaw_t), np.cos(roll_t)*np.sin(pitch_t)*np.sin(yaw_t) - np.sin(roll_t)*np.cos(yaw_t)],
        [-np.sin(pitch_t), np.sin(roll_t)*np.cos(pitch_t), np.cos(roll_t)*np.cos(pitch_t)]
    ])

    roll_r = (np.pi/180)*rec_ori[0]  # Roll angle of Reciever 
    pitch_r = (np.pi/180)*rec_ori[1]  # Pitch angle of Reciever
    yaw_r = (np.pi/180)*rec_ori[2]   # Yaw angle of Reciever
    R_r_to_i = np.array([
        [np.cos(pitch_r)*np.cos(yaw_r), np.sin(roll_r)*np.sin(pitch_r)*np.cos(yaw_r) - np.cos(roll_r)*np.sin(yaw_r), np.cos(roll_r)*np.sin(pitch_r)*np.cos(yaw_r) + np.sin(roll_r)*np.sin(yaw_r)],
        [np.cos(pitch_r)*np.sin(yaw_r), np.sin(roll_r)*np.sin(pitch_r)*np.sin(yaw_r) + np.cos(roll_r)*np.cos(yaw_r), np.cos(roll_r)*np.sin(pitch_r)*np.sin(yaw_r) - np.sin(roll_r)*np.cos(yaw_r)],
        [-np.sin(pitch_r), np.sin(roll_r)*np.cos(pitch_r), np.cos(roll_r)*np.cos(pitch_r)]
    ])

    B_vectors.append(get_arva_data(pr, pt, R_t_to_i, R_r_to_i, m_vec))
    B_scalar = np.linalg.norm(B_vectors[0])
    return  B_vectors, B_scalar, R_t_to_i, R_r_to_i

def get_arva_data(pr, pt, R_t_to_i, R_r_to_i, m_vec):
    R_i_to_t = np.transpose(R_t_to_i)
    r = pr - pt
    r = np.dot(R_i_to_t, r)
    A = np.array([[2*r[0]**2 - r[1]**2 - r[2]**2, 3*r[0]*r[1], 3*r[0]*r[2]],
                  [3*r[0]*r[1], 2*r[1]**2 - r[0]**2 - r[2]**2, 3*r[1]*r[2]],
                  [3*r[0]*r[2], 3*r[1]*r[2], 2*r[2]**2 - r[0]**2 - r[1]**2]])
    Am = np.dot(R_t_to_i, A)
    Am_x = A[0, 0]*m_vec[0] + A[0, 1]*m_vec[1] + A[0, 2]*m_vec[2]
    Am_y = A[1, 0]*m_vec[0] + A[1, 1]*m_vec[1] + A[1, 2]*m_vec[2]
    Am_z = A[2, 0]*m_vec[0] + A[2, 1]*m_vec[1] + A[2, 2]*m_vec[2]
    rd = np.linalg.norm(r)
    H = np.array([(1/(4*np.pi*rd**5))*Am_x, (1/(4*np.pi*rd**5))*Am_y, (1/(4*np.pi*rd**5))*Am_z])
    R_i_to_r = np.transpose(R_r_to_i)
    Hb = np.dot(R_i_to_r, H)
    return Hb 

if __name__ == '__main__':
    start = time.time()
    
    orientation = Orientations()
    rec_loct = LocationsReceiver()
    tra_loct = TransLoc() 

    rec_loc = rec_loct.locations
    tran_loc= tra_loct.trans_loc 

    reciever_orientations = orientation.reciever_orientations
    transmitter_orientations = orientation.transmitter_orientations 

    pos_t , pos_r ,  bstr_vec , bstr_sca , ori_tra , ori_rec = [] , [] , [] , [] , [] , [] 

    t_count = 1 
    for pt in tran_loc:
        count = 1
        for pr in rec_loc :
            for i in transmitter_orientations:
                for j in reciever_orientations:
                    b_vec , b_sca , _ , _= setup_data(i , j , pr , pt) 
                    pos_t.append(pt)
                    pos_r.append(pr)
                    bstr_vec.append(b_vec)
                    bstr_sca.append(b_sca)
                    ori_tra.append(i)
                    ori_rec.append(j)
            print("Transmitter Location Count = {} , Receiver Location Count  = {} ".format(t_count , count))
            count += 1
        t_count   += 1
    
    data_dict = {
        "Transmitter Location" : pos_t , 
        "Receiver Location" : pos_r , 
        "Magnetic_Vector" : bstr_vec ,
        "Magnetic_Strength" : bstr_sca,
        "Transmitter Orientation" : ori_tra , 
        "Reciever Orientation" : ori_rec
    }

    data = pd.DataFrame(data_dict)
    end = time.time()
    print("Total Time Taken : " , end-start)
    data.to_csv("artifacts/data.csv")
