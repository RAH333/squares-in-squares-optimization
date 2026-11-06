import csv
import os
import math

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
    n = 0
    ln = 0
    id = 0
    x = 0
    y = 0
    angle = 0
    while id < total_no_id:
        print(f"At start of while loop (id) = {id}")
        xl = 0
        yl = 0
        hl = 0
        vc = 0
        if id == n*(n+1)/2:
            n = n + 1
            print(f" After increament in the (n) = {n}")
        for square_id in range(n):
            print(f"At the start of (square id )= {square_id}")
            print(f"In the for loop (ln) = {ln}")
            if n == ((ln*ln)+1) and ln != 0 and n > 4:
                print(f"in the if statament ln = {ln}")
                if hl == 0 and vc == 1:
                    angle = math.pi/4
                else:
                    angle = 0
                if vc < ln :
                    print(f"In the (if vc < ln ) = {vc}")
                    if vc ==1:
                        print(f"In the (if vc == 1) = {vc}")
                        
                        if hl == 0:
                            x = xl + 0.3535533905932
                            y = yl + 1 + 0.3535533905932
                            print(f"In the (if hl == 0) x = {x}, y = {y}")
                            xl = xl + 0.7071067811865
                        elif hl != 0 :
                            x = xl + 0.5
                            y = yl + 0.5
                            xl = xl + 1
                            print(f"In the (if hl != 0) x = {x}, y = {y}")
                        print(f"In the (if vc == 1) end xl = {xl}")
                    elif vc !=1:
                        x = xl + 0.5
                        y = yl + 0.5
                        if vc == 0 and hl > 0 :
                            xl = xl + 1 + 0.7071067811865
                        else:
                            xl = xl + 1
                        print(f"In the (vc !=1) x = {x}, y = {y}, xl = {xl}")
                    vc = vc + 1
                    print(f"In the end of (if vc< ln) vc = {vc}")
                elif vc == ln:
                    ##
                    print(f"In the (if vc < ln ) = {vc}")
                    if vc ==1:
                        print(f"In the (if vc == 1) = {vc}")
                        if hl == 0:
                            x = xl + 0.3535533905932
                            y = yl + 1 + 0.3535533905932
                            print(f"In the (if hl == 0) x = {x}, y = {y}")
                        xl = xl + 0.7071067811865
                        print(f"In the (if vc == 1) end xl = {xl}")
                    elif vc !=1:
                        x = xl + 0.5
                        y = yl + 0.5
                        xl = xl + 1
                        print(f"In the (vc !=1) x = {x}, y = {y}, xl = {xl}")
                    print(f"In the end of (if vc< ln) vc = {vc}")
                    xl = 0
                    if hl == 0:
                        yl = yl + 1 + 0.7071067811865
                    elif hl != 0:
                        yl = yl + 1
                    hl = hl+1
                    vc = 0
            elif (n == (ln+1)*(ln+1)) or (n != (ln*ln)+1 and ln >1) or n < 5:
                print(f"in the elif statament ln = {ln}")
                angle = 0
                print(f"In the (1) x = {x}, y = {y}, xl = {xl}, yl = {yl}, hl = {hl} , vc = {vc} , ln = {ln}  ")
                x = xl + 0.5
                y = yl + 0.5
                xl = xl + 1
                print(f"In the (2) x = {x}, y = {y}, xl = {xl}, yl = {yl}, hl = {hl} , vc = {vc} , ln = {ln}  ")
                if vc < ln or vc == 0:
                    if ln !=0 :
                        vc = vc + 1
                    print(f"In the (3) x = {x}, y = {y}, xl = {xl}, yl = {yl}, hl = {hl} , vc = {vc} , ln = {ln}  ")
                elif vc == ln:
                    hl = hl+1
                    xl= 0
                    yl = yl + 1
                    vc = 0
                    print(f"In the (4) x = {x}, y = {y}, xl = {xl}, yl = {yl}, hl = {hl} , vc = {vc} , ln = {ln}  ")
                
                if n == (hl+1)*(vc+1) and hl == vc:
                        ln = ln+1
                print(f"In the (5) x = {x}, y = {y}, xl = {xl}, yl = {yl}, hl = {hl} , vc = {vc} , ln = {ln}  ")
                
            # 6. Write the exact parameters for this specific step to the CSV
            writer.writerow([id, n, square_id, x, y, angle])
            id = id +1
            print(f"{id} no line Data value added successfully")
    print("Data successfully logged iteration-by-iteration!")
