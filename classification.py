#!/usr/bin/python

# polistream
__author__ = "Markus Gildenhard"
__copyright__ = "Copyright 2017, Markus Gildenhard"
__credits__ = ["Markus Gildenhard"]
__license__ = ("MIT License as detailed in License File"
                " provided with this software")
__maintainer__ = "Markus Gildenhard"
__email__ = "mgdatascience@posteo.de"
__status__ = "Development"
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')