import numpy as np

def calculate(list):
    #check length of list > 9
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    #create dictionary
    fetures = ['mean','variance','standard deviation','max','min','sum']
    calculations ={feture:[] for feture in fetures}

    #transfer list to Numpy array
    arr = np.array(list)
    arr = arr.reshape((3,3))

    #2D array calculation
    for axis in range(2):
        #calculate mean
        mean = np.mean(arr,axis = axis)
        calculations["mean"].append(mean.tolist())
        #calculate variance
        variamce = np.var(arr,axis = axis)
        calculations["variance"].append(variamce.tolist())
        #calculate standard deviation
        std = np.std(arr,axis = axis)
        calculations["standard deviation"].append(std.tolist())
        #calculate the max
        max_num = np.max(arr,axis = axis)
        calculations["max"].append(max_num.tolist())
        #calculate the min
        min_num = np.min(arr,axis = axis)
        calculations["min"].append(min_num.tolist())
        #calculate the sum
        sum_num = np.sum(arr,axis = axis)
        calculations["sum"].append(sum_num.tolist())

    #flattened arrary
    flattened_arr = np.ndarray.flatten(arr)
    #calculate mean
    mean = np.mean(flattened_arr)
    calculations["mean"].append(mean.tolist())
    #calculate variance
    variamce = np.var(flattened_arr)
    calculations["variance"].append(variamce.tolist())
    #calculate standard deviation
    std = np.std(flattened_arr)
    calculations["standard deviation"].append(std.tolist())
    #calculate the max
    max_num = np.max(flattened_arr)
    calculations["max"].append(max_num.tolist())
    #calculate the min
    min_num = np.min(flattened_arr)
    calculations["min"].append(min_num.tolist())
    #calculate the sum
    sum_num = np.sum(flattened_arr)
    calculations["sum"].append(sum_num.tolist())

    #return calculations(dictionary)
    return calculations