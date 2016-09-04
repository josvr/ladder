#!/bin/bash

THEANO_FLAGS="cuda.root=/usr/local/cuda-7.5,mode=FAST_RUN,allow_gc=False,device=gpu0,force_device=True,floatX=float32,optimizer_excluding=low_memory" python2 run.py train --encoder-layers 5000-3000-1500-2 --batch-size 256 --decoder-spec gauss --denoising-cost-x 0.01,0.01,0.01,0.01,0.01 --lr 0.0001 --valid-set-size 200000 --labeled-samples 1000000 --unlabeled-samples 1000000 --save_to exp1 --seed 1 --dataset jos >> exp1.log 2>&1
