import pandas as pd

@pd.api.extensions.register_series_accessor('nlp')
class NlpSeriesAccessor(object):
    def __init__(self, s):
        self._s = s
    
    def __list_in(self, _source: list, _target: list) -> bool:
        for target in _target:
            if target in _source:
                return True
        return False

    def is_wordin(self, word_list: list):
        '''
        check if the word is in the passed word_list

        Parameters
        ----------
        words_list: list
            word list
        
        Returns
        -------
        series: pandas.core.series.Series
        '''

        series = self._s.apply(lambda x: False if pd.isna(x) else self.__list_in(x.split(' '), word_list))
        return series