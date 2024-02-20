        # Multi value Container
            # SETS

jashan_followers = {"SIMMU","VANSH","NAMAN","BAABBU"}
print(jashan_followers,type(jashan_followers) )

simmu_followers = {"ROSHIL","VANSH","NAMAN","DIVIT" }
print(simmu_followers , type(simmu_followers))

mutual_followers = jashan_followers.intersection(simmu_followers)
print(mutual_followers , type(mutual_followers))

            # TO CONVERT SET INTO LIST

mutual_list = list(mutual_followers)
print(mutual_list , type(mutual_list))
