"""
Load a nifti image, remove nans, clip the values between zero and 1000, write it to outfile

Required for the peak enhancement images 

Todo: 

    * check argparse: how do we get a filename from the commandline
    * wcall it with a zsh loop
"""
import os
import nibabel as nib
import numpy as np


def python_clip_images(vmin=0, vmax=2000):
    image = nib.load(filename)
    data = image.get_data()
    ndata = np.nan_to_num(data)
    ndata.clip(vmin, vmax)
    outimage = nib.Nifti1Image(ndata, image.get_affine())
    outfilename = filename.replace('.nii', '_clip.nii')
    outimage.to_filename(outfilename)

if __name__=="__main__":
    # get the filename from the command line
    # possibly get the clipping values from the cli
    # call the function with these parameters

