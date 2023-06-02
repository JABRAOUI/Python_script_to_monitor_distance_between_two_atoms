import numpy as np
import matplotlib.pyplot as plt
import sys,os,string


if len(sys.argv) != 4:
  print ("Syntax: python script inputFile atom1_idx atom2_idx")
  sys.exit()



inFileName = sys.argv[1]

atom1_idx = float(sys.argv[2])
atom2_idx = float(sys.argv[3])

inFile = open(inFileName, "r")
lines = inFile.readlines()
inFile.close()

# Extract the number of atoms and the number of frames from the first line
num_atoms = int(lines[0])
num_frames = len(lines[1:]) // (num_atoms + 2)

# Extract the atomic coordinates for each frame
coords = []
for i in range(num_frames):
    start_idx = i * (num_atoms + 2) + 2
    end_idx = start_idx + num_atoms
    frame_coords = []
    for line in lines[start_idx:end_idx]:
        frame_coords.append([float(x) for x in line.split()[1:]])
    coords.append(frame_coords)

# Calculate the distance between the two atoms for each frame
distances = []
for frame_coords in coords:
    distance = np.linalg.norm(np.array(frame_coords[int(atom1_idx)]) - np.array(frame_coords[int(atom2_idx)]))
    distances.append(distance)

# Save the distance data to a text file
np.savetxt('distances.txt', distances)

# Plot the distance vs the frame number
plt.plot(range(num_frames), distances)
plt.xlabel('Frame')
plt.ylabel('Distance')
plt.show()

