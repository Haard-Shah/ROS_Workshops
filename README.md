# ROS_Workshops

## Workshop 1
### Setup
ROS runs on a linux based environment you can therefore dual boot a non linux native system, run linux subsystem for windows or run Ubuntu in a virtual machine.  We will be running a ubuntu virtual machine to ensure all of us can follow along and to keep the development environemnt consistant. 

You can use <b>Virtual Box</b> by <i>Oracle</i> or <b>VMWare</b> we prefer virtualbox as its more user friendly however the below guide 


#### Vritual Box 

Virtual Box install: https://www.virtualbox.org/wiki/Downloads

Here is the link to the ubunutu guide. You will need to install the ubuntu virtual image available at: https://www.linuxvmimages.com/images/ubuntu-1804/ (Ensure you download the correct version, the virtual box image)

then follow this guide: https://www.linuxvmimages.com/how-to-use/how-to-import-vm-images-in-virtualbox/ it walks you through on how to install ubuntu on a virtual box. 

Minimum requirements: 
- Ram: >2GB 
- CPU Processor: >= 1 
- Disk space: >20 GB (Recommended)
- Password: `ubuntu`

Ensure when installing the ubuntu image the disk image is in the same directory as the root folder. 


If the above doesn't work here is a sepearte guide: https://brb.nci.nih.gov/seqtools/installUbuntu.html 

-----
This will be covered in the workshop but if you want to get ahead here are ROS installation guides. 

### ROS installation 
First we need to install al the dependencies and ROS itself, follow this guide to help install ROS and all its dependencies: http://wiki.ros.org/melodic/Installation/Ubuntu 

Next we need to download the catkin build tools. Note ROS comes with ros build tools but they are no longer supported and all the build tools have transitioned to catkin build tools. Guide: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment 