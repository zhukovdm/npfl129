#!/usr/bin/bash

python3 linear_regression_features.py \
    --data_size=10 \
    --test_size=5  \
    --range=6

python3 linear_regression_features.py \
    --data_size=30 \
    --test_size=20  \
    --range=9

python3 linear_regression_features.py \
    --data_size=50 \
    --test_size=40  \
    --range=9