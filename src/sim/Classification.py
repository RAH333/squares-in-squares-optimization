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
    x = 0
    y = 0
    angle = 0
    # a = math.pi/4
    # sdvh = 0.5/math.sqrt(2)
    # s = 0.5*math.sqrt(2) 
    while id < total_no_id:
        # if id >= 11: #
            # break #
        xl = 0
        yl = 0
        hl = 0
        vc = 0
        if id == n*(n+1)/2:
            n = n + 1
        for square_id in range(n):
            if n == ln*ln+1:
                angle = 0
                if vc < ln:
                    # if vc ==1 and hl == 0:
                    if vc ==1:
                        if hl == 0:
                            x = xl + 0.3535533905932
                            y = yl + 1 + 0.3535533905932
                        xl = xl + 0.7071067811865
                    if vc !=1:
                        x = xl + 0.5
                        y = yl + 0.5
                        xl = xl + 1
                    vc = vc + 1
                elif vc == ln:
                    hl = hl+1
                    # vc = 0
                    xl= 0
                    if hl == 0:
                        yl = yl + 1 + 0.7071067811865
                    elif hl != 0:
                        yl = yl + 1
                    if n == (hl+1)*(vc+1):
                        ln = ln+1
                    vc = 0
            elif n == (ln+1)*(ln+1) or n != ln*ln+1:
                angle = 0
                if vc < ln:
                    x = xl + 0.5
                    y = yl + 0.5
                    xl = xl + 1
                    vc = vc + 1
                elif vc == ln:
                    hl = hl+1
                    # vc = 0
                    xl= 0
                    yl = yl + 1
                    if n == (hl+1)*(vc+1):
                        ln = ln+1
                    vc = 0
            # 6. Write the exact parameters for this specific step to the CSV
            writer.writerow([id, n, square_id, x, y, angle])
            id = id +1
            print(f"{id} no line Data value added successfully")
    print("Data successfully logged iteration-by-iteration!")
