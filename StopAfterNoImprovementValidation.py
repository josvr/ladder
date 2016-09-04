from blocks.extensions import Printing, SimpleExtension

#
# Probably we can also implement this using FinishAfter, but this also works ;-)
#

class StopAfterNoImprovementValidation(Printing):
    def __init__(self, variable_string, threshold_epochs , **kwargs):
        self.init = False
        self.lowest = 0
        self.variable_string = variable_string
        self.threshold_epochs = threshold_epochs
        super(StopAfterNoImprovementValidation, self).__init__(**kwargs)

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
        else:
          if error < self.lowest_error*0.995:
             msg+=' new low ('+str(error)+')'
             self.lowest_error = error
             self.counter = 0
          else: 
             self.counter = self.counter + 1
             msg+=' no new low ('+str(error)+' vs last '+str(self.lowest_error)+'). Failed = '+str(self.counter)
        print(msg)
        if self.threshold_epochs == self.counter: 
           print("Stop -> Epochs = "+str(self.counter)+" and no new low.")
           self.main_loop.log.current_row['training_finish_requested'] = True
