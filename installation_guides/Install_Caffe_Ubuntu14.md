### Installation of Caffe on Ubuntu 14

```
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install python-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```

Makefile config: http://caffe.berkeleyvision.org/installation.html#compilation

```
make all -j <number of threads>
make test
make runtest
```

```
make pycaffe
export PYTHONPATH=~/caffe/python/:$PYTHONPATH
```

```
python
import caffe 
```

### If errors appear - try:

```
sudo apt-get install python-matplotlib python-numpy python-pil python-scipy
sudo apt-get install build-essential cython
sudo apt-get install python-skimage

sudo pip install protobuf
```

### Usage

1. `cd caffe/memnet`
2. Edit `image dir name` in `score_images.py`
3. `python score_images.py`
