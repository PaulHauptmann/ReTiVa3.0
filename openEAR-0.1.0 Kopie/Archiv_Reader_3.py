from openpyxl import load_workbook

def Read_Excel_File(Directory):
    
    wb = load_workbook(Directory)
    ws = wb.worksheets[0]



    # Create a list of list names
    list_names = [
        "Archive_Data_DateTime",
        "Archive_Data_SessionName",
        "Archive_Data_Time",
        "Archive_Data_Arousal",
        "Archive_Data_Valence",
        "Archive_Data_EmodbEmotionAnger",
        "Archive_Data_EmodbEmotionBoredom",
        "Archive_Data_EmodbEmotionDisgust",
        "Archive_Data_EmodbEmotionFear",
        "Archive_Data_EmodbEmotionHappiness",
        "Archive_Data_EmodbEmotionNeutral",
        "Archive_Data_EmodbEmotionSadness",
        "Archive_Data_AbcAffectAgressiv",
        "Archive_Data_AbcAffectCheerfull",
        "Archive_Data_AbcAffectIntoxicated",
        "Archive_Data_AbcAffectNervous",
        "Archive_Data_AbcAffectNeutral",
        "Archive_Data_AbcAffectTired",
        "Archive_Data_Loi1",
        "Archive_Data_Loi2",
        "Archive_Data_Loi3"
    ]

    # Create an empty dictionary to store the rows
    data = {}

    # Iterate over the rows and append each one to the data dictionary
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i >= 21:
            break
        data[list_names[i]] = [cell for cell in row]
    
    

    return data

def Get_Data(Directory):
    return Read_Excel_File(Directory)







#Beispiel Aufruf:

"""
data = Get_Data("/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/SmileArchiv/test23_15:23_13_01_2023.xlsx")
archive__Data_DateTime              = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_DateTime", "Key not found")
archive__Data_SessionNme            = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_SessionName", "Key not found")
archive__Data_Time                  = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Time", "Key not found")
archive__Data_Aroual                = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Arousal", "Key not found")
archive__Data_Valence               = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Valence", "Key not found")
archive__Data_EmodbEmtionAnger      = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionAnger", "Key not found")
archive__Data_EmodbEmotionBoredm    = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionBoredom", "Key not found")
archive__Data_EmodbEmotionDisgust   = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionDisgust", "Key not found")
archive__Data_EmodbEmotionFear      = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionFear", "Key not found")
archive__Data_EmodbEmotionHappness  = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionHappiness", "Key not found")
archive__Data_EmodbEmotionNeutral   = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionNeutral", "Key not found")
archive__Data_EmodbEmotionSadness   = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_EmodbEmotionSadness", "Key not found")
archive__Data_AbcAffectAgressiv     = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectAgressiv", "Key not found")
archive__Data_AbcAffectCheerful     = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectCheerfull", "Key not found")
archive__Data_AbcAffectIntoxicatd   = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectIntoxicated", "Key not found")
archive__Data_AbcAffectNervous      = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectNervous", "Key not found")
archive__Data_AbcAffectNeutral      = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectNeutral", "Key not found")
archive__Data_AbcAffectTired        = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_AbcAffectTired", "Key not found")
archive__Data_Loi1                  = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Loi1", "Key not found")
archive__Data_Loi2                  = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Loi2", "Key not found")
archive__Data_Loi3                  = (Hier Müsste importierte Instanz stehen).data.get("Archive_Data_Loi3", "Key not found")




print (archive__Data_DateTime)
print (archive__Data_SessionNme)
print (archive__Data_Time)
print (archive__Data_Aroual)
print (archive__Data_Valence)
print (archive__Data_EmodbEmtionAnger)
print (archive__Data_EmodbEmotionBoredm)
print (archive__Data_EmodbEmotionDisgust)
print (archive__Data_EmodbEmotionFear)
print (archive__Data_EmodbEmotionHappness)
print (archive__Data_EmodbEmotionNeutral)
print (archive__Data_EmodbEmotionSadness)
print (archive__Data_AbcAffectAgressiv)
print (archive__Data_AbcAffectCheerful)
print (archive__Data_AbcAffectIntoxicatd)
print (archive__Data_AbcAffectNervous)
print (archive__Data_AbcAffectNeutral)
print (archive__Data_AbcAffectTired)
print (archive__Data_Loi1)
print (archive__Data_Loi2)
print (archive__Data_Loi3)"""







    

















































