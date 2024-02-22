import pandas as pd

def load_data(self):
    '''
    Load in new data from CSV file
    '''
    try:
        data = pd.read_csv(self.path)
    except UnicodeDecodeError:
        print('There has been an encoding error, please check the file you are loading is in \
              UTF-8 encoding.')
        
    self.data = data
    
    
        