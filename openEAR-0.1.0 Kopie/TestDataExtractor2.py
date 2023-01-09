import re
from dataclasses import dataclass#
from datetime import datetime
import time
import os
import openpyxl
import wave


#path definitionen
file_path = '/Users/paul/Desktop/openEAR-0.1.0/smile.log'
directory_path = '/Users/paul/Desktop/openEAR-0.1.0/'
archive_path = '/Users/paul/Desktop/SmileArchiv/'

#listen Initialisierung
DataSpeakRatio = [0]
DataSpeakTime = [0]
DataLength = [0]
DataTime = [0]
DataArousal = [0]
DataValence = [0]
DataEmodbEmotionAnger = [0]
DataEmodbEmotionBoredom = [0]
DataEmodbEmotionDisgust = [0]
DataEmodbEmotionFear = [0]
DataEmodbEmotionHappiness = [0]
DataEmodbEmotionNeutral = [0]
DataEmodbEmotionSadness = [0]
DataAbcAffectAgressiv = [0]
DataAbcAffectCheerfull = [0]
DataAbcAffectIntoxicated = [0]
DataAbcAffectNervous = [0]
DataAbcAffectNeutral = [0]
DataAbcAffectTired = [0]
DataLoi1 = [0]
DataLoi2 = [0]
DataLoi3 = [0]












@dataclass
class EMO:
    time: float
    Arousal: float
    Valence: float
    emodbEmotionAnger: float	
    emodbEmotionBoredom: float	
    emodbEmotionDisgust: float	
    emodbEmotionFear: float	
    emodbEmotionHappiness: float	
    emodbEmotionNeutral: float	
    emodbEmotionSadness: float	
    abcAffectAgressiv: float	
    abcAffectCheerfull: float	
    abcAffectIntoxicated: float	
    abcAffectNervous: float	
    abcAffectNeutral: float	
    abcAffectTired: float	
    Loi1: float	
    Loi2: float	
    Loi3: float


def delete_old_wav_files(directory):

    files = os.listdir(directory)

    # Iterate through the list of files
    for file in files:
    
        # If the file starts with "output_segment_", delete it
        if file.startswith('output_segment_'):
            os.remove(os.path.join(directory, file))


def read_log_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        contents = str(file.readlines()[-25:])
        errorcatch= re.findall(r"\d{2}\.\d{2}\.\d{4}", contents)
        
        if len(errorcatch) != 0:
            # text_window.insert('1.0', "HAHAHAHAH")
            return

        result=re.findall(r"\d+\.\d+", contents)

        # 2 4 12 19
        result.pop(19)
        result.pop(12)
        result.pop(4)
        result.pop(2)

        emo = EMO(*result)

        
        


        
        #schreibt pro tick in die jeweilige Liste hinten dran neuesten wert, wenn der wert sich ändert
        if DataTime[-1] != emo.time:
            DataTime.append(emo.time)
            DataArousal.append(emo.Arousal)
            DataValence.append(emo.Valence)
            DataEmodbEmotionAnger.append(emo.emodbEmotionAnger)
            DataEmodbEmotionBoredom.append(emo.emodbEmotionBoredom)
            DataEmodbEmotionDisgust.append(emo.emodbEmotionDisgust)
            DataEmodbEmotionFear.append(emo.emodbEmotionFear)
            DataEmodbEmotionHappiness.append(emo.emodbEmotionHappiness)
            DataEmodbEmotionNeutral.append(emo.emodbEmotionNeutral)
            DataEmodbEmotionSadness.append(emo.emodbEmotionSadness)
            DataAbcAffectAgressiv.append(emo.abcAffectAgressiv)
            DataAbcAffectCheerfull.append(emo.abcAffectCheerfull)
            DataAbcAffectIntoxicated.append(emo.abcAffectIntoxicated)
            DataAbcAffectNervous.append(emo.abcAffectNervous)
            DataAbcAffectNeutral.append(emo.abcAffectNeutral)
            DataAbcAffectTired.append(emo.abcAffectTired)
            DataLoi1.append(emo.Loi1)
            DataLoi2.append(emo.Loi2)
            DataLoi3.append(emo.Loi3)

            #Ausgabe der Listen
            print('Time:                  ', DataTime)
            print('Arousal:               ', DataArousal)
            print('Valence:               ', DataValence)
            print('EmodbEmotionAnger:     ', DataEmodbEmotionAnger)
            print('EmodbEmotionBoredom:   ', DataEmodbEmotionBoredom)
            print('EmodbEmotionDisgust:   ', DataEmodbEmotionDisgust)
            print('EmodbEmotionFear:      ', DataEmodbEmotionFear)
            print('EmodbEmotionHappiness: ', DataEmodbEmotionHappiness)
            print('EmodbEmotionNeutral:   ', DataEmodbEmotionNeutral)
            print('EmodbEmotionSadness:   ', DataEmodbEmotionSadness)
            print('AbcAffectAgressiv:     ', DataAbcAffectAgressiv)
            print('AbcAffectCheerfull:    ', DataAbcAffectCheerfull)
            print('AbcAffectIntoxicated:  ', DataAbcAffectIntoxicated)
            print('AbcAffectNervous:      ', DataAbcAffectNervous)
            print('AbcAffectNeutral:      ', DataAbcAffectNeutral)
            print('AbcAffectTired:        ', DataAbcAffectTired)
            print('Loi1:                  ', DataLoi1)
            print('Loi2:                  ', DataLoi2)
            print('Loi3:                  ', DataLoi3)


def get_length_of_last_added_wav(directory):
    # Find the last wav file in the given directory
    wav_file = None
    last_modified_time = 0
    for file in os.listdir(directory):
        if file.startswith("output_segment_") and file.endswith(".wav"):
            modified_time = os.path.getmtime(os.path.join(directory, file))
            if modified_time > last_modified_time:
                wav_file = file
                last_modified_time = modified_time
    if wav_file is None:
        return 0

    

    # Open the wav file and get its length
    try:
        with wave.open(os.path.join(directory, wav_file), 'rb') as w:
            length = w.getnframes() / w.getframerate()
            if DataLength[-1] != length and length != 0:
                DataLength.append(length)
                print('Length:                ', DataLength)
            return w.getnframes() / w.getframerate()

    
    except (OSError, EOFError):

        return 0

            
def write_excel_file(directory, filename):
    # Create the Excel file
            #now = datetime.now()
            #file_name = now.strftime("%Y-%m-%d %H:%M:%S") + '.xlsx'
            file_name = filename + '.xlsx'
            workbook = openpyxl.Workbook()
            worksheet = workbook.active

            # Write the 19 lists to the file
            worksheet.append(DataTime)
            worksheet.append(DataArousal)
            worksheet.append(DataValence)
            worksheet.append(DataEmodbEmotionAnger)
            worksheet.append(DataEmodbEmotionBoredom)
            worksheet.append(DataEmodbEmotionDisgust)
            worksheet.append(DataEmodbEmotionFear)
            worksheet.append(DataEmodbEmotionHappiness)
            worksheet.append(DataEmodbEmotionNeutral)
            worksheet.append(DataEmodbEmotionSadness)
            worksheet.append(DataAbcAffectAgressiv)
            worksheet.append(DataAbcAffectCheerfull)
            worksheet.append(DataAbcAffectIntoxicated)
            worksheet.append(DataAbcAffectNervous)
            worksheet.append(DataAbcAffectNeutral)
            worksheet.append(DataAbcAffectTired)
            worksheet.append(DataLoi1)
            worksheet.append(DataLoi2)
            worksheet.append(DataLoi3)

            # Save the file
            workbook.save(directory+file_name)
            

def get_new_filename(directory):
    # Find all files in the specified directory that start with "Archive_File_" and end with ".xlsx"
    files = [f for f in os.listdir(directory) if f.startswith('Archive_File_') and f.endswith('.xlsx')]
    # Extract the numbers from the end of the filenames
    numbers = [int(f.split('_')[-1].split('.')[0]) for f in files]
    # If there are no files, start with number 1
    if not numbers:
        return 'Archive_File_0001.xlsx'
    # Otherwise, get the next highest number
    else:
        return 'Archive_File_{:04d}.xlsx'.format(max(numbers) + 1)
        

def get_speak_ratio():


    SpeakDuration = sum(DataLength)
    SpeakTime = float(DataTime[-1])

    if SpeakDuration != 0 and SpeakTime != DataSpeakTime[-1]:
       
        SpeakRatio = SpeakDuration/SpeakTime
        DataSpeakTime.append(SpeakTime)
        DataSpeakRatio.append(SpeakRatio)
        print('SpeakRatio:            ', SpeakRatio)
    






delete_old_wav_files(directory_path)
filename = get_new_filename(archive_path)


while True:


    
    read_log_file(file_path)    
    get_length_of_last_added_wav(directory_path)
    get_speak_ratio()
    write_excel_file(archive_path, filename)
    
       



    time.sleep(0.1)







