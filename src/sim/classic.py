no_of_puzzles = 1000
total_no_id = no_of_puzzles*(no_of_puzzles+1)/2
n = 1
for id in range(total_no_id):
  # for n in range(id):
  if id == n*(n+1)/2:
    n = n + 1
    for square_id in range(n):
      x = 0.5
      y = 0.5
      angle
