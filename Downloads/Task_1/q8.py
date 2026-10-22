import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def distance_origin(row):
    x=float(row["x"])
    y=float(row["y"])
    return (x**2 + y**2)**0.5
def des_reference(blue_cone,yellow_cone):
    bx,by = float(blue_cone["x"]), float(blue_cone["y"])
    yx,yy = float(yellow_cone["x"]), float(yellow_cone["y"])
    return ((bx-yx)**2 + (by-yy)**2)**0.5
blue_cone = []
yellow_cone = []
with open("cone.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["color"] == "blue":
            blue_cone.append(row)
        elif row["color"] == "yellow":
            yellow_cone.append(row)
blue_cone.sort(key=distance_origin)
yellow_cone.sort(key=distance_origin)
header=["cone_id","x","y","color"]
with open("blue_cone.csv","w",newline="") as f_blue:
    bwriter = csv.DictWriter(f_blue,fieldnames=header)
    bwriter.writeheader()
    bwriter.writerows(blue_cone)
with open("yellow_cone.csv","w",newline="") as f_yellow:
    ywriter = csv.DictWriter(f_yellow,fieldnames=header)
    ywriter.writeheader()
    ywriter.writerows(yellow_cone)
centreline=[]
for blue in blue_cone:
    nearest_yellow = min(yellow_cone, key=lambda yellow: des_reference(blue,yellow))
    bx, by = float(blue["x"]), float(blue["y"])
    yx, yy = float(nearest_yellow["x"]), float(nearest_yellow["y"])
    centreline.append({
        "blue_cone": blue["cone_id"],
        "yellow_cone": nearest_yellow["cone_id"],
        "x": (bx + yx) / 2,
        "y": (by + yy) / 2
})
with open("centreline.csv","w",newline="") as f_centreline:
    header2 = ["blue_cone","yellow_cone","x","y"]
    centreline_writer = csv.DictWriter(f_centreline,fieldnames=header2)
    centreline_writer.writeheader()
    centreline_writer.writerows(centreline)