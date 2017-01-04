
import __builtin__

from copy import deepcopy

from aneris.boundary import DataDefinition, Structure

import pandas as pd

class testDefinition(DataDefinition):

    @property
    def package_name(self):

        return "aneris"

    @property
    def company_name(self):

        return "DTOcean"

    @property
    def local_yaml_dir(self):
        '''The paths of the yaml definition files.'''
        return 'yaml'

    @property
    def  user_yaml_dir(self):
        '''The paths of the yaml definition files.'''
        return None


class UnitData(Structure):

    '''A single item of data'''

    def get_data(self, raw, meta_data):

        return raw

    def get_value(self, data):

        return deepcopy(data)


class Simple(Structure):

    '''Simple single value data such as a bool, str, int or float'''

    def get_data(self, raw, meta_data):

        simple = raw

        if meta_data._types:

            try:
                simple_type = getattr(__builtin__, meta_data._types[0])
                simple = simple_type(simple)
            except TypeError:
                errStr = ("Raw data is of incorrect type. Should be "
                          "{}, but is {}.").format(meta_data._types,
                                                   type(simple))
                raise TypeError(errStr)

        return simple

    def get_value(self, data):

        return deepcopy(data)


class SimpleList(Structure):

    '''Simple list of value data such as a bool, str, int or float'''

    def get_data(self, raw, meta_data):

        raw_list = raw

        if meta_data._types:

            simple_list = []

            for item in raw_list:

                try:
                    simple_type = getattr(__builtin__,
                                          meta_data._types[0])
                    simple_item = simple_type(item)
                except TypeError:
                    errStr = ("Raw data is of incorrect type. Should be "
                              "{}, but is {}.").format(meta_data._types[0],
                                                       type(item))
                    raise TypeError(errStr)

                simple_list.append(simple_item)
                
        else:
            
            simple_list = raw_list

        return simple_list

    def get_value(self, data):

        return data[:]

class SeriesData(Structure):

    '''Structure represented in a series of some sort'''

    def get_data(self, raw, meta_data):

        series = pd.Series(raw)

        return series

    def get_value(self, data):

        return data.copy()


class TableData(Structure):

    '''Structure represented in a pandas dataframe'''

    def get_data(self, raw, meta_data):

        dataframe = pd.DataFrame(raw)

        return dataframe

    def get_value(self, data):

        return data.copy()
