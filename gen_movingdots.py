import random
from smile.scale import scale as s
# from config import *
# generate moving dots trials

"""Chuiwen's experimental version"""

"""
We will be creating dictionaries with the following keys:
    motion_props        The coherence, direction, speed, lifespan, direction_variance, speed_variance
    CR                  The correct answer which should be one of the allowed keys to press.
"""
dots_set = []
blocks = []
numblocks = 5
lenblocks = 4
Left_coh = [0, 0.1, 0.2, 0.3]
Right_coh = [0, 0.1, 0.2, 0.3] #2 layers of forloop
for y in range(numblocks):
    dots_set = []
    for x in range(lenblocks): # trials in each block
        for i in Left_coh:
            for j in Right_coh:
                if i > j:
                    CR = 'F' #allowed key left
                elif i<j:
                    CR = 'J' #allowed key right
                else:
                    continue
                    # CR = None #equal    
                motion_props = [{"coherence": i, "direction": 180, "speed":s(110), "lifespan":2/60},
                                {"coherence": j, "direction": 0, "speed":s(110), "lifespan":2/60},
                                {"coherence": 1-i-j, "direction": 0, "direction_variance":180,"speed":s(450), "speed_variance":s(100), "lifespan":2/60}]
                trial_dots = {'motion_props':motion_props,
                            'CR':CR,}
                dots_set.append(trial_dots)
    for repeat in range(2):
        for same in Left_coh:
            CR = None # equal
            motion_props = [{"coherence": same, "direction": 180, "speed":s(110), "lifespan":2/60},
                            {"coherence": same, "direction": 0, "speed":s(110), "lifespan":2/60},
                            {"coherence": 1-same*2, "direction": 0, "direction_variance":180,"speed":s(450), "speed_variance":s(100), "lifespan":2/60}]
            trial_dots = {'motion_props':motion_props,
                        'CR':CR,}
            dots_set.append(trial_dots)
    random.shuffle(dots_set)
    blocks.append(dots_set)

# random.shuffle(dots_set)
random.shuffle(blocks)

# for bb in blocks:
#     for dd in range(len(bb)):
#         bb[dd]['trial_num'] = (bb-1)*len(bb)+dd