# -*- coding: utf-8 -*-
import os

import operator

from backend.helper import Helper
from backend.querier import Querier
from backend.simlifier import Simplifier
from processor import Processor

if __name__ == '__main__':
    rp = 'data/trajectory/raw_data/vehicle_gps_log_2015-04.txt'
    wd = 'data/trajectory/raw_trajectory'
    c = 'shanghai'
    c_range = {'lng': [119.5, 123.5], 'lat': [30.5, 32.5]}

    '''
    Trajectory processor
    '''
    p = Processor(rp, wd, c, c_range)
    # p.pre_extract()
    # p.trajectory_per_user()
    # p.simplification_per_user() # TODO the simplified rate could be better set for project
    # p.per_user2per_day()
    # p.construct_rtree()

    '''
    '''
    '''
    '''

    # points = Helper.file2points(
    #     '/Users/apple/Projects/PycharmProjects/search-trajectory-kBCT/backend/data/test_data/test.txt')
    # print points
    # query_points = Simplifier.dp_algorithm(points, 0, len(points) - 1, epsilon=1e-02)

    from time import time
    q = Querier(prepath='data/trajectory/sim_trajectory_per_day/shanghai/2015-04/01',
                rtreepath='data/rtree/shanghai/2015-04/01')
    t0 = time()
    query_points = [[121.359331, 31.184999], [121.360705, 31.287742], [121.406314, 31.227461], [121.50284, 31.294784]]
    a = q.iknn_algorithm(query_points, 7)
    t1 = time()
    print 'function takes %f' % (t1 - t0)
    for item in a:
        print item[0]
        print Helper.file2points('data/trajectory/sim_trajectory_per_day/shanghai/2015-04/01/%s' % item[0])
        print
