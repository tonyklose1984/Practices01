#-*- coding:utf-8 -*-
__author__ = 'tony'
import fire

class Calculator(object):
    """A simple calculator class."""

    def double(self,number):
        return 2*number

    def add(self,A,B):
        return A+B

if __name__ == "__main__":
    fire.Fire(Calculator)

