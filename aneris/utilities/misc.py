# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es archivo temporal
"""

from copy import deepcopy
from collections import MutableSet

class Injective:
    
    '''Provides a one to one mapping structure'''
    
    def __init__(self):
        
       self._d = {}
       
       return
       
    def add(self, k, v):
        
       self._d[k] = v
       self._d[v] = k
       
       return
       
    def remove(self, k):
        
       self._d.pop(self._d.pop(k))
       
       return
       
    def get(self, k):
        
       return self._d[k]
       

class OrderedSet(MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


def safe_update(dst_dict, src_dict, allow_none=False):
    
    '''Update the dst_dict using the src_dict, but only the keys contained
    in dst_dict, and where values in the src_dict are not None, assuming
    allow_none is False'''
    
    dst_copy = deepcopy(dst_dict)
    
    if allow_none:
        
        src_copy = deepcopy(src_dict)
        
    else:
        
        src_copy = {k: v for k, v in src_dict.iteritems() if v is not None}

    dst_copy.update((k, src_copy[k]) for k in dst_copy.viewkeys() &
                                              src_copy.viewkeys())
    
    return dst_copy
