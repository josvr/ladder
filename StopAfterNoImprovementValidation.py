import os
import logging
from blocks.extensions import Printing, SimpleExtension
import numpy as np
from pandas import DataFrame, read_hdf

logger = logging.getLogger('main.utils')

#
# Probably we can also implement this using FinishAfter, but this also works ;-)
#

class StopAfterNoImprovementValidation(Printing):
    def __init__(self, variable_string, threshold_epochs ,params, experiment_params,save_path, **kwargs):
        self.init = False
        self.save_path = save_path
        self.params = params
        self.experiment_params = experiment_params
        self.lowest = 0
        self.variable_string = variable_string
        self.threshold_epochs = threshold_epochs
        super(StopAfterNoImprovementValidation, self).__init__(**kwargs)

    def save(self):
        to_save = {v.name: v.get_value() for v in self.params}
        path = self.save_path + '/trained_params'
        logger.info('Saving parameters %s' % self.save_path)
        np.savez_compressed(path, **to_save)
        df = DataFrame.from_dict(self.experiment_params, orient='index')
        df.to_hdf(os.path.join(self.save_path, 'params'), 'params', mode='w',complevel=5, complib='blosc')
        df = DataFrame.from_dict(self.main_loop.log, orient='index')
        df.to_hdf(os.path.join(self.save_path, 'log'), 'log', mode='w',complevel=5, complib='blosc')

    def do(self, which_callback, *args):
        log = self.main_loop.log
        iteration = log.status['epochs_done']
        if iteration == 0:
           return
        error = log.current_row[self.variable_string]
        msg = 'Iteration='+(str(iteration))+' error='+str(error)
        if self.init == False:
          self.init = True
          self.lowest_error = error
          self.counter = 0
          logger.info(msg)
          self.save()
        else:
          if error < self.lowest_error*0.995:
             msg+=' new low ('+str(error)+')'
             logger.info(msg)
             self.lowest_error = error
             self.counter = 0
             self.save()
          else: 
             self.counter = self.counter + 1
             msg+=' no new low ('+str(error)+' vs last '+str(self.lowest_error)+'). Failed = '+str(self.counter)
             logger.info(msg)
        if self.threshold_epochs == self.counter: 
           logger.info("Stop -> Epochs = "+str(self.counter)+" and no new low.")
           self.main_loop.log.current_row['training_finish_requested'] = True
