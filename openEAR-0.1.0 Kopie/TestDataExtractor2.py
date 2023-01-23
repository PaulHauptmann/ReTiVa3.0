import re
from dataclasses import dataclass#
from datetime import datetime
import time
import os
import openpyxl
import wave
import subprocess




@dataclass
class MWEmo:
    MWDataSpeakRatio: float
    MWDataSpeakTime: float
    MWDataLength: float
    MWDataTime: float
    MWDataArousal: float
    MWDataValence: float
    MWDataEmodbEmotionAnger: float
    MWDataEmodbEmotionBoredom: float
    MWDataEmodbEmotionDisgust: float
    MWDataEmodbEmotionFear: float
    MWDataEmodbEmotionHappiness: float
    MWDataEmodbEmotionNeutral: float
    MWDataEmodbEmotionSadness: float
    MWDataAbcAffectAgressiv: float
    MWDataAbcAffectCheerfull: float
    MWDataAbcAffectIntoxicated: float
    MWDataAbcAffectNervous: float
    MWDataAbcAffectNeutral: float
    MWDataAbcAffectTired: float
    MWDataLoi1: float
    MWDataLoi2: float
    MWDataLoi3: float

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

    file_path = 'openEAR-0.1.0 Kopie/smile.log'
    #file_path = 'openEAR-0.1.0 Kopie/test_log_files/Smile1.log'
    directory_path = 'openEAR-0.1.0 Kopie/'
    archive_path = 'openEAR-0.1.0 Kopie/SmileArchiv/'



    timestemp1 = 1
    timestemp2 = 1
    timestemp3 = 1
    Session_Name = None
    now = datetime.now()
    dt_string = now.strftime("_%H:%M_%d_%m_%Y")
    Excel_Filename = None

    #listen Initialisierung
    DataDateTime = []
    DataSessionName = []
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
    
    
    #Nach Zeit genormte Liste
    Data_Difference_Score_EmodbEmotion = []
    Data_Difference_Score_AbcAffect = []
    Data_Difference_Score_Loi = []
    Data_Difference_Length = []
    Data_Difference_Time = []
    Data_Difference_Arousal = []
    Data_Difference_Valence = []
    Data_Difference_EmodbEmotionAnger = []
    Data_Difference_EmodbEmotionBoredom = []
    Data_Difference_EmodbEmotionDisgust = []
    Data_Difference_EmodbEmotionFear = []
    Data_Difference_EmodbEmotionHappiness = []
    Data_Difference_EmodbEmotionNeutral = []
    Data_Difference_EmodbEmotionSadness = []
    Data_Difference_AbcAffectAgressiv = []
    Data_Difference_AbcAffectCheerfull = []
    Data_Difference_AbcAffectIntoxicated = []
    Data_Difference_AbcAffectNervous = []
    Data_Difference_AbcAffectNeutral = []
    Data_Difference_AbcAffectTired = []
    Data_Difference_Loi1 = []
    Data_Difference_Loi2 = []
    Data_Difference_Loi3 = []
    
    
    
    #Mittelwerte Initialisierung
    MWDataSpeakRatio: float
    MWDataSpeakTime: float
    MWDataLength: float
    MWDataTime: float
    MWDataArousal: float
    MWDataValence: float
    MWDataEmodbEmotionAnger: float
    MWDataEmodbEmotionBoredom: float
    MWDataEmodbEmotionDisgust: float
    MWDataEmodbEmotionFear: float
    MWDataEmodbEmotionHappiness: float
    MWDataEmodbEmotionNeutral: float
    MWDataEmodbEmotionSadness: float
    MWDataAbcAffectAgressiv: float
    MWDataAbcAffectCheerfull: float
    MWDataAbcAffectIntoxicated: float
    MWDataAbcAffectNervous: float
    MWDataAbcAffectNeutral: float
    MWDataAbcAffectTired: float
    MWDataLoi1: float
    MWDataLoi2: float
    MWDataLoi3: float
    
    
    Soll_DataArousal: float
    Soll_DataValence: float
    Soll_DataEmodbEmotionAnger: float
    Soll_DataEmodbEmotionBoredom: float
    Soll_DataEmodbEmotionDisgust: float
    Soll_DataEmodbEmotionFear: float
    Soll_DataEmodbEmotionHappiness: float
    Soll_DataEmodbEmotionNeutral: float
    Soll_DataEmodbEmotionSadness: float
    Soll_DataAbcAffectAgressiv: float
    Soll_DataAbcAffectCheerfull: float
    Soll_DataAbcAffectIntoxicated: float
    Soll_DataAbcAffectNervous: float
    Soll_DataAbcAffectNeutral: float
    Soll_DataAbcAffectTired: float
    Soll_DataLoi1: float
    Soll_DataLoi2: float
    Soll_DataLoi3: float
    
    Loi_Score: float
    MWLoi_Score: float
    
   


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

            Main.timestemp1 = emo.time
            
            


    
            #schreibt pro tick in die jeweilige Liste hinten dran neuesten wert, wenn der wert sich ändert
            if float(Main.DataTime[-1]) != float(emo.time):
                Main.DataTime.append(float(emo.time))
                Main.DataArousal.append(float(emo.Arousal))
                Main.DataValence.append(float(emo.Valence))
                Main.DataEmodbEmotionAnger.append(float(emo.emodbEmotionAnger))
                Main.DataEmodbEmotionBoredom.append(float(emo.emodbEmotionBoredom))
                Main.DataEmodbEmotionDisgust.append(float(emo.emodbEmotionDisgust))
                Main.DataEmodbEmotionFear.append(float(emo.emodbEmotionFear))
                Main.DataEmodbEmotionHappiness.append(float(emo.emodbEmotionHappiness))
                Main.DataEmodbEmotionNeutral.append(float(emo.emodbEmotionNeutral))
                Main.DataEmodbEmotionSadness.append(float(emo.emodbEmotionSadness))
                Main.DataAbcAffectAgressiv.append(float(emo.abcAffectAgressiv))
                Main.DataAbcAffectCheerfull.append(float(emo.abcAffectCheerfull))
                Main.DataAbcAffectIntoxicated.append(float(emo.abcAffectIntoxicated))
                Main.DataAbcAffectNervous.append(float(emo.abcAffectNervous))
                Main.DataAbcAffectNeutral.append(float(emo.abcAffectNeutral))
                Main.DataAbcAffectTired.append(float(emo.abcAffectTired))
                Main.DataLoi1.append(float(emo.Loi1))
                Main.DataLoi2.append(float(emo.Loi2))
                Main.DataLoi3.append(float(emo.Loi3))

                #Ausgabe der Listen
                """print('Time:                  ', Main.DataTime)
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
                print('Loi3:                  ', Main.DataLoi3)"""


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


    def write_excel_file(directoryExcel, filename):
        # Create the Excel file
                #now = datetime.now()
                #file_name = now.strftime("%Y-%m-%d %H:%M:%S")
                file_name = str(directoryExcel)+str(filename)+".xlsx"
                
                workbook = openpyxl.Workbook()
                worksheet = workbook.active

                # Write the 19 lists to the file
                worksheet.append(Main.DataDateTime)
                worksheet.append(Main.DataSessionName)
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
                workbook.save(file_name)
    

    def get_new_filename(directory, Session_Name):
        
        if Session_Name != None:
            return Session_Name+Main.dt_string

        else:
            return "Neue_Session"+Main.dt_string

        
    def get_speak_ratio():

        SpeakDuration = sum(Main.DataLength)
        SpeakTime = float(Main.DataTime[-1])

        if SpeakDuration != 0 and SpeakTime != Main.DataSpeakTime[-1]:
        
            SpeakRatio = SpeakDuration/SpeakTime
            Main.DataSpeakTime.append(SpeakTime)
            Main.DataSpeakRatio.append(SpeakRatio)
            print('SpeakRatio:            ', SpeakRatio)


    def Anzahl_Files_Gleitender_Mittelwert():
        # Hier kann man einstellen über wieviel sekunden der Mittelwert gehen soll
        if sum(Main.DataLength) >= 20:
            K=1
            while sum(Main.DataLength[-K:]) <= 20:
                K = K+1
            #print (K)
            return K

        else:
            #print(len(Main.DataLength))
            return len(Main.DataLength)


    def Gleitender_Mittelwert():
        K = int(Main.Anzahl_Files_Gleitender_Mittelwert())

        if float(Main.DataTime[-1]) != float(Main.timestemp2):

        
            Main.MWDataSpeakRatio =                    ((sum(Main.DataSpeakRatio[-K:]))                  /      (K))
            Main.MWDataSpeakTime =                     ((sum(Main.DataSpeakTime[-K:]))                   /      (K))
            Main.MWDataLength =                        ((sum(Main.DataLength[-K:]))                      /      (K))
            Main.MWDataTime =                          ((sum(Main.DataTime[-K:]))                        /      (K))
            Main.MWDataArousal =                       ((sum(Main.DataArousal[-K:]))                     /      (K))
            Main.MWDataValence =                       ((sum(Main.DataValence[-K:]))                     /      (K))
            Main.MWDataEmodbEmotionAnger =             ((sum(Main.DataEmodbEmotionAnger[-K:]))           /      (K))
            Main.MWDataEmodbEmotionBoredom =           ((sum(Main.DataEmodbEmotionBoredom[-K:]))         /      (K))
            Main.MWDataEmodbEmotionDisgust =           ((sum(Main.DataEmodbEmotionDisgust[-K:]))         /      (K))
            Main.MWDataEmodbEmotionFear =              ((sum(Main.DataEmodbEmotionFear[-K:]))            /      (K))
            Main.MWDataEmodbEmotionHappiness =         ((sum(Main.DataEmodbEmotionHappiness[-K:]))       /      (K))
            Main.MWDataEmodbEmotionNeutral =           ((sum(Main.DataEmodbEmotionNeutral[-K:]))         /      (K))
            Main.MWDataEmodbEmotionSadness =           ((sum(Main.DataEmodbEmotionSadness[-K:]))         /      (K))
            Main.MWDataAbcAffectAgressiv =             ((sum(Main.DataAbcAffectAgressiv[-K:]))           /      (K))
            Main.MWDataAbcAffectCheerfull =            ((sum(Main.DataAbcAffectCheerfull[-K:]))          /      (K))
            Main.MWDataAbcAffectIntoxicated =          ((sum(Main.DataAbcAffectIntoxicated[-K:]))        /      (K))
            Main.MWDataAbcAffectNervous =              ((sum(Main.DataAbcAffectNervous[-K:]))            /      (K))
            Main.MWDataAbcAffectNeutral =              ((sum(Main.DataAbcAffectNeutral[-K:]))            /      (K))
            Main.MWDataAbcAffectTired =                ((sum(Main.DataAbcAffectTired[-K:]))              /      (K))
            Main.MWDataLoi1 =                          ((sum(Main.DataLoi1[-K:]))                        /      (K))
            Main.MWDataLoi2 =                          ((sum(Main.DataLoi2[-K:]))                        /      (K))
            Main.MWDataLoi3 =                          ((sum(Main.DataLoi3[-K:]))                        /      (K))

        
            Main.timestemp2 = Main.timestemp1

    
    def Set_Session_Name (Sessionname):

        Main.Session_Name = Sessionname
        Main.Excel_Filename = Main.get_new_filename(Main.archive_path, Main.Session_Name)
        

    def Printer():
        
        if float(Main.DataTime[-1]) != float(Main.timestemp3):
        
            print("DataSpeakRatio:                ",         Main.DataSpeakRatio)
            print("DataSpeakTime:                 ",         Main.DataSpeakTime)
            print("DataLength:                    ",         Main.DataLength)
            print("DataTime:                      ",         Main.DataTime)
            print("DataArousal:                   ",         Main.DataArousal)
            print("DataValence:                   ",         Main.DataValence)
            print("DataEmodbEmotionAnger:         ",         Main.DataEmodbEmotionAnger)
            print("DataEmodbEmotionBoredom:       ",         Main.DataEmodbEmotionBoredom)
            print("DataEmodbEmotionDisgust:       ",         Main.DataEmodbEmotionDisgust)
            print("DataEmodbEmotionFear:          ",         Main.DataEmodbEmotionFear)
            print("DataEmodbEmotionHappiness:     ",         Main.DataEmodbEmotionHappiness)
            print("DataEmodbEmotionNeutral:       ",         Main.DataEmodbEmotionNeutral)
            print("DataEmodbEmotionSadness:       ",         Main.DataEmodbEmotionSadness)
            print("DataAbcAffectAgressiv:         ",         Main.DataAbcAffectAgressiv)
            print("DataAbcAffectCheerfull:        ",         Main.DataAbcAffectCheerfull)
            print("DataAbcAffectIntoxicated:      ",         Main.DataAbcAffectIntoxicated)
            print("DataAbcAffectNervous:          ",         Main.DataAbcAffectNervous)
            print("DataAbcAffectNeutral:          ",         Main.DataAbcAffectNeutral)
            print("DataAbcAffectTired:            ",         Main.DataAbcAffectTired)
            print("DataLoi1:                      ",         Main.DataLoi1)
            print("DataLoi2:                      ",         Main.DataLoi2)
            print("DataLoi3:                      ",         Main.DataLoi3)

            Main.timestemp3 = Main.timestemp1


    def Updater():

        Main.read_log_file(Main.file_path) 
        Main.get_length_of_last_added_wav(Main.directory_path)
        time.sleep(0.5)
        Main.get_speak_ratio()
        Main.Gleitender_Mittelwert()
        Main.write_excel_file(Main.archive_path, Main.Excel_Filename)
        Main.Printer()
        Main.Get_Score()
        Main.Get_Loi_Score
        Main.Get_MWLoi_Score()
        

    def Set_Absolut_Difference():
        
        
        
        Main.Data_Difference_Score_EmodbEmotion.clear()
        Main.Data_Difference_Score_AbcAffect.clear()
        Main.Data_Difference_Score_Loi.clear()
        Main.Data_Difference_Length.clear()
        Main.Data_Difference_Time.clear()
        Main.Data_Difference_Arousal.clear()
        Main.Data_Difference_Valence.clear()
        Main.Data_Difference_EmodbEmotionAnger.clear()
        Main.Data_Difference_EmodbEmotionBoredom.clear()
        Main.Data_Difference_EmodbEmotionDisgust.clear()
        Main.Data_Difference_EmodbEmotionFear.clear()
        Main.Data_Difference_EmodbEmotionHappiness.clear()
        Main.Data_Difference_EmodbEmotionNeutral.clear()
        Main.Data_Difference_EmodbEmotionSadness.clear()
        Main.Data_Difference_AbcAffectAgressiv.clear()
        Main.Data_Difference_AbcAffectCheerfull.clear()
        Main.Data_Difference_AbcAffectIntoxicated.clear()
        Main.Data_Difference_AbcAffectNervous.clear()
        Main.Data_Difference_AbcAffectNeutral.clear()
        Main.Data_Difference_AbcAffectTired.clear()
        Main.Data_Difference_Loi1.clear()
        Main.Data_Difference_Loi2.clear()
        Main.Data_Difference_Loi3.clear()
        
        
        
        for i in range(len(Main.DataArousal)):
            
        
        
            
           
            Main.Data_Difference_Arousal.append(                      (abs(        Main.DataArousal[i]                  -         Main.Soll_DataArousal))/2)
            Main.Data_Difference_Valence.append(                      (abs(        Main.DataValence[i]                  -         Main.Soll_DataValence))/2)
            Main.Data_Difference_EmodbEmotionAnger.append(            (abs(        Main.DataEmodbEmotionAnger[i]        -         Main.Soll_DataEmodbEmotionAnger))/2)
            Main.Data_Difference_EmodbEmotionBoredom.append(          (abs(        Main.DataEmodbEmotionBoredom[i]      -         Main.Soll_DataEmodbEmotionBoredom))/2)
            Main.Data_Difference_EmodbEmotionDisgust.append(          (abs(        Main.DataEmodbEmotionDisgust[i]      -         Main.Soll_DataEmodbEmotionDisgust))/2)
            Main.Data_Difference_EmodbEmotionFear.append(             (abs(        Main.DataEmodbEmotionFear[i]         -         Main.Soll_DataEmodbEmotionFear))/2)
            Main.Data_Difference_EmodbEmotionHappiness.append(        (abs(        Main.DataEmodbEmotionHappiness[i]    -         Main.Soll_DataEmodbEmotionHappiness))/2)
            Main.Data_Difference_EmodbEmotionNeutral.append(          (abs(        Main.DataEmodbEmotionNeutral[i]      -         Main.Soll_DataEmodbEmotionNeutral))/2)
            Main.Data_Difference_EmodbEmotionSadness.append(          (abs(        Main.DataEmodbEmotionSadness[i]      -         Main.Soll_DataEmodbEmotionSadness))/2)
            Main.Data_Difference_AbcAffectAgressiv.append(            (abs(        Main.DataAbcAffectAgressiv[i]        -         Main.Soll_DataAbcAffectAgressiv))/2)
            Main.Data_Difference_AbcAffectCheerfull.append(           (abs(        Main.DataAbcAffectCheerfull[i]       -         Main.Soll_DataAbcAffectCheerfull))/2)
            Main.Data_Difference_AbcAffectIntoxicated.append(         (abs(        Main.DataAbcAffectIntoxicated[i]     -         Main.Soll_DataAbcAffectIntoxicated))/2)
            Main.Data_Difference_AbcAffectNervous.append(             (abs(        Main.DataAbcAffectNervous[i]         -         Main.Soll_DataAbcAffectNervous))/2)
            Main.Data_Difference_AbcAffectNeutral.append(             (abs(        Main.DataAbcAffectNeutral[i]         -         Main.Soll_DataAbcAffectNeutral))/2)
            Main.Data_Difference_AbcAffectTired.append(               (abs(        Main.DataAbcAffectTired[i]           -         Main.Soll_DataAbcAffectTired))/2)
            Main.Data_Difference_Loi1.append(                         (abs(        Main.DataLoi1[i]                     -         Main.Soll_DataLoi1))/2)
            Main.Data_Difference_Loi2.append(                         (abs(        Main.DataLoi2[i]                     -         Main.Soll_DataLoi2))/2)
            Main.Data_Difference_Loi3.append(                         (abs(        Main.DataLoi3[i]                     -         Main.Soll_DataLoi3))/2)
            
            
            Main.Data_Difference_Score_EmodbEmotion.append(
                
                (1-
                (Main.Data_Difference_EmodbEmotionAnger[i]+
                Main.Data_Difference_EmodbEmotionBoredom[i]+
                Main.Data_Difference_EmodbEmotionDisgust[i]+
                Main.Data_Difference_EmodbEmotionFear[i]+
                Main.Data_Difference_EmodbEmotionHappiness[i]+
                Main.Data_Difference_EmodbEmotionNeutral[i]+
                Main.Data_Difference_EmodbEmotionSadness[i])
                ) * Main.DataLength[i]
            )
            
            Main.Data_Difference_Score_AbcAffect.append(
                
                (1-
                ((Main.Data_Difference_AbcAffectAgressiv[i]+
                Main.Data_Difference_AbcAffectCheerfull[i]+
                Main.Data_Difference_AbcAffectIntoxicated[i]+
                Main.Data_Difference_AbcAffectNervous[i]+
                Main.Data_Difference_AbcAffectNeutral[i]+
                Main.Data_Difference_AbcAffectTired[i])
                /2)) * Main.DataLength[i]
            )
            
            
            Main.Data_Difference_Score_Loi.append(
                
                (1-
                ((Main.Data_Difference_Loi1[i]+
                Main.Data_Difference_Loi2[i]+
                Main.Data_Difference_Loi3[i]) 
                /2)) * Main.DataLength[i]
            
            )
            

    def Set_Soll_Werte(
        Soll_DataEmodbEmotionAnger,
        Soll_DataEmodbEmotionBoredom,
        Soll_DataEmodbEmotionDisgust,
        Soll_DataEmodbEmotionFear,
        Soll_DataEmodbEmotionHappiness,
        Soll_DataEmodbEmotionNeutral,
        Soll_DataEmodbEmotionSadness,
        Soll_DataAbcAffectAgressiv,
        Soll_DataAbcAffectCheerfull,
        Soll_DataAbcAffectIntoxicated,
        Soll_DataAbcAffectNervous,
        Soll_DataAbcAffectNeutral,
        Soll_DataAbcAffectTired,
        
    ):
        
        Main.Soll_DataEmodbEmotionAnger =         Soll_DataEmodbEmotionAnger
        Main.Soll_DataEmodbEmotionBoredom =       Soll_DataEmodbEmotionBoredom
        Main.Soll_DataEmodbEmotionDisgust =       Soll_DataEmodbEmotionDisgust
        Main.Soll_DataEmodbEmotionFear =          Soll_DataEmodbEmotionFear
        Main.Soll_DataEmodbEmotionHappiness =     Soll_DataEmodbEmotionHappiness
        Main.Soll_DataEmodbEmotionNeutral =       Soll_DataEmodbEmotionNeutral
        Main.Soll_DataEmodbEmotionSadness =       Soll_DataEmodbEmotionSadness
        Main.Soll_DataAbcAffectAgressiv =         Soll_DataAbcAffectAgressiv
        Main.Soll_DataAbcAffectCheerfull =        Soll_DataAbcAffectCheerfull
        Main.Soll_DataAbcAffectIntoxicated =      Soll_DataAbcAffectIntoxicated
        Main.Soll_DataAbcAffectNervous =          Soll_DataAbcAffectNervous
        Main.Soll_DataAbcAffectNeutral =          Soll_DataAbcAffectNeutral
        Main.Soll_DataAbcAffectTired =            Soll_DataAbcAffectTired
        
        
    def Get_Score():
        
        Main.Set_Absolut_Difference()
        
        
        
        Score_EmodbEmotions = (sum(Main.Data_Difference_Score_EmodbEmotion)) / (sum(Main.DataLength))
        Score_AbcAffect = (sum(Main.Data_Difference_Score_AbcAffect)) / (sum(Main.DataLength))
        
        
        return (Score_EmodbEmotions, Score_AbcAffect)
    
    
    def Get_Live_Score():
        
        Main.Set_Absolut_Difference()
        
        
        
        Score_EmodbEmotions = ((Main.Data_Difference_Score_EmodbEmotion)) / ((Main.DataLength))
        Score_AbcAffect = ((Main.Data_Difference_Score_AbcAffect)) / ((Main.DataLength))
        
        
        return (Score_EmodbEmotions, Score_AbcAffect)


    def Start_Programm():
        Main.delete_old_wav_files(Main.directory_path)
        cmd = "echo 'hello world'"
        
        subprocess.run(cmd, shell=True, capture_output=True)
        
    
    def Get_Loi_Score():
        if EMO.Loi1 > EMO.Loi2 and EMO.Loi1 > EMO.Loi3:
            Main.Loi_Score = (EMO.Loi2 + (2*EMO.Loi3))/2
        elif EMO.Loi2 > EMO.Loi1 and EMO.Loi2 > EMO.Loi3:
            Main.Loi_Score = (1 + (EMO.Loi3 - EMO.Loi1))/2
        else:
            Main.Loi_Score = (2 - (EMO.Loi2 + (2*EMO.Loi1)))/2
        

    def Get_MWLoi_Score():
        if Main.MWDataLoi1 > Main.MWDataLoi2 and Main.MWDataLoi1 > Main.MWDataLoi3:
            Main.MWLoi_Score = (Main.MWDataLoi2 + (2*Main.MWDataLoi3))/2
        elif Main.MWDataLoi2 > Main.MWDataLoi1 and Main.MWDataLoi2 > Main.MWDataLoi3:
            Main.MWLoi_Score = (1 + (Main.MWDataLoi3 - Main.MWDataLoi1))/2
        else:
            Main.MWLoi_Score = (2 - (Main.MWDataLoi2 + (2*Main.MWDataLoi1)))/2



