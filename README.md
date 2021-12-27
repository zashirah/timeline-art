To set up Docker container:

cd into current folder

run `docker build -t selenium-image .`

On Mac: run `docker run --name selenium-container -v "$PWD:/app" -p 8888:8888 -itd selenium-image`

To execute the app.py:

run `docker exec -it selenium-container python app.py`


## Thoughts for next steps

- Gather data for all top 10 performers: 
  - G
  - MP
  - Wins
  - Pts
  - Rbs
  - Assists
  - Steals
  - Blocks
  - 3s
  - FG %
  - 2pt %
  - 3pt %
  - Rings
# timeline-art
