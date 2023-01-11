import re
from dataclasses import dataclass#
from datetime import datetime
import time
import os
import openpyxl
import wave





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


class Main:

    #path definitionen
    file_path = '/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/smile.log'
    directory_path = '/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie'
    archive_path = '/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/SmileArchiv'

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
            if Main.DataTime[-1] != emo.time:
                Main.DataTime.append(emo.time)
                Main.DataArousal.append(emo.Arousal)
                Main.DataValence.append(emo.Valence)
                Main.DataEmodbEmotionAnger.append(emo.emodbEmotionAnger)
                Main.DataEmodbEmotionBoredom.append(emo.emodbEmotionBoredom)
                Main.DataEmodbEmotionDisgust.append(emo.emodbEmotionDisgust)
                Main.DataEmodbEmotionFear.append(emo.emodbEmotionFear)
                Main.DataEmodbEmotionHappiness.append(emo.emodbEmotionHappiness)
                Main.DataEmodbEmotionNeutral.append(emo.emodbEmotionNeutral)
                Main.DataEmodbEmotionSadness.append(emo.emodbEmotionSadness)
                Main.DataAbcAffectAgressiv.append(emo.abcAffectAgressiv)
                Main.DataAbcAffectCheerfull.append(emo.abcAffectCheerfull)
                Main.DataAbcAffectIntoxicated.append(emo.abcAffectIntoxicated)
                Main.DataAbcAffectNervous.append(emo.abcAffectNervous)
                Main.DataAbcAffectNeutral.append(emo.abcAffectNeutral)
                Main.DataAbcAffectTired.append(emo.abcAffectTired)
                Main.DataLoi1.append(emo.Loi1)
                Main.DataLoi2.append(emo.Loi2)
                Main.DataLoi3.append(emo.Loi3)

                #Ausgabe der Listen
                print('Time:                  ', Main.DataTime)
                print('Arousal:               ', Main.DataArousal)
                print('Valence:               ', Main.DataValence)
                print('EmodbEmotionAnger:     ', Main.DataEmodbEmotionAnger)
                print('EmodbEmotionBoredom:   ', Main.DataEmodbEmotionBoredom)
                print('EmodbEmotionDisgust:   ', Main.DataEmodbEmotionDisgust)
                print('EmodbEmotionFear:      ', Main.DataEmodbEmotionFear)
                print('EmodbEmotionHappiness: ', Main.DataEmodbEmotionHappiness)
                print('EmodbEmotionNeutral:   ', Main.DataEmodbEmotionNeutral)
                print('EmodbEmotionSadness:   ', Main.DataEmodbEmotionSadness)
                print('AbcAffectAgressiv:     ', Main.DataAbcAffectAgressiv)
                print('AbcAffectCheerfull:    ', Main.DataAbcAffectCheerfull)
                print('AbcAffectIntoxicated:  ', Main.DataAbcAffectIntoxicated)
                print('AbcAffectNervous:      ', Main.DataAbcAffectNervous)
                print('AbcAffectNeutral:      ', Main.DataAbcAffectNeutral)
                print('AbcAffectTired:        ', Main.DataAbcAffectTired)
                print('Loi1:                  ', Main.DataLoi1)
                print('Loi2:                  ', Main.DataLoi2)
                print('Loi3:                  ', Main.DataLoi3)


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
                if Main.DataLength[-1] != length and length != 0:
                    Main.DataLength.append(length)
                    print('Length:                ', Main.DataLength)
                return w.getnframes() / w.getframerate()

        
        except (OSError, EOFError):

            return 0


    def write_excel_file(directory, filename):
        # Create the Excel file
                #now = datetime.now()
                #file_name = now.strftime("%Y-%m-%d %H:%M:%S")
                file_name = filename
                workbook = openpyxl.Workbook()
                worksheet = workbook.active

                # Write the 19 lists to the file
                worksheet.append(Main.DataTime)
                worksheet.append(Main.DataArousal)
                worksheet.append(Main.DataValence)
                worksheet.append(Main.DataEmodbEmotionAnger)
                worksheet.append(Main.DataEmodbEmotionBoredom)
                worksheet.append(Main.DataEmodbEmotionDisgust)
                worksheet.append(Main.DataEmodbEmotionFear)
                worksheet.append(Main.DataEmodbEmotionHappiness)
                worksheet.append(Main.DataEmodbEmotionNeutral)
                worksheet.append(Main.DataEmodbEmotionSadness)
                worksheet.append(Main.DataAbcAffectAgressiv)
                worksheet.append(Main.DataAbcAffectCheerfull)
                worksheet.append(Main.DataAbcAffectIntoxicated)
                worksheet.append(Main.DataAbcAffectNervous)
                worksheet.append(Main.DataAbcAffectNeutral)
                worksheet.append(Main.DataAbcAffectTired)
                worksheet.append(Main.DataLoi1)
                worksheet.append(Main.DataLoi2)
                worksheet.append(Main.DataLoi3)

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

        SpeakDuration = sum(Main.DataLength)
        SpeakTime = float(Main.DataTime[-1])

        if SpeakDuration != 0 and SpeakTime != Main.DataSpeakTime[-1]:
        
            SpeakRatio = SpeakDuration/SpeakTime
            Main.DataSpeakTime.append(SpeakTime)
            Main.DataSpeakRatio.append(SpeakRatio)
            print('SpeakRatio:            ', SpeakRatio)





    delete_old_wav_files(directory_path)
    filename = get_new_filename(archive_path)


    def live_schleif():

        while True:

            Main.read_log_file(Main.file_path)    
            Main.get_length_of_last_added_wav(Main.directory_path)
            time.sleep(0.5)
            Main.get_speak_ratio()
            Main.write_excel_file(Main.archive_path, Main.filename)

            time.sleep(0.2)
        #return Main.DataTime


Main.live_schleif()




