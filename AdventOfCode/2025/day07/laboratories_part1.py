""" Advent Of Code 2025: Day 07 Part 1 """
import sys
from tachyon_manifold import TachyonManifold

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        data = f.read().strip()
    
    tachyon_manifold = TachyonManifold(data)
    tachyon_manifold.start()

    print(f'Total splits: {tachyon_manifold.splits}')
