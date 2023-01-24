import logging
import random
import time
import os

class Main():
    Time = 0.0

    arousel:  float
    valence:  float

    EmoDbEmotionAnger:  float
    EmoDbEmotionboredom: float
    EmoDbEmotiondisgust: float
    EmoDbEmotionfear: float
    EmoDbEmotionhappiness: float
    EmoDbEmotionneutral: float
    EmoDbEmotionsadness: float



    AbcAffectaggresive :  float
    AbcAffectcheerful :  float
    AbcAffectintoxicated :  float
    AbcAffectnervous :  float
    AbcAffectneutral :  float
    AbcAffecttired :  float

    Loi1 :  float
    Loi2 :  float
    Loi3 :  float



    def randomizer():
        
        Main.Time= Main.Time + random.uniform(1,2)
        
        Main.arousel= random.uniform(0,1)
        Main.valence= random.uniform(0,1)

        Main.EmoDbEmotionAnger= random.uniform(0,1)
        Main.EmoDbEmotionboredom=random.uniform(0,1)
        Main.EmoDbEmotiondisgust=random.uniform(0,1)
        Main.EmoDbEmotionfear=random.uniform(0,1)
        Main.EmoDbEmotionhappiness=random.uniform(0,1)
        Main.EmoDbEmotionneutral=random.uniform(0,1)
        Main.EmoDbEmotionsadness=random.uniform(0,1)
        
        

        Main.AbcAffectaggresive = random.uniform(0,1)
        Main.AbcAffectcheerful = random.uniform(0,1)
        Main.AbcAffectintoxicated = random.uniform(0,1)
        Main.AbcAffectnervous = random.uniform(0,1)
        Main.AbcAffectneutral = random.uniform(0,1)
        Main.AbcAffecttired = random.uniform(0,1)

        Main.Loi1 = random.uniform(0,1)
        Main.Loi2 = random.uniform(0,1)
        Main.Loi3 = random.uniform(0,1)
        

        Main.EmoDbEmotionAnger=      Main.EmoDbEmotionAnger      / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotionboredom=    Main.EmoDbEmotionboredom    / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotiondisgust=    Main.EmoDbEmotiondisgust    / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotionfear=       Main.EmoDbEmotionfear       / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotionhappiness=  Main.EmoDbEmotionhappiness  / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotionneutral=    Main.EmoDbEmotionneutral    / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        Main.EmoDbEmotionsadness=    Main.EmoDbEmotionsadness    / (Main.EmoDbEmotionAnger+Main.EmoDbEmotionboredom+Main.EmoDbEmotiondisgust+Main.EmoDbEmotionfear+Main.EmoDbEmotionhappiness+Main.EmoDbEmotionneutral+Main.EmoDbEmotionsadness)
        
        

        Main.AbcAffectaggresive   =        Main.AbcAffectaggresive   / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)
        Main.AbcAffectcheerful    =        Main.AbcAffectcheerful    / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)
        Main.AbcAffectintoxicated =        Main.AbcAffectintoxicated / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)
        Main.AbcAffectnervous     =        Main.AbcAffectnervous     / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)
        Main.AbcAffectneutral     =        Main.AbcAffectneutral     / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)
        Main.AbcAffecttired       =        Main.AbcAffecttired       / (Main.AbcAffectaggresive+Main.AbcAffectcheerful+Main.AbcAffectintoxicated+Main.AbcAffectnervous+Main.AbcAffectneutral+Main.AbcAffecttired)

        Main.Loi1 = Main.Loi1 / (Main.Loi1+Main.Loi2+Main.Loi3)
        Main.Loi2 = Main.Loi2 / (Main.Loi1+Main.Loi2+Main.Loi3)
        Main.Loi3 = Main.Loi3 / (Main.Loi1+Main.Loi2+Main.Loi3)



    def random_log():
        # Set up logging to a file
        log_file = os.path.join('/Users/paul/Documents/GitHub/ReTiVa3.0/openEAR-0.1.0 Kopie/', 'Smile1.log')
        logging.basicConfig(filename=log_file, level=logging.DEBUG)

        # List of 25 lines
        lines = [
                "",
                "LibSVM  'arousal' result (@ time: "+ str(Main.Time) +") :  ~~> "+ str(Main.arousel) +" <~~",
                "", 
                "LibSVM  'valence' result (@ time: "+ str(Main.Time) +") :  ~~> "+ str(Main.valence) +" <~~",
                "", 
                "LibSVM  'emodbEmotion' result (@ time: "+ str(Main.Time) +") :  ~~> disgust <~~",
                "     prob. class 'anger': 	 "+ str(Main.EmoDbEmotionboredom),
                "     prob. class 'boredom': 	 "+ str(Main.EmoDbEmotiondisgust),
                "     prob. class 'disgust': 	 "+ str(Main.EmoDbEmotionfear),
                "     prob. class 'fear': 	 "+ str(Main.EmoDbEmotionhappiness),
                "     prob. class 'happiness': 	 "+ str(Main.EmoDbEmotionneutral),
                "     prob. class 'neutral': 	 "+ str(Main.EmoDbEmotionsadness),
                "     prob. class 'sadness': 	 "+ str(Main.EmoDbEmotionAnger),
                "",
                "LibSVM  'abcAffect' result (@ time: "+ str(Main.Time) +") :  ~~> agressiv <~~" ,
                "     prob. class 'agressiv': 	 "+ str(Main.AbcAffectaggresive),
                "     prob. class 'cheerful': 	 "+ str(Main.AbcAffectcheerful),
                "     prob. class 'intoxicated': 	 "+ str(Main.AbcAffectintoxicated) ,
                "     prob. class 'nervous': 	 "+ str(Main.AbcAffectnervous),
                "     prob. class 'neutral': 	 "+ str(Main.AbcAffectneutral),
                "     prob. class 'tired': 	 "+ str(Main.AbcAffecttired),
                "",
                " LibSVM  'avicInterest' result (@ time: "+ str(Main.Time) +") :  ~~><~~",
                "     prob. class 'loi1': 	 "+ str(Main.Loi1) ,
                "     prob. class 'loi2': 	 "+ str(Main.Loi2),
                "     prob. class 'loi3': 	 "+ str(Main.Loi3)]

        # Iterate through the list and write each line to the log file
        for line in lines:
            logging.debug(line)


"""while True:
    Main.randomizer()
    Main.random_log()
    time.sleep(2)"""
