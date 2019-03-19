## Overview

This is a python implementation of [Linear Regression](http://www.statisticssolutions.com/what-is-linear-regression/). This repository is based on [linear_regression_demo](https://github.com/llSourcell/linear_regression_demo). The original code doesn't actually implement all the fundamental codes. Of course, we can use libraries like sklearn to use linear regression. But I hope this codes help you study the basic principal of it.

## Dependencies

To use the `demo.py` which uses `sklearn`, you need to install it first. And `linear-regression.py` uses libraries for data-processing(`numpy`) and visualizing(`matplotlib`). So you need to install three dependencies below.

* numpy
* scikit-learn
* matplotlib

You can just run
`pip install -r requirements.txt` 
in terminal to install the necessary dependencies. Here is a link to [pip](https://pip.pypa.io/en/stable/installing/) if you don't already have it.

## Usage

In `fire_and_theft.txt`, you can find two columns of float data that indicate fire and theft occurrence in Chicago.

We are going to find out the relationship between fire and theft occurrence. Specifically, we will get a function of `y = w*x + b` which defines the relationship.

I tried to make the model be able to be applied even if there are multiple `x`s.

Type `python demo.py` into terminal and you'll see the scatter plot and line of best fit appear.

And you can also type `python linear-regression.py` without using `sklearn` libraray. But you will see the same result of `demo.py`.

If you are trying without display, you can run `without_display.py`. It will create image files of `graph.png` and `cost.png` so that you can check to result later.

Enjoy the codes.
