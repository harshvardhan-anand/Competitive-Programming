# https://compucademy.net/python-trace-tables/
# Frame methods -  https://docs.python.org/3/library/inspect.html
# All Events in settrace - https://docs.python.org/3/library/sys.html#sys.settrace
# Handle Exception Traceback - https://docs.python.org/3/library/sys.html#sys.tracebacklimit

'''
Usages - 
    # start_trace and end_trace are functions. 
    # Call start_trace to create trace table for variables.
    # Call end_trace to generate report
    # If you have your variables in global scope then create a main function and then call start_trace.
    from trace_table import start_trace, end_trace
    
    # If you want to generate HTML table then do
    from trace_table import start_trace, end_trace, tracer
    tracer.as_html = True
'''

import sys
import pandas as pd

class Tracer:
    def __init__(self):
        self.as_html = False
        self.traced = {}
        self.debug = True
        self.variables = [] # To track order of entry of variable
        self.traced['line'] = []
        self.traced['event'] = []
        self.traced['var'] = {}
    def trace(self, frame, event, arg_unused):
        if frame.f_locals:
            self.traced['line'].append(frame.f_lineno)
            self.traced['event'].append(event)
            for variable, value in frame.f_locals.items():
                if variable not in self.traced['var']:
                    self.traced['var'][variable] = []
                self.traced['var'][variable].append(value)
                if variable not in self.variables:
                    self.variables.append(variable)
            if tracer.debug:
                with open('trace_table_debug.txt', 'a') as f:
                    f.write(f"{frame.f_lineno} --> {event} --> {frame.f_locals}\n")
        # print(frame.f_lineno, '-->', event, '-->', frame.f_locals)
        return self.trace

    def report(self):
        total_execution = len(self.traced['line'])
        print(len(self.variables[0]))
        print(total_execution)
        for var in self.traced['var']:
            len_of_var = len(self.traced['var'][var])
            temp = ['']*(total_execution-len_of_var)
            temp+=self.traced['var'][var]
            self.traced['var'][var]=list(temp)

        variables = {}
        for var in self.variables:
            variables[var] = self.traced['var'][var]
        df = pd.DataFrame(
            {
                'line':self.traced['line'],
                'event':self.traced['event'],
                **variables
            }
        )
        # print(df)
        print(self.variables)
        df.to_excel('trace_table_report.xlsx', index=False)

tracer = Tracer()
def start_trace():
    if tracer.debug:
        with open('trace_table_debug.txt', 'w') as f:
            f.flush()
    sys.tracebacklimit = 0
    sys.settrace(tracer.trace)

def end_trace():
    sys.settrace(None)
    tracer.report()

# def f():
#     x = [[10], [234]]
#     # print(df)
#     # print(jj)
#     # return 'df'
#     y = 20
#     x = 30
#     z = 50  
# start_trace()
# import pandas as pd
# f()
# end_trace()