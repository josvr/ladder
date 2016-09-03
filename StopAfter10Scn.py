from blocks.extensions import Printing, SimpleExtension

class StopAfterNoImprovement(Printing):
    def __init__(self, to_print, use_log=True, **kwargs):
        self.to_print = to_print
        self.use_log = use_log
        super(StopAfterNoImprovement, self).__init__(**kwargs)

    def do(self, which_callback, *args):
        iteration = log.status['epochs_done']
        print("JosStopAfterNoImprovement iteration="+str(iteration))
