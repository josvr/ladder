#!/bin/bash

THEANO_FLAGS="cuda.root=/usr/local/cuda-7.5,mode=FAST_RUN,device=gpu,force_device=True,lib.cnmem=1.0,floatX=float32" python2 ./run.py evaluate results/noname0
