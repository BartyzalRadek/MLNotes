### Installation of Tensorflow with GPU support

https://www.tensorflow.org/versions/r1.3/install/install_windows


1. Install Visual Studio 2013 - https://my.visualstudio.com/downloads 
2. Install CUDA Toolkit without the drivers (you probably have newer ones) http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/ 
3. Open `C:\ProgramData\NVIDIA Corporation\CUDA Samples\v8.0\1_Utilities\deviceQuery\deviceQuery_vs2013.sln`
4. In Visual Studio: set to `Release`
5. Build the program
6. Also build the `bandwidthTest` the same way (located in `1_Utilities` )
7. Run in CMD: 
```
cd C:\ProgramData\NVIDIA Corporation\CUDA Samples\v8.0\bin\win64\Release
deviceQuery.exe
```
![Output of deviceQuery.exe](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/graphics/valid-results-from-sample-cuda-devicequery-program.png)

```
bandwidthTest.exe
```
![Image of Yaktocat](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/graphics/valid-results-from-sample-cuda-bandwidthtest-program.png)

If the outputs look similar to the images, good job.

8. Download and Extract CuDNN -> you will get `cuda` folder with 3 sub folders
9. Put `cudnn.lib`, `cudnn.h` and `cudnn64_5.dll` into the root of the extracted folder = into the `cuda` folder
10. Add the `cuda` folder into PATH variable via `Edit the System environment variables`
11. start anaconda prompt:
```
conda create -n tensorflow_gpu python=3.5
activate tensorflow_gpu
pip install --upgrade tensorflow-gpu
```

12. Check if TF works:
```
python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
```

