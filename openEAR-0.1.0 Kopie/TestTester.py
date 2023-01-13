import logging
import random
import time
import os
I = 1
def random_log():
    
    # Set up logging to a file
    log_file = os.path.join('openEAR-0.1.0 Kopie/test_log_files', 'Smile1.log')
    logging.basicConfig(filename=log_file, level=logging.DEBUG)

    # List of 25 lines
    lines = ["LibSVM  'arousal' result (@ time: "+ str(I) +") :  ~~> "+ str(random.uniform(0,1)) +" <~~",
            "", 
            "LibSVM  'valence' result (@ time: "+ str(random.uniform(0,1)) +") :  ~~> "+ str(random.uniform(0,1)) +" <~~",
            "", 
            "LibSVM  'emodbEmotion' result (@ time: "+ str(random.uniform(0,1)) +") :  ~~> disgust <~~",
            "     prob. class 'anger': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'boredom': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'disgust': 	 "+ str(random.uniform(0,1)) ,
            "     prob. class 'fear': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'happiness': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'neutral': 	 "+ str(random.uniform(0,1)) ,
            "     prob. class 'sadness': 	 "+ str(random.uniform(0,1)),
            "",
            "LibSVM  'abcAffect' result (@ time: "+ str(random.uniform(0,1)) +") :  ~~> agressiv <~~" ,
            "     prob. class 'agressiv': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'cheerful': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'intoxicated': 	 "+ str(random.uniform(0,1)) ,
            "     prob. class 'nervous': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'neutral': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'tired': 	 "+ str(random.uniform(0,1)),
            "",
            " LibSVM  'avicInterest' result (@ time: "+ str(random.uniform(0,1)) +") :  ~~> "+ str(random.uniform(0,1)) +" <~~",
            "     prob. class 'loi1': 	 "+ str(random.uniform(0,1)) ,
            "     prob. class 'loi2': 	 "+ str(random.uniform(0,1)),
            "     prob. class 'loi3': 	 "+ str(random.uniform(0,1))]

    # Iterate through the list and write each line to the log file
    for line in lines:
        logging.debug(line)
    
    


while True:
    random_log()
    I = I+1
    time.sleep(5)
