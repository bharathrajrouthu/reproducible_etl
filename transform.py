def transform(self):
    '''
    To transform and clean the raw data
    Consider 1. generic transformation
                2. complex transformations
                    3. rare transformations
    '''
    pass

def check_duplicates(self, remove:bool=False):
    '''
    Check for duplicates 
    :param remove: Boolean set to True if the duplicates should be removed
    '''
    dupes = len(self.data) - len(self.data.drop_duplicates())

    if dupes is not None:
        self.messages.update({'Duplicates': dupes})
    if remove:
        self.data.drop_duplicates(inplace= True)
    