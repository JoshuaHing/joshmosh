#!/usr/bin/python3.5

import os, sys, traceback
try:
    from wsgiref.handlers import CGIHandler
    from werkzeug.debug import DebuggedApplication
    from joshmosh import app
    if 'PATH_INFO' not in os.environ:
        os.environ['PATH_INFO'] = ''
    app.secret_key = 'correct horse battery staple'
    app.debug = True
    CGIHandler().run(DebuggedApplication(app))
except Exception:
    print('Content-Type: text/plain\n', flush=True)
    etype, evalue, etraceback = sys.exc_info()
    print("\n".join(traceback.format_exception_only(etype, evalue)), flush=True)
    traceback.print_exc(file=sys.stdout)
