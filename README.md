# Linear-Regression by python implementation

## Overview

This is a python implementation of [Linear Regression](http://www.statisticssolutions.com/what-is-linear-regression/). This repository is based on [linear_regression_demo](https://github.com/llSourcell/linear_regression_demo). The original code doesn't actually implement all the fundamental codes. Of course, we can use libraries like sklearn to use linear regression. But I hope this codes help you study the basic principal of it.

## Dependencies

To use the `demo.py` which uses `sklearn`, you need to install it first. For visualization, you will need `matplotlib`. And `linear-regression.py` uses `numpy` libraries for data-processing. So you need to install three dependencies below.

* numpy
* scikit-learn
* matplotlib

You can just run `pip install -r requirements.txt` in terminal to install the necessary dependencies. Here is a link to [pip](https://pip.pypa.io/en/stable/installing/) if you don't already have it.

## Usage

Type `python demo.py` into terminal and you'll see the scattered data and best fit line. `demo.py` uses `sklearn` library for learning. 

If you want learn how the linear regression works, you'd better read the `linear-regression.py` which implement the model with `numpy`. There are three hyper parameters.

> epoch : The number times that the learning algorithm will work through the entire training dataset.<br/>
> learning rate : How much the weights would be updated.<br/>
> train data ratio : How much to use as learning data. The rest of it would be used for validating. 

I set default values for the hyper parameters, but I recommend you to edit them and observe the changes.

Because of `train data ratio`, there could be a little difference between `demo.py` and `linear-regression.py`.

Type `python linear-regression.py data_name.txt` into terminal.

#### for single attribute

In `fire_and_theft.txt`, you can find two columns of float data that indicate fire and theft occurrence in Chicago.

With `demo.py` and `fire_and_theft.txt`, you will get a plot below.

![](https://github.com/YongWookHa/linear-regression-python/blob/master/images/demo_graph.png?raw=true)

With `linear-regression.py` and `fire_and_theft.txt`, you will get plots below.

![](https://github.com/YongWookHa/linear-regression-python/blob/master/images/linear-regression_graph.png?raw=true)

![](https://github.com/YongWookHa/linear-regression-python/blob/master/images/linear-regression_cost.png?raw=true)

We are going to find out the relationship between fire and theft occurrence. Specifically, we will get a function of `y = w*x + b` which defines the relationship. In this case, you will get a single value of `w` and `b`.

> `w` stands for weight<br/>
> `b` stands for bias

If you are using single attribute input, it will make a graph image of scattered data and result function.

#### for multiple attribute

I tried to make the model be able to be applied even if there are multiple attributes.

In `pm2.5.txt`, you can find several columns. Attribute information is below. 

> month, day, hour is what it is.<br/>
> DEWP : Dew Point<br/>
> TEMP : Temperature<br/>
> PRES : Pressure<br/>
> lws : Cumulated wind speed<br/>
> lr : Cumulated hours of rain


We will say the number of attributes as `k`. With `pm2.5.txt`, `k` will be 8. Then, we'll try to figure out the formular of `y = w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + b`.

All `w`s are handled by a matrix. So don't be confused.

When you test `pm2.5.text` with linear regression, you will find that it's really hard to stabilize the model. It's because of the scale difference among the attributes. So you need to pre-process the data. 

`pm2.5_normalized.txt` is literally normalized data. You will get a better result with this data.

#### without display

If you are trying without display, you can run `without_display.py`. It will create image files of `graph.png` and `cost.png` so that you can check to result later.

Enjoy the codes.
