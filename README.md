# Social-Distancing-Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This programme is intended to check for social distancing among pedestrians

## For using your own Custom Dataset:


Clone https://github.com/tzutalin/labelImg

Prerequisites for this

    conda install pyqt=5
    pyrcc5 -o resources.py resources.qrc
    Transfer resources.py and resources.qrc into the resources folder

Execute using python labelImg.py

## For using the Caltech dataset:

Download dataset from : http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/

Create a directory structure in the format
--

    startdt_data
      caltech_pedestrian_dataset
        annotations
        set01
        .
        .
          <contains all the .vbb files>
      set01
      .
      .
      .
        <contains all the .seq files>

run python vbb2voc.py

The above code generated xml files in startdt_data\caltech_pedestrian_dataset\annotations\set01 and extracts the jpeg images from .seq and pastes them into /caltech_pedestrian_dataset/set01/frame

I've saved in XML filetype.

Switch to tools folder
--

Execute XML_to_YOLOv3.py
--

This Creates 3 text files under the Text_Files folder

Change necessary configurations by setting up configs.py

Run train.py  

Check the graphs using : tensorboard --logdir=log
