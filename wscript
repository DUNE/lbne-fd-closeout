#!/usr/bin/env python

import os

top='.'

def configure(cfg):
    cfg.load('tex')
    pass


def build(bld):

    bld(features='tex',
        type='pdflatex',
        source = 'lbne-fd-closeout.tex',
        outs = 'pdf',
    )
    bld.install_files('${PREFIX}','lbne-fd-closeout.pdf')
    return


