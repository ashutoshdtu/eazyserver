import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

class FunctionMapper():
    def __init__(self):
        self.routes = {}

    def add(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def get(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function
        else:
            raise ValueError('Route "{}"" has not been registered'.format(path))

    def _routes(self):
        return self.routes.keys()
