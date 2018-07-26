def canVisitAllRooms(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    room_size = len(rooms)
    result = {r:False for r in xrange(1, room_size)}
    result[0] = True
    idx_set = set([0])
    while True:
        copy_set = idx_set.copy()
        for i in copy_set:
            for k in rooms[i]:
                result[k] = True
                idx_set.add(k)
        if idx_set == copy_set:
            return all(result.values())

if __name__ == '__main__':
    print('[[1],[2],[3],[]]',canVisitAllRooms([[1],[2],[3],[]]))
    print('[[1,3],[3,0,1],[2],[0]]',canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
