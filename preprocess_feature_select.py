import os

import numpy as np
import pandas as pd


class dataset:
    pass


"""
import_directory = "/home/mab/dataset_cicids_2018/"
print(import_directory)
files = os.listdir(import_directory)

maxfile = 0
for file in files:
	
		

	if ( maxfile > 2 ):
		break
	if ( "~" in file ) :
		continue
	if( ".csv" in file ):	
		print(file)
		sample_data = pd.read_csv(import_directory+file)
		del sample_data['Timestamp']
		del sample_data['Dst Port']
		sample_data.to_pickle(file+".pkl")
		maxfile = maxfile + 1
		
"""

# arr = np.array([],[])
data_array = np.empty((0, 2))

pkl_directory = "/home/mab/model_cicids_2018/"
pklfiles = os.listdir(pkl_directory)
print("f")
cpt = 0
for file in pklfiles:
    print(file)
    print("fi")
    if (".pkl" in file):

        print("file to read " + file)
        if(cpt>=1):
            break
        print(pkl_directory + file)

        df = pd.read_pickle(pkl_directory + file)

        df["Flow Pkts/s"] = pd.to_numeric(df["Flow Pkts/s"], errors='coerce')
        df.info(verbose=True)


        label = df['Label']
        label_arr = label.to_numpy().T
        del df['Label']
        print("yo")
        #np_arr = df.to_numpy()
        counter = 0
        np_arr = np.array(df, dtype=np.float)
        arr1 = [np_arr, label_arr]
        #data_array = np.vstack((data_array, arr1))

        for index, row in df.iterrows():
            #print(counter)
            label = row['Label']
            np_arr = np.array(row[:-1].tolist(), dtype=np.float)
            if (label == 'Benign'):
                # arr = np.array([row.tolist(),0])
                arr1 = [np_arr, 0]
            # data_array = np.vstack([np.array(np_arr),0])
            # data_array[1] = 0
            else:
                # data_array = np.vstack((data_array,[1] ))
                arr1 = [np_arr, 1]
            # print(np_arr.dtype)
            # print(arr1)
            data_array = np.vstack((data_array, arr1))
            counter = counter + 1
            if ( counter%1000 == 1):
                print (counter)
                print(data_array)
            cpt = cpt + 1

        # print(df.Label.unique())
        print(data_array.shape)
print("sest fini")
