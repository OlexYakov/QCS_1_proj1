from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file('temp', 'temp.py')
cfg.build_visual('exampleCFG', 'pdf',)
