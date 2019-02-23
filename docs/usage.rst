=====
Usage
=====

To use eazyserver in a project::

    from eazyserver import Eazy
    app = Eazy(__name__, settings='settings.py', configs=['config.ini', 'config.prod.ini'], env_prefix='APP')

    app.run(host=app.config['HOST'], port=app.config['PORT'], threaded=app.config['THREADED'])
