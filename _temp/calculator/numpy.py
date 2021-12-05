'''
 * @Process: complete
 * @Project_Name: module
 * @Package_Name: calculator
 * @Made_By: JS
 * @The_creation_time: --
 * @File_Name: numpy.py
 * @Version : Python 3.7.8
 * @contents: -
'''

import numpy as np
import pytest

print(np.array([1, 2, 3, 4]))


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


capital_case('Ebcdd')
