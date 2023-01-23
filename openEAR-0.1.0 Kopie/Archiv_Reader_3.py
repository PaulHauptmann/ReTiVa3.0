from openpyxl import load_workbook

def Read_Excel_File(Directory):
    
    wb = load_workbook(Directory)
    ws = wb.worksheets[0]

    # Create a list of list names
    list_names = ["Archive_Data_EmodbEmotionAnger", 
        "Archive_Data_EmodbEmotionBoredom", 
        "Archive_Data_EmodbEmotionDisgust", 
        "Archive_Data_EmodbEmotionFear", 
        "Archive_Data_EmodbEmotionHappiness", 
        "Archive_Data_EmodbEmotionNeutral", 
        "Archive_Data_EmodbEmotionSadness", 
        "Archive_Data_Wahre_Emotion"]

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





"""

Beispiel Aufruf:

data = T1.Get_Data("Weg zu File")
archive_dt_string = data.get("Archive_dt_string", "Key not found")

print (archive_dt_string)


"""




    

















































