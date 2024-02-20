def get_max(data):
    max= data[0]

    for idx in range(1,len(data)):
        if data[idx] > max:
            max = data[idx]

    return max

#ipl_score_pt=[10,12,13,14,17,15]
#print("Max Is: " , get_max(ipl_score_pt))