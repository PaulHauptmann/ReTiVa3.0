import re
from dataclasses import dataclass
from datetime import datetime
import time
import os
import openpyxl
import wave
import subprocess
import random
#import Test1 as T




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

    #file_path = 'openEAR-0.1.0 Kopie/smile.log'
    file_path = '/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/smile.log'
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
    DataSpeakRatio = [0.0]
    DataSpeakTime = [0.0]
    DataLength = [0.0]
    DataTime = [0.0]
    DataArousal = [0.0]
    DataValence = [0.0]
    DataEmodbEmotionAnger = [0.0]
    DataEmodbEmotionBoredom = [0.0]
    DataEmodbEmotionDisgust = [0.0]
    DataEmodbEmotionFear = [0.0]
    DataEmodbEmotionHappiness = [0.0]
    DataEmodbEmotionNeutral = [0.0]
    DataEmodbEmotionSadness = [0.0]
    DataAbcAffectAgressiv = [0.0]
    DataAbcAffectCheerfull = [0.0]
    DataAbcAffectIntoxicated = [0.0]
    DataAbcAffectNervous = [0.0]
    DataAbcAffectNeutral = [0.0]
    DataAbcAffectTired = [0.0]
    DataLoi1 = [0.0]
    DataLoi2 = [0.0]
    DataLoi3 = [0.0]
    
  
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
    MWDataSpeakRatio: float = 0.0
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
    
    
    Time_Norm_Data_Arousal = []
    Time_Norm_Data_Valence = []
    Time_Norm_Data_EmodbEmotionAnger = []
    Time_Norm_Data_EmodbEmotionBoredom = []
    Time_Norm_Data_EmodbEmotionDisgust = []
    Time_Norm_Data_EmodbEmotionFear = []
    Time_Norm_Data_EmodbEmotionHappiness = []
    Time_Norm_Data_EmodbEmotionNeutral = []
    Time_Norm_Data_EmodbEmotionSadness = []
    Time_Norm_Data_AbcAffectAgressiv = []
    Time_Norm_Data_AbcAffectCheerfull = []
    Time_Norm_Data_AbcAffectIntoxicated = []
    Time_Norm_Data_AbcAffectNervous = []
    Time_Norm_Data_AbcAffectNeutral = []
    Time_Norm_Data_AbcAffectTired = []
    Time_Norm_Data_Loi1 = []
    Time_Norm_Data_Loi2 = []
    Time_Norm_Data_Loi3 = []
    
    
    Abs_MW_Data_Arousal: float = 0.0
    Abs_MW_Data_Valence: float = 0.0
    Abs_MW_Data_EmodbEmotionAnger: float = 0.0
    Abs_MW_Data_EmodbEmotionBoredom: float = 0.0
    Abs_MW_Data_EmodbEmotionDisgust: float = 0.0
    Abs_MW_Data_EmodbEmotionFear: float = 0.0
    Abs_MW_Data_EmodbEmotionHappiness: float = 0.0
    Abs_MW_Data_EmodbEmotionNeutral: float = 0.0
    Abs_MW_Data_EmodbEmotionSadness: float = 0.0
    Abs_MW_Data_AbcAffectAgressiv: float = 0.0
    Abs_MW_Data_AbcAffectCheerfull: float = 0.0
    Abs_MW_Data_AbcAffectIntoxicated: float = 0.0
    Abs_MW_Data_AbcAffectNervous: float = 0.0
    Abs_MW_Data_AbcAffectNeutral: float = 0.0
    Abs_MW_Data_AbcAffectTired: float = 0.0
    Abs_MW_Data_Loi1: float = 0.0
    Abs_MW_Data_Loi2: float = 0.0
    Abs_MW_Data_Loi3: float = 0.0
    Abs_MW_Data_EmodbEmotion_List = []
    Abs_MW_Data_AbcAffect_List = []
    
    
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
    Soll_Data_EmodbEmotion_List = []
    Soll_Data_AbcAffect_List = []
    
    
    Loi_Score: float
    MWLoi_Score: float
    Abs_MW_Loi_Score: float

    Score_EmodbEmotions: float
    Score_AbcAffect: float
    Score_Retiva: float
    
   


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
            
            


    
            #schreibt pro tick in die jeweilige Liste hinten dran neuesten wert, wenn der wert sich ??ndert
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
                #if Main.DataLength[-1] != length:
                    Main.DataLength.append(length)
                return w.getnframes() / w.getframerate()

        
        except (OSError, EOFError):

            return 0
        

    def zusammenf??hrer():
        while len(Main.DataTime) != len(Main.DataLength):
            time.sleep(0.5)
            Main.get_length_of_last_added_wav(Main.directory_path)


    def write_excel_file(directoryExcel, filename):
        
        # Create the Excel file
        #now = datetime.now()
        #file_name = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = str(directoryExcel)+str(filename)+".xlsx"
        
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
        worksheet.append([Main.Soll_DataEmodbEmotionAnger])
        worksheet.append([Main.Soll_DataEmodbEmotionBoredom])
        worksheet.append([Main.Soll_DataEmodbEmotionDisgust])
        worksheet.append([Main.Soll_DataEmodbEmotionFear])
        worksheet.append([Main.Soll_DataEmodbEmotionHappiness])
        worksheet.append([Main.Soll_DataEmodbEmotionNeutral])
        worksheet.append([Main.Soll_DataEmodbEmotionSadness])
        worksheet.append([Main.Soll_DataAbcAffectAgressiv])
        worksheet.append([Main.Soll_DataAbcAffectCheerfull])
        worksheet.append([Main.Soll_DataAbcAffectIntoxicated])
        worksheet.append([Main.Soll_DataAbcAffectNervous])
        worksheet.append([Main.Soll_DataAbcAffectNeutral])
        worksheet.append([Main.Soll_DataAbcAffectTired])
        worksheet.append([Main.Abs_MW_Data_Arousal])
        worksheet.append([Main.Abs_MW_Data_Valence])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionAnger])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionBoredom])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionDisgust])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionFear])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionHappiness])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionNeutral])
        worksheet.append([Main.Abs_MW_Data_EmodbEmotionSadness])
        worksheet.append([Main.Abs_MW_Data_AbcAffectAgressiv])
        worksheet.append([Main.Abs_MW_Data_AbcAffectCheerfull])
        worksheet.append([Main.Abs_MW_Data_AbcAffectIntoxicated])
        worksheet.append([Main.Abs_MW_Data_AbcAffectNervous])
        worksheet.append([Main.Abs_MW_Data_AbcAffectNeutral])
        worksheet.append([Main.Abs_MW_Data_AbcAffectTired])
        worksheet.append([Main.Abs_MW_Data_Loi1])
        worksheet.append([Main.Abs_MW_Data_Loi2])
        worksheet.append([Main.Abs_MW_Data_Loi3])
        worksheet.append([Main.Score_EmodbEmotions])
        worksheet.append([Main.Score_AbcAffect])
        worksheet.append([Main.Score_Retiva])
        worksheet.append([Main.Abs_MW_Loi_Score])
        worksheet.append([Main.MWDataSpeakRatio])




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
        

    def Anzahl_Files_Gleitender_Mittelwert():
        # Hier kann man einstellen ??ber wieviel sekunden der Mittelwert gehen soll
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
        last_K_DataLength = Main.DataLength[-K:]
        
        if float(Main.DataTime[-1]) != float(Main.timestemp2) and sum(last_K_DataLength)>=20:

        
            last_K_DataLength = Main.DataLength[-K:]
            Main.MWDataArousal =                       ((sum(Main.Time_Norm_Data_Arousal[-K:])                      / sum(last_K_DataLength)))
            Main.MWDataValence =                       ((sum(Main.Time_Norm_Data_Valence[-K:])                      / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionAnger =             ((sum(Main.Time_Norm_Data_EmodbEmotionAnger[-K:])            / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionBoredom =           ((sum(Main.Time_Norm_Data_EmodbEmotionBoredom[-K:])          / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionDisgust =           ((sum(Main.Time_Norm_Data_EmodbEmotionDisgust[-K:])          / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionFear =              ((sum(Main.Time_Norm_Data_EmodbEmotionFear[-K:])             / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionHappiness =         ((sum(Main.Time_Norm_Data_EmodbEmotionHappiness[-K:])        / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionNeutral =           ((sum(Main.Time_Norm_Data_EmodbEmotionNeutral[-K:])          / sum(last_K_DataLength)))
            Main.MWDataEmodbEmotionSadness =           ((sum(Main.Time_Norm_Data_EmodbEmotionSadness[-K:])          / sum(last_K_DataLength)))
            Main.MWDataAbcAffectAgressiv =             ((sum(Main.Time_Norm_Data_AbcAffectAgressiv[-K:])            / sum(last_K_DataLength)))
            Main.MWDataAbcAffectCheerfull =            ((sum(Main.Time_Norm_Data_AbcAffectCheerfull[-K:])           / sum(last_K_DataLength)))
            Main.MWDataAbcAffectIntoxicated =          ((sum(Main.Time_Norm_Data_AbcAffectIntoxicated[-K:])         / sum(last_K_DataLength)))
            Main.MWDataAbcAffectNervous =              ((sum(Main.Time_Norm_Data_AbcAffectNervous[-K:])             / sum(last_K_DataLength)))
            Main.MWDataAbcAffectNeutral =              ((sum(Main.Time_Norm_Data_AbcAffectNeutral[-K:])             / sum(last_K_DataLength)))
            Main.MWDataAbcAffectTired =                ((sum(Main.Time_Norm_Data_AbcAffectTired[-K:])               / sum(last_K_DataLength)))
            Main.MWDataLoi1 =                          ((sum(Main.Time_Norm_Data_Loi1[-K:])                         / sum(last_K_DataLength)))
            Main.MWDataLoi2 =                          ((sum(Main.Time_Norm_Data_Loi2[-K:])                         / sum(last_K_DataLength)))
            Main.MWDataLoi3 =                          ((sum(Main.Time_Norm_Data_Loi3[-K:])                         / sum(last_K_DataLength)))

        
            Main.timestemp2 = Main.timestemp1
        
        elif float(Main.DataTime[-1]) != float(Main.timestemp2):
            C = len(Main.Time_Norm_Data_Arousal)
            last_C_DataLength = Main.DataLength[-C:]
            Main.MWDataArousal =                       ((sum(Main.Time_Norm_Data_Arousal[-C:])                      / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataValence =                       ((sum(Main.Time_Norm_Data_Valence[-C:])                      / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionAnger =             ((sum(Main.Time_Norm_Data_EmodbEmotionAnger[-C:])            / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionBoredom =           ((sum(Main.Time_Norm_Data_EmodbEmotionBoredom[-C:])          / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionDisgust =           ((sum(Main.Time_Norm_Data_EmodbEmotionDisgust[-C:])          / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionFear =              ((sum(Main.Time_Norm_Data_EmodbEmotionFear[-C:])             / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionHappiness =         ((sum(Main.Time_Norm_Data_EmodbEmotionHappiness[-C:])        / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionNeutral =           ((sum(Main.Time_Norm_Data_EmodbEmotionNeutral[-C:])          / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataEmodbEmotionSadness =           ((sum(Main.Time_Norm_Data_EmodbEmotionSadness[-C:])          / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectAgressiv =             ((sum(Main.Time_Norm_Data_AbcAffectAgressiv[-C:])            / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectCheerfull =            ((sum(Main.Time_Norm_Data_AbcAffectCheerfull[-C:])           / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectIntoxicated =          ((sum(Main.Time_Norm_Data_AbcAffectIntoxicated[-C:])         / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectNervous =              ((sum(Main.Time_Norm_Data_AbcAffectNervous[-C:])             / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectNeutral =              ((sum(Main.Time_Norm_Data_AbcAffectNeutral[-C:])             / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataAbcAffectTired =                ((sum(Main.Time_Norm_Data_AbcAffectTired[-C:])               / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataLoi1 =                          ((sum(Main.Time_Norm_Data_Loi1[-C:])                         / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataLoi2 =                          ((sum(Main.Time_Norm_Data_Loi2[-C:])                         / (sum(last_C_DataLength)+0.0000000001)))
            Main.MWDataLoi3 =                          ((sum(Main.Time_Norm_Data_Loi3[-C:])                         / (sum(last_C_DataLength)+0.0000000001)))
            
            Main.timestemp2 = Main.timestemp1
    
    
    def Set_Session_Name (V1):

        Main.Session_Name = V1
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
            print()
            print("MWDataArousal:                 ",         Main.MWDataArousal)
            print("MWDataValence:                 ",         Main.MWDataValence)
            print("MWDataEmodbEmotionAnger:       ",         Main.MWDataEmodbEmotionAnger)
            print("MWDataEmodbEmotionBoredom:     ",         Main.MWDataEmodbEmotionBoredom)
            print("MWDataEmodbEmotionDisgust:     ",         Main.MWDataEmodbEmotionDisgust)
            print("MWDataEmodbEmotionFear:        ",         Main.MWDataEmodbEmotionFear)
            print("MWDataEmodbEmotionHappiness:   ",         Main.MWDataEmodbEmotionHappiness)
            print("MWDataEmodbEmotionNeutral:     ",         Main.MWDataEmodbEmotionNeutral)
            print("MWDataEmodbEmotionSadness:     ",         Main.MWDataEmodbEmotionSadness)
            print("MWDataAbcAffectAgressiv:       ",         Main.MWDataAbcAffectAgressiv)
            print("MWDataAbcAffectCheerfull:      ",         Main.MWDataAbcAffectCheerfull)
            print("MWDataAbcAffectIntoxicated:    ",         Main.MWDataAbcAffectIntoxicated)
            print("MWDataAbcAffectNervous:        ",         Main.MWDataAbcAffectNervous)
            print("MWDataAbcAffectNeutral:        ",         Main.MWDataAbcAffectNeutral)
            print("MWDataAbcAffectTired:          ",         Main.MWDataAbcAffectTired)
            print("MWDataLoi1:                    ",         Main.MWDataLoi1)
            print("MWDataLoi2:                    ",         Main.MWDataLoi2)
            print("MWDataLoi3:                    ",         Main.MWDataLoi3)
            print()
            print("MWLoi_Score                    ",         Main.MWLoi_Score)
            print("Loi_Score                      ",         Main.Loi_Score)
            print("Score_EmodbEmotions            ",         Main.Score_EmodbEmotions)
            print("Score_AbcAffect                ",         Main.Score_AbcAffect)
            print()
            print()
            print()
            print()
            

        Main.timestemp3 = Main.timestemp1
        

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
        
            try: 
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
            except IndexError:
                time.sleep(0.5)
                
        
    """def Set_Soll_Werte(
        ??bergabe_Soll_DataEmodbEmotionAnger,
        ??bergabe_Soll_DataEmodbEmotionBoredom,
        ??bergabe_Soll_DataEmodbEmotionDisgust,
        ??bergabe_Soll_DataEmodbEmotionFear,
        ??bergabe_Soll_DataEmodbEmotionHappiness,
        ??bergabe_Soll_DataEmodbEmotionNeutral,
        ??bergabe_Soll_DataEmodbEmotionSadness,
        ??bergabe_Soll_DataAbcAffectAgressiv,
        ??bergabe_Soll_DataAbcAffectCheerfull,
        ??bergabe_Soll_DataAbcAffectIntoxicated,
        ??bergabe_Soll_DataAbcAffectNervous,
        ??bergabe_Soll_DataAbcAffectNeutral,
        ??bergabe_Soll_DataAbcAffectTired
        
    ):
        
        Main.Soll_DataEmodbEmotionAnger =         ??bergabe_Soll_DataEmodbEmotionAnger
        Main.Soll_DataEmodbEmotionBoredom =       ??bergabe_Soll_DataEmodbEmotionBoredom
        Main.Soll_DataEmodbEmotionDisgust =       ??bergabe_Soll_DataEmodbEmotionDisgust
        Main.Soll_DataEmodbEmotionFear =          ??bergabe_Soll_DataEmodbEmotionFear
        Main.Soll_DataEmodbEmotionHappiness =     ??bergabe_Soll_DataEmodbEmotionHappiness
        Main.Soll_DataEmodbEmotionNeutral =       ??bergabe_Soll_DataEmodbEmotionNeutral
        Main.Soll_DataEmodbEmotionSadness =       ??bergabe_Soll_DataEmodbEmotionSadness
        Main.Soll_DataAbcAffectAgressiv =         ??bergabe_Soll_DataAbcAffectAgressiv
        Main.Soll_DataAbcAffectCheerfull =        ??bergabe_Soll_DataAbcAffectCheerfull
        Main.Soll_DataAbcAffectIntoxicated =      ??bergabe_Soll_DataAbcAffectIntoxicated
        Main.Soll_DataAbcAffectNervous =          ??bergabe_Soll_DataAbcAffectNervous
        Main.Soll_DataAbcAffectNeutral =          ??bergabe_Soll_DataAbcAffectNeutral
        Main.Soll_DataAbcAffectTired =            ??bergabe_Soll_DataAbcAffectTired"""
        
        
    def Get_Score():
        
        Main.Set_Absolut_Difference()
        Main.Score_EmodbEmotions = (sum(Main.Data_Difference_Score_EmodbEmotion)) / (sum(Main.DataLength)+0.0000001)
        Main.Score_AbcAffect = (sum(Main.Data_Difference_Score_AbcAffect)) / (sum(Main.DataLength)+0.0000001)
        Main.Score_Retiva = (Main.Score_EmodbEmotions+Main.Score_AbcAffect)/2
        
    
    def Get_Live_Score():
        
        Main.Set_Absolut_Difference()
        
        Score_EmodbEmotions = ((Main.Data_Difference_Score_EmodbEmotion)) / ((Main.DataLength))
        Score_AbcAffect = ((Main.Data_Difference_Score_AbcAffect)) / ((Main.DataLength))
        
        
        return (Score_EmodbEmotions, Score_AbcAffect)
        
    
    def Get_Loi_Score():
        if Main.DataLoi1[-1] > Main.DataLoi2[-1] and Main.DataLoi1[-1] > Main.DataLoi3[-1]:
            Main.Loi_Score = (Main.DataLoi2[-1] + (2*Main.DataLoi3[-1]))/2
            
        elif Main.DataLoi2[-1] > Main.DataLoi1[-1] and Main.DataLoi2[-1] > Main.DataLoi3[-1]:
            Main.Loi_Score = (1 + (Main.DataLoi3[-1] - Main.DataLoi1[-1]))/2
            
        else:
            Main.Loi_Score = (2 - (Main.DataLoi2[-1] + (2*Main.DataLoi1[-1])))/2
       
            
    def Get_Abs_Loi_Score():
        if Main.Abs_MW_Data_Loi1 > Main.Abs_MW_Data_Loi2 and Main.Abs_MW_Data_Loi1 > Main.Abs_MW_Data_Loi3:
            Main.Abs_MW_Loi_Score = (Main.Abs_MW_Data_Loi2 + (2*Main.Abs_MW_Data_Loi3))/2
            
        elif Main.Abs_MW_Data_Loi2 > Main.Abs_MW_Data_Loi1 and Main.Abs_MW_Data_Loi2 > Main.Abs_MW_Data_Loi3:
            Main.Abs_MW_Loi_Score = (1 + (Main.Abs_MW_Data_Loi3 - Main.Abs_MW_Data_Loi1))/2
            
        else:
            Main.Abs_MW_Loi_Score = (2 - (Main.Abs_MW_Data_Loi2 + (2*Main.Abs_MW_Data_Loi1)))/2
            
        
    def Get_MWLoi_Score():
        if Main.MWDataLoi1 > Main.MWDataLoi2 and Main.MWDataLoi1 > Main.MWDataLoi3:
            Main.MWLoi_Score = (Main.MWDataLoi2 + (2*Main.MWDataLoi3))/2
        elif Main.MWDataLoi2 > Main.MWDataLoi1 and Main.MWDataLoi2 > Main.MWDataLoi3:
            Main.MWLoi_Score = (1 + (Main.MWDataLoi3 - Main.MWDataLoi1))/2
        else:
            Main.MWLoi_Score = (2 - (Main.MWDataLoi2 + (2*Main.MWDataLoi1)))/2


    def Set_Time_Norm_Values():
        
        
        Main.Time_Norm_Data_Arousal                 =       [x * y for x, y in zip(Main.DataArousal,Main.DataLength)]
        Main.Time_Norm_Data_Valence                 =       [x * y for x, y in zip(Main.DataValence,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionAnger       =       [x * y for x, y in zip(Main.DataEmodbEmotionAnger,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionBoredom     =       [x * y for x, y in zip(Main.DataEmodbEmotionBoredom,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionDisgust     =       [x * y for x, y in zip(Main.DataEmodbEmotionDisgust,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionFear        =       [x * y for x, y in zip(Main.DataEmodbEmotionFear,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionHappiness   =       [x * y for x, y in zip(Main.DataEmodbEmotionHappiness,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionNeutral     =       [x * y for x, y in zip(Main.DataEmodbEmotionNeutral,Main.DataLength)]
        Main.Time_Norm_Data_EmodbEmotionSadness     =       [x * y for x, y in zip(Main.DataEmodbEmotionSadness,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectAgressiv       =       [x * y for x, y in zip(Main.DataAbcAffectAgressiv,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectCheerfull      =       [x * y for x, y in zip(Main.DataAbcAffectCheerfull,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectIntoxicated    =       [x * y for x, y in zip(Main.DataAbcAffectIntoxicated,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectNervous        =       [x * y for x, y in zip(Main.DataAbcAffectNervous,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectNeutral        =       [x * y for x, y in zip(Main.DataAbcAffectNeutral,Main.DataLength)]
        Main.Time_Norm_Data_AbcAffectTired          =       [x * y for x, y in zip(Main.DataAbcAffectTired,Main.DataLength)]
        Main.Time_Norm_Data_Loi1                    =       [x * y for x, y in zip(Main.DataLoi1,Main.DataLength)]
        Main.Time_Norm_Data_Loi2                    =       [x * y for x, y in zip(Main.DataLoi2,Main.DataLength)]
        Main.Time_Norm_Data_Loi3                    =       [x * y for x, y in zip(Main.DataLoi3,Main.DataLength)]


    def Set_Abolute_Verteilung():
        if sum(Main.DataLength) != 0.0:
            Main.Abs_MW_Data_Arousal               = sum(Main.Time_Norm_Data_Arousal)                       /          sum(Main.DataLength)
            Main.Abs_MW_Data_Valence               = sum(Main.Time_Norm_Data_Valence)                       /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionAnger     = sum(Main.Time_Norm_Data_EmodbEmotionAnger)             /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionBoredom   = sum(Main.Time_Norm_Data_EmodbEmotionBoredom)           /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionDisgust   = sum(Main.Time_Norm_Data_EmodbEmotionDisgust)           /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionFear      = sum(Main.Time_Norm_Data_EmodbEmotionFear)              /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionHappiness = sum(Main.Time_Norm_Data_EmodbEmotionHappiness)         /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionNeutral   = sum(Main.Time_Norm_Data_EmodbEmotionNeutral)           /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotionSadness   = sum(Main.Time_Norm_Data_EmodbEmotionSadness)           /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectAgressiv     = sum(Main.Time_Norm_Data_AbcAffectAgressiv)             /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectCheerfull    = sum(Main.Time_Norm_Data_AbcAffectCheerfull)            /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectIntoxicated  = sum(Main.Time_Norm_Data_AbcAffectIntoxicated)          /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectNervous      = sum(Main.Time_Norm_Data_AbcAffectNervous)              /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectNeutral      = sum(Main.Time_Norm_Data_AbcAffectNeutral)              /          sum(Main.DataLength)
            Main.Abs_MW_Data_AbcAffectTired        = sum(Main.Time_Norm_Data_AbcAffectTired)                /          sum(Main.DataLength)
            Main.Abs_MW_Data_Loi1                  = sum(Main.Time_Norm_Data_Loi1)                          /          sum(Main.DataLength)
            Main.Abs_MW_Data_Loi2                  = sum(Main.Time_Norm_Data_Loi2)                          /          sum(Main.DataLength)
            Main.Abs_MW_Data_Loi3                  = sum(Main.Time_Norm_Data_Loi3)                          /          sum(Main.DataLength)
            Main.Abs_MW_Data_EmodbEmotion_List = [Main.Abs_MW_Data_EmodbEmotionAnger, Main.Abs_MW_Data_EmodbEmotionBoredom, Main.Abs_MW_Data_EmodbEmotionDisgust, Main.Abs_MW_Data_EmodbEmotionFear, Main.Abs_MW_Data_EmodbEmotionHappiness, Main.Abs_MW_Data_EmodbEmotionNeutral, Main.Abs_MW_Data_EmodbEmotionSadness]
            Main.Abs_MW_Data_AbcAffect_List = [Main.Abs_MW_Data_AbcAffectAgressiv, Main.Abs_MW_Data_AbcAffectCheerfull, Main.Abs_MW_Data_AbcAffectIntoxicated, Main.Abs_MW_Data_AbcAffectNervous, Main.Abs_MW_Data_AbcAffectNeutral, Main.Abs_MW_Data_AbcAffectTired]
            Main.Soll_Data_EmodbEmotion_List = [Main.Soll_DataEmodbEmotionAnger, Main.Soll_DataEmodbEmotionBoredom, Main.Soll_DataEmodbEmotionDisgust, Main.Soll_DataEmodbEmotionFear, Main.Soll_DataEmodbEmotionHappiness, Main.Soll_DataEmodbEmotionNeutral, Main.Soll_DataEmodbEmotionSadness]
            Main.Soll_Data_AbcAffect_List = [Main.Soll_DataAbcAffectAgressiv, Main.Soll_DataAbcAffectCheerfull, Main.Soll_DataAbcAffectIntoxicated, Main.Soll_DataAbcAffectNervous, Main.Soll_DataAbcAffectNeutral, Main.Soll_DataAbcAffectTired]
        

    def Get_Soll_Werte(
        ??bergabe_Gewichte_DataEmodbEmotionAnger,
        ??bergabe_Gewichte_DataEmodbEmotionBoredom,
        ??bergabe_Gewichte_DataEmodbEmotionDisgust,
        ??bergabe_Gewichte_DataEmodbEmotionFear,
        ??bergabe_Gewichte_DataEmodbEmotionHappiness,
        ??bergabe_Gewichte_DataEmodbEmotionNeutral,
        ??bergabe_Gewichte_DataEmodbEmotionSadness,
        ??bergabe_Gewichte_DataAbcAffectAgressiv,
        ??bergabe_Gewichte_DataAbcAffectCheerfull,
        ??bergabe_Gewichte_DataAbcAffectIntoxicated,
        ??bergabe_Gewichte_DataAbcAffectNervous,
        ??bergabe_Gewichte_DataAbcAffectNeutral,
        ??bergabe_Gewichte_DataAbcAffectTired
    ):
        
        
        Main.Soll_DataEmodbEmotionAnger        =         ??bergabe_Gewichte_DataEmodbEmotionAnger        /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness)
        Main.Soll_DataEmodbEmotionBoredom      =         ??bergabe_Gewichte_DataEmodbEmotionBoredom      /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness)
        Main.Soll_DataEmodbEmotionDisgust      =         ??bergabe_Gewichte_DataEmodbEmotionDisgust      /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness) 
        Main.Soll_DataEmodbEmotionFear         =         ??bergabe_Gewichte_DataEmodbEmotionFear         /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness) 
        Main.Soll_DataEmodbEmotionHappiness    =         ??bergabe_Gewichte_DataEmodbEmotionHappiness    /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness) 
        Main.Soll_DataEmodbEmotionNeutral      =         ??bergabe_Gewichte_DataEmodbEmotionNeutral      /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness) 
        Main.Soll_DataEmodbEmotionSadness      =         ??bergabe_Gewichte_DataEmodbEmotionSadness      /     (??bergabe_Gewichte_DataEmodbEmotionAnger+??bergabe_Gewichte_DataEmodbEmotionBoredom+??bergabe_Gewichte_DataEmodbEmotionDisgust+??bergabe_Gewichte_DataEmodbEmotionFear+??bergabe_Gewichte_DataEmodbEmotionHappiness+??bergabe_Gewichte_DataEmodbEmotionNeutral+??bergabe_Gewichte_DataEmodbEmotionSadness) 
        
        Main.Soll_DataAbcAffectAgressiv        =         ??bergabe_Gewichte_DataAbcAffectAgressiv        /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        Main.Soll_DataAbcAffectCheerfull       =         ??bergabe_Gewichte_DataAbcAffectCheerfull       /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        Main.Soll_DataAbcAffectIntoxicated     =         ??bergabe_Gewichte_DataAbcAffectIntoxicated     /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        Main.Soll_DataAbcAffectNervous         =         ??bergabe_Gewichte_DataAbcAffectNervous         /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        Main.Soll_DataAbcAffectNeutral         =         ??bergabe_Gewichte_DataAbcAffectNeutral         /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        Main.Soll_DataAbcAffectTired           =         ??bergabe_Gewichte_DataAbcAffectTired           /     (??bergabe_Gewichte_DataAbcAffectAgressiv+??bergabe_Gewichte_DataAbcAffectCheerfull+??bergabe_Gewichte_DataAbcAffectIntoxicated+??bergabe_Gewichte_DataAbcAffectNervous+??bergabe_Gewichte_DataAbcAffectNeutral+??bergabe_Gewichte_DataAbcAffectTired)
        
        
        
        
        """Main.Set_Soll_Werte(
            ??bergabe_Soll_DataEmodbEmotionAnger,
            ??bergabe_Soll_DataEmodbEmotionBoredom,
            ??bergabe_Soll_DataEmodbEmotionDisgust,
            ??bergabe_Soll_DataEmodbEmotionFear,
            ??bergabe_Soll_DataEmodbEmotionHappiness,
            ??bergabe_Soll_DataEmodbEmotionNeutral,
            ??bergabe_Soll_DataEmodbEmotionSadness,
            ??bergabe_Soll_DataAbcAffectAgressiv,
            ??bergabe_Soll_DataAbcAffectCheerfull,
            ??bergabe_Soll_DataAbcAffectIntoxicated,
            ??bergabe_Soll_DataAbcAffectNervous,
            ??bergabe_Soll_DataAbcAffectNeutral,
            ??bergabe_Soll_DataAbcAffectTired
        )"""


    def get_highest_EmoDb():
        
        # Create a dictionary to store the variable names and their values
        variables = {'Anger': Main.DataEmodbEmotionAnger[-1], 'Boredom': Main.DataEmodbEmotionBoredom[-1], 'Disgust': Main.DataEmodbEmotionDisgust[-1], 'Fear': Main.DataEmodbEmotionFear[-1], 'Happiness': Main.DataEmodbEmotionHappiness[-1], 'Neutral': Main.DataEmodbEmotionNeutral[-1], 'Sadness': Main.DataEmodbEmotionSadness[-1]}
        
        # Find the highest value and the corresponding variable name
        highest_value = max(variables.values())
        highest_name = [name for name, value in variables.items() if value == highest_value][0]
        
        # Return the variable name as a string
        return highest_name


    def get_highest_AbcAffect():
        # Create a dictionary to store the variable names and their values
        variables = {'Aggressiv': Main.DataAbcAffectAgressiv[-1], 'Cheerful': Main.DataAbcAffectCheerfull[-1], 'Intoxicated': Main.DataAbcAffectIntoxicated[-1], 'Nervous': Main.DataAbcAffectNervous[-1], 'Neutral': Main.DataAbcAffectNervous[-1], 'Tired': Main.DataAbcAffectTired[-1]}
        
        
        # Find the highest value and the corresponding variable name
        highest_value = max(variables.values())
        highest_name = [name for name, value in variables.items() if value == highest_value][0]
        
        # Return the variable name as a string
        return highest_name


    def Updater():
        print("The analysis is running... ")

        Main.read_log_file(Main.file_path)
        Main.get_length_of_last_added_wav(Main.directory_path)
        #Main.zusammenf??hrer()
        Main.get_speak_ratio()
        Main.Gleitender_Mittelwert()
        Main.Set_Time_Norm_Values()
        Main.Set_Abolute_Verteilung()
        Main.Get_Score()
        Main.Get_Loi_Score()
        Main.Get_Abs_Loi_Score()
        Main.Get_MWLoi_Score()
        #Main.Printer()
        Main.write_excel_file(Main.archive_path, Main.Excel_Filename)



Main.delete_old_wav_files(Main.directory_path)
Main.Set_Session_Name(None)

#floats = (0.06743775, 0.29886375, 0.06159575, 0.30633225, 0.09225925, 0.1257095, 0.04780175, 0.5911573631587611,0.006152395,0.306738115,0.23492557,0.179188181,0.272995739)
#Main.Set_Soll_Werte23(*floats)
#print(Main.Excel_Filename)
#print(Main.Soll_DataEmodbEmotionAnger)

"""#Main.Soll_Data_EmodbEmotion_List = [0.06743775, 0.29886375, 0.06159575, 0.30633225, 0.09225925, 0.1257095, 0.04780175]
Main.Abs_MW_Data_EmodbEmotion_List = [0.06743775, 0.29886375, 0.06159575, 0.30633225, 0.09225925, 0.1257095, 0.04780175]
Main.Abs_MW_Data_AbcAffect_List = [0.06743775, 0.29886375, 0.06159575, 0.30633225, 0.09225925, 0.1257095]
#Main.Soll_Data_EmodbEmotion_List = []
Main.Abs_MW_Data_EmodbEmotionAnger=0.06743775
Main.Abs_MW_Data_EmodbEmotionBoredom=0.29886375
Main.Abs_MW_Data_EmodbEmotionDisgust=0.06159575
Main.Abs_MW_Data_EmodbEmotionFear=0.30633225
Main.Abs_MW_Data_EmodbEmotionHappiness=0.09225925
Main.Abs_MW_Data_EmodbEmotionNeutral=0.1257095
Main.Abs_MW_Data_EmodbEmotionSadness=0.04780175
Main.Abs_MW_Data_Arousal= 0.432
Main.Abs_MW_Data_Valence= 0.1
Main.Abs_MW_Data_AbcAffectAgressiv= 0.34276
Main.Abs_MW_Data_AbcAffectCheerfull= 0.34276
Main.Abs_MW_Data_AbcAffectIntoxicated= 0.34276
Main.Abs_MW_Data_AbcAffectNervous= 0.34276
Main.Abs_MW_Data_AbcAffectNeutral= 0.34276
Main.Abs_MW_Data_AbcAffectTired= 0.34276
Main.Abs_MW_Data_Loi1= 0.34276
Main.Abs_MW_Data_Loi2= 0.34276
Main.Abs_MW_Data_Loi3= 0.34276"""


