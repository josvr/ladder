#!/bin/bash

THEANO_FLAGS="cuda.root=/usr/local/cuda-7.5,mode=FAST_RUN,device=gpu,force_device=True,lib.cnmem=1.0,floatX=float32" python2 run.py train --encoder-layers 5000-2048-1024-512-256-128-2 --batch-size 256 --decoder-spec gauss --denoising-cost-x 0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01 --lr 0.0001 --valid-set-size 800000 --labeled-samples 3200000 --unlabeled-samples 3200000 --seed 1 --dataset jos
