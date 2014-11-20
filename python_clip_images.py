"""
Load a nifti image, remove nans, clip the values between zero and 1000, write it to outfile

Required for the peak enhancement images 

Todo: 
    * call it with a zsh loop
"""
import os
import argparse
import nibabel as nib
import numpy as np


def python_clip_images(filename, vmin=0, vmax=None, outfilename=None):
    image = nib.load(filename)
    data = image.get_data()
    ndata = np.nan_to_num(data)
    if not vmax:
        vmax=np.percentile(ndata, 99)
    ndata=ndata.clip(vmin, vmax)
    print "Clipping to {} and {}".format(vmin, vmax)
    # needs generalization! the infile could be a different fileformat
    outimage = nib.Nifti1Image(ndata, image.get_affine())
    if not outfilename:
        outfilename = filename.replace('.nii', '_clip.nii')
    outimage.to_filename(outfilename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Input file to be clipped, as nifti")
    #parser.add_argument(
    #    "--outfile", "-o", help="Output filename (optional). Default is infile_clip.nii")
    parser.add_argument(
        "--vmin", type=float, help="Lower boundary of the clipped image")
    parser.add_argument(
        "--vmax", type=float, help="Upper boundary of the clipped image")

    args = parser.parse_args()
    vmin, vmax = (0, None)
    if args.vmin:
        vmin = args.vmin
    if args.vmax:
        vmax = args.vmax

    python_clip_images(
        #args.infile, vmin=vmin, vmax=vmax, outfilename=outfilename)
        args.infile, vmin=vmin, vmax=vmax)

    # todo: some testing is required
