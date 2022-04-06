import tarfile

fname = "faster_rcnn_inception_v2_coco_2018_01_28.tar.gz"

if fname.endswith("tar.gz"):
    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()
elif fname.endswith("tar"):
    tar = tarfile.open(fname, "r:")
    tar.extractall()
    tar.close()

print("Extracted...")
