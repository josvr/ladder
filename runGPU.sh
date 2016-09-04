#!/bin/bash

THEANO_FLAGS="cuda.root=/usr/local/cuda-7.5,mode=FAST_RUN,allow_gc=False,device=gpu0,force_device=True,floatX=float32,optimizer_excluding=low_memory" python2 run.py train --encoder-layers 5000-2048-1024-512-256-128-2 --batch-size 256 --decoder-spec gauss --denoising-cost-x 0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01 --lr 0.0001 --valid-set-size 200000 --labeled-samples 1000000 --unlabeled-samples 1000000 --seed 1 --dataset jos >> runGPU.log 2>&1
