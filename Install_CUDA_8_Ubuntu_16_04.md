## Install CUDA Toolkit 8.0 and cuDNN v6.0 on Ubuntu 16.04 64bit

Improved script inspired by: https://gist.github.com/mjdietzx/0ff77af5ae60622ce6ed8c4d9b419f45

#### FIRSTLY check for installed CUDA or NVIDIA drivers and remove them!
nvcc -V # check version of the CUDA Toolkit
nvidia-smi # check that nvidia driver is working
lsmod | grep nvidia # get loaded drivers

sudo apt-get autoremove --purge cuda-8-0 # try just `cuda`
rm -rf /usr/local/cuda-8.0/ # delete the folder if it still exists, change the version number of course
apt remove --purge nvidia* # remove drivers

#### install CUDA Toolkit v8.0:

instructions from https://developer.nvidia.com/cuda-downloads (linux -> x86_64 -> Ubuntu -> 16.04 -> deb (network))

```
CUDA_REPO_PKG="cuda-repo-ubuntu1604_8.0.61-1_amd64.deb"
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/${CUDA_REPO_PKG}
sudo dpkg -i ${CUDA_REPO_PKG}
sudo apt-get update
```

*Install CUDA Toolkit 8:*
`sudo apt-get -y install cuda-8-0`

*Install newest CUDA Toolkit:*
`sudo apt-get -y install cuda`


#### install cuDNN v6.0:

```
CUDNN_TAR_FILE="cudnn-8.0-linux-x64-v6.0.tgz"
wget http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/${CUDNN_TAR_FILE}
tar -xzvf ${CUDNN_TAR_FILE}
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-8.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-8.0/lib64/
sudo chmod a+r /usr/local/cuda-8.0/lib64/libcudnn*
```

#### set environment variables = add to the end of ~/.bashrc for permanent effect:

```
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```


#### Verify installation:

 - `nvcc -V` check version of the CUDA Toolkit
 - `nvidia-smi` check that driver is working

Test CUDA

```
cuda-install-samples-8.0.sh .
cd NVIDIA_CUDA-8.0_Samples/; make;
cd bin/x86_64/linux/release; ./deviceQuery;
```

#### Troubleshooting:

*nvidia-smi returns: NVML: Driver/library version mismatch*

Solution = reboot or:

https://stackoverflow.com/questions/43022843/nvidia-nvml-driver-library-version-mismatch

*Missing locale Warnings when connecting remotely*

`locale` # now set the (unset) members
`sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8`
