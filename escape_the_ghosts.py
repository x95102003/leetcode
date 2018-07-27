#!/usr/bin/env python
# -*- coding: utf-8 -*-

def escapeGhosts(ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # Just compare distance between ghost and target
        dist = abs(target[0]) + abs(target[1])
        for g in ghosts:
            g_dist = abs(target[0] - g[0]) + abs(target[1] - g[1])
            if dist >= g_dist:
                return False
        return True
if __name__ == '__main__':
    print(escapeGhosts([[2,0]],[1,0]))
