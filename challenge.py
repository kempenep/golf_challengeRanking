# challenge.py: Python program to calculate challenge ranking of golf games
# Copyright (C) 2017 Pieter Kempeneers

# challenge.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# challenge.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with challenge.py.  If not, see <http://www.gnu.org/licenses/>.

import csv
import os
import heapq
from collections import defaultdict
import argparse

indir='.'
ext='csv'
player='Player'
score='Net Stable'
delimiter=';'
output=None

parser=argparse.ArgumentParser()
parser.add_argument("-indir","--indir",help="Path of the input directory containing the csv files",dest="indir",required=False,type=str,default=indir)
parser.add_argument("-ext","--ext",help="Extension of csv files",dest="ext",required=False,type=str,default=ext)
parser.add_argument("-delimiter","--delimiter",help="Delimiter for colums",dest="delimiter",required=False,type=str,default=delimiter)
parser.add_argument("-player","--player",help="Column name for player",dest="player",required=False,type=str,default=player)
parser.add_argument("-score","--score",help="Column name for score",dest="score",required=False,type=str,default=score)
parser.add_argument("-output","--output",help="Output filename with challenge ranking (leave empty to print on screen)",dest="output",required=False,type=str,default=output)

args = parser.parse_args()
indir=args.indir
ext=args.ext
delimiter=args.delimiter
player=args.player
score=args.score
output=args.output
    
netScores = defaultdict(list)
top5={}
    
for filename in os.listdir(indir):
    if filename.endswith(ext):
        with open(os.path.join(indir,filename), "r", encoding="ISO-8859-1") as csvfile:
            readCSV = csv.DictReader(csvfile,delimiter=delimiter)
            for row in readCSV:
                #print(row)
                if row[score]:
                    netScores[row[player]].append(int(row[score]))
        continue
    else:
        continue

for name in netScores:
    if len(netScores[name])>=3:
        #print(name,sum(netScores[name]))
        #totalScore[name]+=sum(netScores[name])
        top5[name]=sum(heapq.nlargest(5,netScores[name]))

top5_sorted=sorted(top5, key=top5.get,reverse=True)

if output:
    with open(output,"w") as outputf:
        for name in top5_sorted:
            #print(name,top5[name])    
            outputf.write("{},{}\n".format(name,top5[name]))
else:
    for name in top5_sorted:
        print(name,top5[name])
