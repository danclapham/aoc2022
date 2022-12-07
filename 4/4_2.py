import time, os

start = time.time()
data_folder = os.path.dirname(__file__) + '/'
file_name = '4.txt'
f = open(data_folder + file_name)

def get_bounds(r):
    bounds = r.split('-')
    return (int(bounds[0]), int(bounds[1]))

def order_ranges(range1, range2):
    if range1[0] < range2[0]:
        return (range1, range2)
    if range1[0] > range2[0]:
        return (range2, range1)
    if range1[-1] > range2[-1]:
        return (range1, range2)
    return (range2, range1)

def do_ranges_overlap(range1, range2):
    if range2[0] <= range1[1]:
        return 1
    return 0

overlap_count = 0

for line in f:
    ranges = line.replace('\n','').split(',')
    bounds1 = get_bounds(ranges[0])
    bounds2 = get_bounds(ranges[1])

    ordered = order_ranges(bounds1, bounds2)
    overlap = do_ranges_overlap(ordered[0], ordered[1])

    overlap_count += overlap

print('\n{}'.format(overlap_count))

f.close()
print('\nCompleted in {:.5f}s'.format(time.time() - start))