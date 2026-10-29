import csv
import os

# 1. Define your file name and headers (parameter names)
csv_filename = "parameter_log.csv"
headers = ["id", "n", "square_id", "x", "y", "angle"]

# 2. Check if file exists to determine if we need to write the header
file_is_empty = not os.path.exists(csv_filename) or os.stat(csv_filename).st_size == 0

# 3. Open the file in append mode ('a')
# 'newline=""' is critical to prevent blank lines between rows on Windows platforms
with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # 4. Write the header only on the very first run/creation
    if file_is_empty:
        writer.writerow(headers)
no_of_puzzles = 1000
total_no_id = no_of_puzzles*(no_of_puzzles+1)/2
# n = 1
n = 0
ln = 0
id = 0
while id < total_no_id:
# for id in range(total_no_id):
  # for n in range(id):
  if id == n*(n+1)/2:
    n = n + 1
  if ln*ln < n <= ln*ln+(ln-1)*(ln-1):
    for square_id in range(n):
      xl = 0
      yl = 0
      if square_id % 2 != 0:
        x = 0.5
        y = 0.5
        angle = 3.14/4
  elif ln*ln+(ln-1)*(ln-1) < n <= (ln+1)*(ln+1):
    if 
    for square_id in range(n):
        x = 0.5
        y = 0.5
        angle = 0
  id = id +1
  # 6. Write the exact parameters for this specific step to the CSV
  writer.writerow([id, n, square_id, x, y, angle])

print("Data successfully logged iteration-by-iteration!")


  """
  for square_id in range(n):
    x = 0.5
    y = 0.5
    angle
  """
## if id == n*(n+1)/2:
    ## n = n + 1
  ## if n*n<= and <= n+(n-1)
# add value in csv file as next line
# id,n,square_id,x,y,angle;
