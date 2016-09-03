from fuel.datasets import H5PYDataset
import os.path;
from fuel import config

# -*- coding: utf-8 -*-
import os

from fuel.utils import find_in_data_path
from fuel import config
from fuel.datasets import H5PYDataset
from fuel.transformers.defaults import uint8_pixels_to_floatX


class JOS(H5PYDataset):

    filename = 'jos.hdf5'

    default_transformers = uint8_pixels_to_floatX(('features',))

    def __init__(self, which_sets, **kwargs):
        kwargs.setdefault('load_in_memory', False)
        super(JOS, self).__init__(
            file_or_path=find_in_data_path(self.filename),
            which_sets=which_sets, **kwargs)

