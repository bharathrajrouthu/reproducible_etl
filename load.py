def load_csv(self, path: str):
    '''
    Load to a csv file
    :param path: Path to the csv file to load data into
    '''
    self.data.to_csv(path)

def load_pickle(self, path):
    '''
    Load to an pkl file
    :param path: Path to the pkl file to load data into
    '''
    self.data.to_pickle(path)