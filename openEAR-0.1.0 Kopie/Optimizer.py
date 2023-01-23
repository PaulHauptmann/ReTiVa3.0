import Archiv_Reader_3 as AR


data = AR.Get_Data("/Users/paul/Desktop/Mappe1.xlsx")
V1 = data.get("Archive_Data_EmodbEmotionAnger", "Key not found")
V2 = data.get("Archive_Data_EmodbEmotionBoredom", "Key not found")
V3 = data.get("Archive_Data_EmodbEmotionDisgust", "Key not found")
V4 = data.get("Archive_Data_EmodbEmotionFear", "Key not found")
V5 = data.get("Archive_Data_EmodbEmotionHappiness", "Key not found")
V6 = data.get("Archive_Data_EmodbEmotionNeutral", "Key not found")
V7 = data.get("Archive_Data_EmodbEmotionSadness", "Key not found")
WE = data.get("Archive_Data_Wahre_Emotion", "Key not found")












# Initialize the variables F1 to F7 as integers
F1, F2, F3, F4, F5, F6, F7 = (0, 0, 0, 0, 0, 0, 1)
Score = int(0)

# Use nested for loops to iterate through each variable from 0 to 100
for i in range(11):
    F1 = i
    
    for j in range(11):
        F2 = j
        print(i,j)
        for k in range(11):
            F3 = k
            for l in range(11):
                F4 = l
                for m in range(11):
                    F5 = m
                    for n in range(11):
                        F6 = n
                        for o in range(11):
                            F7 = o
                            if F1+F2+F3+F4+F5+F6+F7 != 0:
                                FG = F1+F2+F3+F4+F5+F6+F7
                            else:
                                FG = 1
                                
                            AV1 = list(map(lambda x: x*(F1/FG), V1))
                            AV2 = list(map(lambda x: x*(F2/FG), V2))
                            AV3 = list(map(lambda x: x*(F3/FG), V3))
                            AV4 = list(map(lambda x: x*(F4/FG), V4))
                            AV5 = list(map(lambda x: x*(F5/FG), V5))
                            AV6 = list(map(lambda x: x*(F6/FG), V6))
                            AV7 = list(map(lambda x: x*(F7/FG), V7))
                            
                            
                            
                            
                            
                            
                            
                            
                            for x in range(15):
                                counter =int(x)
                                E1 = AV1[counter]
                                E2 = AV2[counter]
                                E3 = AV3[counter]
                                E4 = AV4[counter]
                                E5 = AV5[counter]
                                E6 = AV6[counter]
                                E7 = AV7[counter]
                                Max = max(E1,E2,E3,E4,E5,E6,E7)
                                if Max == E1:
                                    if WE[counter]==1:
                                        Score = Score+1
                                if Max == E2:
                                    if WE[counter]==2:
                                        Score = Score+1
                                if Max == E3:
                                    if WE[counter]==3:
                                        Score = Score+1
                                if Max == E4:
                                    if WE[counter]==4:
                                        Score = Score+1
                                if Max == E5:
                                    if WE[counter]==5:
                                        Score = Score+1
                                if Max == E6:
                                    if WE[counter]==6:
                                        Score = Score+1
                                if Max == E7:
                                    if WE[counter]==7:
                                        Score = Score+1
                                        
                            
                                
                                    
                        
                            
                            # Print the current combination of values for the variables
                            
                            if Score >=5:
                                print("Score:   ", Score, "   ",F1/FG, F2/FG, F3/FG, F4/FG, F5/FG, F6/FG, F7/FG)
                            Score = 0
