#!/bin/bash

sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' &&
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 &&
sudo apt update &&
sudo apt install -y ros-melodic-desktop-full &&
sudo rosdep init &&
rosdep update &&
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc &&
source ~/.bashrc &&
sudo apt install -y python-rosinstall python-rosinstall-generator python-wstool build-essential &&
./ros_setup.sh