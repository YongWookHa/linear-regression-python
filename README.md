## Overview

This is a python implementation of [Linear Regression](http://www.statisticssolutions.com/what-is-linear-regression/). This repository is based on [linear_regression_demo](https://github.com/llSourcell/linear_regression_demo). The original code doesn't actually implement all the fundamental codes. Of course, we can use libraries like sklearn to use linear regression. But I hope this codes help you study the basic principal of it.

## Dependencies

To use the `demo.py` which uses `sklearn`, you need to install it first. And `linear-regression.py` uses libraries for data-reading(`pandas`), data-processing(`numpy`) and visualizing(`matplotlib`). So you need to install three dependencies below.

* pandas
* numpy
* scikit-learn
* matplotlib

You can just run
`pip install -r requirements.txt` 
in terminal to install the necessary dependencies. Here is a link to [pip](https://pip.pypa.io/en/stable/installing/) if you don't already have it.

## Usage

Type `python demo.py` into terminal and you'll see the scatter plot and line of best fit appear.

And you can also type `python linear-regression.py` without using `sklearn` libraray. But you will see the same result of `demo.py`.

Enjoy the codes.
