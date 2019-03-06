import logging
logger = logging.getLogger(__name__)
logger.debug("Loaded " + __name__)

class Behaviour(object):
    def __init__(self, Config):
        self.id = Config["_id"]
        self.enabled = True
        self.Config  = Config
    
    def run(self, data, params):
        return(data)
