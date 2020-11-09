
import h5py
filename = "file.hdf5"
p2= "C:/Users/Jo/Desktop/HCI-dataset-Copy/blender/papillon/feature_gt_depth_probabilities.h5"
with h5py.File(p2, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])