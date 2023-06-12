"""
https://leetcode.com/problems/snapshot-array/

1146. Snapshot Array
Medium
Accepted
31 minutes !
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.data = [{0: 0} for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        pack = self.data[index]
        if pack.get(self.snap_id) is not None:
            pack[self.snap_id] = val
        else:
            pack[self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pack = self.data[index]
        # print(f"get in pack = {pack}")
        while True:
            if pack.get(snap_id) is not None:
                return pack[snap_id]
            else:
                snap_id -= 1

    def print(self):
        for el in self.data:
            print(el)


if __name__ == '__main__':
    array = SnapshotArray(5)
    array.set(1, 10)
    array.set(1, 20)
    array.snap()
    print(array.get(1, 1))
    array.print()
