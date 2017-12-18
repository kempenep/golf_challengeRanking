# golf_challengeRanking
Calculate challenge ranking of golf games, based on best of five

Requirements: 
- install Python
- comma separated values (default delimiter is ';') with scores of games. First row contains column names

usage: challenge.py [-h] [-indir INDIR] [-ext EXT] [-delimiter DELIMITER]
                    [-player PLAYER] [-score SCORE] [-output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -indir INDIR, --indir INDIR
                        Path of the input directory containing the csv files
  -ext EXT, --ext EXT   Extension of csv files
  -delimiter DELIMITER, --delimiter DELIMITER
                        Delimiter for colums
  -player PLAYER, --player PLAYER
                        Column name for player
  -score SCORE, --score SCORE
                        Column name for score
  -output OUTPUT, --output OUTPUT
                        Output filename with challenge ranking (leave empty to
                        print on screen)

Simple usage: copy challenge.py in directory with csv files and execute in that directory:
python challenge.py 
