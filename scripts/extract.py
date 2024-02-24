from logs.log import log
import pandas as pd

class Extract:
    '''
    Extract the data
    '''
    def read_data(self, path):
        '''
        Load in new data from CSV file
        '''
        try:
            data = pd.read_csv(path)
        except UnicodeDecodeError:
            print('There has been an encoding error, please check the file you are loading is in \
                UTF-8 encoding.')
        log("Read data operation completed successfully")
        log("Returning the data frame")
        return data
    
    