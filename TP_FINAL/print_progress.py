# -*- coding: utf-8 -*-

from progressbar import ProgressBar
pbar = ProgressBar()
my_list = [1,2,3,4,5,6,7]
for x in pbar(my_list):
  print x
