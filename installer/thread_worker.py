from functools import partial
from PySide2.QtCore import Signal, Slot, QRunnable, QObject

import traceback
import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class ThreadButton(QPushButton):
    
    def __init__(self, text, form, threadpool):
        super(ThreadButton, self).__init__()
        print(threadpool)
        self.form = form
        self.form.buttons.append(self)
        self.threadpool = threadpool
        self.setText(text)

    def quick_start(self, threaded_func, result_func=None, finished_func=None, error_func=None):
        print('threaded_func', threaded_func)
        print('result', result_func)
        print('error_func', error_func)

        self.connect_worker(threaded_func)
        self.connect_result(result_func)
        self.connect_finished(finished_func)
        self.connect_error_handler(error_func)
        self.start()

    def start(self):
        self.form.toggle_button_enabled(False)
        self.threadpool.start(self.query_worker)

    def _run_func(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            pass
        finally:
            self.form.toggle_button_enabled(True)

    def connect_worker(self, func, *args, **kwargs):
        self.query_worker = Worker(func, *args, **kwargs)

    def connect_result(self, func, *args, **kwargs):
        self.query_worker.result.connect(partial(self._run_func, func, *args, **kwargs))

    def connect_error_handler(self, func, *args, **kwargs)
        self.query_worker.error.connect(partial(self._run_func, func, *args, **kwargs))

    def connect_finished(self, func, *args, **kwargs)
        self.query_worker.finished.connect(partial(self._run_func, func, *args, **kwargs))

    def connect_line_edit(self, line_edit):
        line_edit.returnPressed.connect(self.clicked.emit)

class Worker(QRunnable):


    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        
        self.signals = WorkerSignals()

        self.finished = self.signals.finished
        self.error = self.signals.error
        self.result = self.signals.result
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot() #QtCore.Slot
    def run(self):

        try: 
            data = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.result.emit(data)  #Return the result of the processing 
        finally:
            self.finished.emit()  #Done

class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)