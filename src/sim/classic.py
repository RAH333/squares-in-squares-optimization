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
        if id >= 11: #
            break #
        xl = 0
        yl = 0
        hl = 0
        vc = 0
        if id == n*(n+1)/2:
            n = n + 1
        for square_id in range(n):
            if ln*ln < n <= ln*ln+(ln-1)*(ln-1) or n == 1:
                # xl = 0
                # yl = 0
                """
                if square_id % 2 != 0:
                    x = 0.5
                    y = 0.5
                    angle = 3.14/4 # 22/7/4
                    # angle = math.pi/4
                """
                # if 0 <= square_id < 2*ln-1:
                if hl*vc <= square_id < hl*vc + 2*ln-1: ## 
                ## if hl* <= square_id < 2*ln-1:
                    # if square_id % 2 != 0: 
                    ## if (hl + square_id) % 2 == 0:
                    if math.check(hl,vc): ##
                    # if square_id % 2 != 0:
                        x = xl + 0.3535533905932
                        y = yl + 
                        angle = 3.14/4 # 22/7/4
                        # angle = math.pi/4
                        xl = xl + 0.7071067811865
                        yl = yl + 
                    elif (hl + square_id) % 2 == 0:
                        # elif square_id % 2 == 0: 
                        # elif square_id % 2 == 0:
                        x = xl + 0.5
                        y = yl + 0.5
                        angle = 0
                        xl = xl + 1
                        yl = yl
                elif square_id == hl*vc + 2*ln-1:
                    hl = hl + 1
                    vc = 0
            elif ln*ln+(ln-1)*(ln-1) < n <= (ln+1)*(ln+1):
                x = xl + 0.5
                y = yl + 0.5
                angle = 0
                xl = xl + 1
                yl = yl
                # x = 0.5
                # y = 0.5
                # angle = 0
                if n == (ln+1)*(ln+1):
                    ln = ln+1
            # 6. Write the exact parameters for this specific step to the CSV
            writer.writerow([id, n, square_id, x, y, angle])
            id = id +1
            print(f"{id} no line Data value added successfully")
    print("Data successfully logged iteration-by-iteration!")
