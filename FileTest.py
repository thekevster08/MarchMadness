import os
#import pkg_resources
from binaryTree import Node
#from binarytree import Node
# import matplotlib.pyplot as plt # for notebook usage
# import numpy as np # for notebook usage
import pandas as pd
#from pillow import Image, ImageDraw

from PIL import Image, ImageDraw

cwd = os.getcwd()

slot_coordinates = {
    2019: {1: (372, 32),# First four
         2: (372, 50),
         3: (30, 328),
         4: (30, 346),
         5: (695, 325),
         6: (695, 343),
         7: (370, 642),
         8: (370, 659),
         9:  (30, 532),# W1
         10: (30, 514),
         11: (30, 567),
         12: (30, 550),
         13: (30, 604),
         14: (30, 586),
         15: (30, 640),
         16: (30, 622),
         17: (30, 496),
         18: (30, 478),
         19: (30, 460),
         20: (30, 442),
         21: (30, 424),
         22: (30, 406),
         23: (30, 388),
         24: (30, 370),
         25: (30, 199),# X1
         26: (30, 182),
         27: (30, 236),
         28: (30, 218),
         29: (30, 272),
         30: (30, 254),
         31: (30, 308),
         32: (30, 290),
         33: (30, 164),
         34: (30, 146),
         35: (30, 128),
         36: (30, 110),
         37: (30, 92),
         38: (30, 74),
         39: (30, 55),
         40: (30, 38),
         41: (815, 532),# Y1
         42: (815, 514),
         43: (815, 567),
         44: (815, 550),
         45: (815, 604),
         46: (815, 586),
         47: (815, 640),
         48: (815, 622),
         49: (815, 496),
         50: (815, 478),
         51: (815, 460),
         52: (815, 442),
         53: (815, 424),
         54: (815, 406),
         55: (815, 388),
         56: (815, 370),
         57: (815, 199),# Z1
         58: (815, 182),
         59: (815, 236),
         60: (815, 218),
         61: (815, 272),
         62: (815, 254),
         63: (815, 308),
         64: (815, 290),
         65: (815, 164),
         66: (815, 146),
         67: (815, 128),
         68: (815, 110),
         69: (815, 92),
         70: (815, 74),
         71: (815, 55),
         72: (815, 38),
         73: (155, 523),# W2
         74: (155, 559),
         75: (155, 595),
         76: (155, 631),
         77: (155, 487),
         78: (155, 451),
         79: (155, 415),
         80: (155, 379),
         81: (155, 191),# X2
         82: (155, 227),
         83: (155, 263),
         84: (155, 299),
         85: (155, 155),
         86: (155, 119),
         87: (155, 83),
         88: (155, 47),
         89: (735, 523),# Y2
         90: (735, 559),
         91: (735, 595),
         92: (735, 631),
         93: (735, 487),
         94: (735, 451),
         95: (735, 415),
         96: (735, 379),
         97: (735, 191),# Z2
         98: (735, 227),
         99: (735, 263),
         100: (735, 299),
         101: (735, 155),
         102: (735, 119),
         103: (735, 83),
         104: (735, 47),
         105: (232, 541),# W3
         106: (232, 613),
         107: (232, 469),
         108: (232, 397),
         109: (232, 209),# X3
         110: (232, 281),
         111: (232, 137),
         112: (232, 65),
         113: (668, 541),# Y3
         114: (668, 613),
         115: (668, 469),
         116: (668, 397),
         117: (668, 209),# Z3
         118: (668, 281),
         119: (668, 137),
         120: (668, 65),
         121: (298, 576),# W4
         122: (298, 432),
         123: (298, 244),# X4
         124: (298, 100),
         125: (601, 576),# Y4
         126: (601, 432),
         127: (601, 244),# Z4
         128: (601, 100),
         129: (358, 504),# W5
         130: (358, 172),# X5
         131: (540, 504),# Y5
         132: (540, 172),# Z5
         133: (420, 457),# WX6
         134: (435, 219),# YZ6
         135: (435, 339)# CH
    }
}

class extNode(Node):
    def __init__(self, value, left=None, right=None, parent=None):
        Node.__init__(self, value, left=left, right=right)
        if parent is not None and isinstance(parent, extNode):
            self.__setattr__('parent', parent)
        else:
            self.__setattr__('parent', None)

    def __setattr__(self, name, value):
        # Magically set the parent to self when a child is created
        if (name in ['left', 'right']
                and value is not None
                and isinstance(value, extNode)):
            value.parent = self
        object.__setattr__(self, name, value)

def clean_col_names(df):
    return df.rename(columns={col: col.lower().replace('_', '') for col in df.columns})

def get_team_id(seedMap):
        return (seedMap, df[df['seed'] == seed_slot_map[seedMap]]['teamid'].values[0])

def get_team_ids_and_gid(slot1, slot2):
    team1 = get_team_id(slot1)
    team2 = get_team_id(slot2)
    if team2[1] < team1[1]:
        temp = team1
        team1 = team2
        team2 = temp
    gid = '{season}_{t1}_{t2}'.format(season=year, t1=team1[1], t2=team2[1])
    return team1, team2, gid

outputPath= cwd + '\\output.png'
teamsPath=cwd + '\\data\\Teams.csv'
seedsPath=cwd + '\\data\\2019TourneySeeds.csv'
slotsPath=cwd + '\\data\\MNCAATourneySlots.csv'
submissionPath=cwd + '\\submission.csv'
resultsPath=None
year=2019

submit = clean_col_names(pd.read_csv(submissionPath))

print(submit.head())


teams_df = clean_col_names(pd.read_csv(teamsPath))
seeds_df = clean_col_names(pd.read_csv(seedsPath))
slots_df = clean_col_names(pd.read_csv(slotsPath))

df = seeds_df.merge(teams_df, left_on='teamid', right_on='teamid')

df = df.drop(['firstd1season','lastd1season'], axis=1)

s = slots_df[slots_df['season'] == year]
seed_slot_map = {0: 'R6CH'}
bkt = extNode(0)


counter = 1
current_nodes = [bkt]
current_id = -1
current_index = 0

while current_nodes:
    next_nodes = []
    current_index = 0
    while current_index < len(current_nodes):
        node = current_nodes[current_index]
        if len(s[s['slot'] == seed_slot_map[node.value]].index) > 0:
            node.left = extNode(counter)
            node.right = extNode(counter + 1)
            seed_slot_map[counter] = s[s['slot'] == seed_slot_map[node.value]].values[0][2]
            seed_slot_map[counter + 1] = s[s['slot'] == seed_slot_map[node.value]].values[0][3]
            next_nodes.append(node.left)
            next_nodes.append(node.right)
            counter += 2
        current_index += 1
        current_id += 1
    current_nodes = next_nodes
    
# Solve bracket using predictions
# Also create a map with slot, seed, game_id, pred
    
results_df = pd.DataFrame({"id": [], "pred": []})
    
pred_map = {}
for level in list(reversed(bkt.levels)):
#     print(level)
    for ix, node in enumerate(level[0: len(level) // 2]):
#         print(node)
        team1, team2, gid = get_team_ids_and_gid(level[ix * 2].value, level[ix * 2 + 1].value)
        print(gid)
        pred = submit[submit['id'] == gid]['pred'].values[0]
        if gid in list(results_df.id):
            game_outcome = results_df[results_df[ID] == gid][PRED].values[0]
            team = team1 if game_outcome == 1 else team2
            if (game_outcome == 1 and pred > 0.5):
                # outcome agress with prediction, team1 wins
                pred_label = pred
            elif (game_outcome == 0 and pred > 0.5):
                # outcome different than prediction, team2 wins
                pred_label = 1 - pred
            elif (game_outcome == 0 and pred <= 0.5):
                # outcome agrees with prediction, team2 wins
                pred_label = 1 - pred
            elif (game_outcome == 1 and pred <= 0.5):
                # outcome different than prediction, team2 wins
                pred_label = pred
            else:
                raise ValueError("wat")

        elif pred >= 0.5:
            team = team1
            pred_label = pred
        else:
            team = team2
            pred_label = 1 - pred

        level[ix * 2].parent.value = team[0]
        pred_map[gid] = (team[0], seed_slot_map[team[0]], pred_label)
        
        
        
        
###################
slotdata = []
for ix, key in enumerate([b for a in bkt.levels for b in a]):
    xy = slot_coordinates[2019][max(slot_coordinates[2019].keys()) - ix]
    pred = ''
    gid = ''
    if key.parent is not None:
        team1, team2, gid = get_team_ids_and_gid(key.parent.left.value, key.parent.right.value)
    if gid != '' and pred_map[gid][1] == seed_slot_map[key.value]:
        pred = "{:.2f}%".format(pred_map[gid][2] * 100)
    st = '{seed} {team} {pred}'.format(
        seed=seed_slot_map[key.value],
        team=df[df['seed'] == seed_slot_map[key.value]]['teamname'].values[0],
        pred=pred
    )
    slotdata.append((xy, st))

# Create bracket image
# relevant:
# https://stackoverflow.com/questions/26649716/how-to-show-pil-image-in-ipython-notebook
#emptyBracketPath = pkg_resources.resource_filename(2017.jpg)
img = Image.open('2017.jpg')
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# draw.text((x, y),"Sample Text",(r,g,b))
for slot in slotdata:
    draw.text(slot[0], str(slot[1]), (0, 0, 0))

# dpi = 72
# margin = 0.05  # (5% of the width/height of the figure...)
# xpixels, ypixels = 940, 700

# Make a figure big enough to accomodate an axis of xpixels by ypixels
# as well as the ticklabels, etc...
# figsize = (1 + margin) * ypixels / dpi, (1 + margin) * xpixels / dpi
# fig = plt.figure(figsize=figsize, dpi=dpi)
# Make the axis the right size...
# ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])

# ax.imshow(np.asarray(img))
# plt.show() # for in notebook
img.save(outputPath)