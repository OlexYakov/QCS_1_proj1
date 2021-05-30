from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file('will', 'will.py')
cfg.build_visual('will_cfg', 'pdf',)
