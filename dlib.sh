#!bin/bash

#INSTALL DLIB
cd .. #go to previous directory so that we would not have some pushes to git
sudo apt-get install build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev -y
sudo apt-get install python-dev python-pip python3-dev python3-pip -y
wget http://dlib.net/files/dlib-19.6.tar.bz2
tar xvf dlib-19.6.tar.bz2
cd dlib-19.6/
mkdir build
cd build
cmake ..
cmake --build . --config Release
sudo make install
sudo ldconfig
cd ..
pkg-config --libs --cflags dlib-1
python setup.py install
