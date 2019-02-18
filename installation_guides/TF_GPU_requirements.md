### Tensorflow CUDA and CuDNN requirements


| TF version | CUDA Toolkit required | CuDNN required |
| --- | --- | --- |
| 1.1 | 8.0 | v5.1 |
|1.2| 8.0 | v5.1|
|1.3| 8.0 | v6.0|
|1.4| 8.0 | v6.0|
|1.5| 9.0 | v7.0|
|1.6| 9.0 | v7.0|
|1.7| 9.0 | v7.0|

The exact version is required, if you have a different one, you must compile from source.

Source: https://www.tensorflow.org/versions/

**CUDA 9 known bug:**

```
Using XLA:GPU with CUDA 9 and CUDA 9.1 results in garbage results and/or
CUDA_ILLEGAL_ADDRESS failures.

Google discovered in mid-December 2017 that the PTX-to-SASS compiler in CUDA 9
and CUDA 9.1 sometimes does not properly compute the carry bit when
decomposing 64-bit address calculations with large offsets (e.g. load [x + large_constant]) into 32-bit arithmetic in SASS.

As a result, these versions of ptxas miscompile most XLA programs which use
more than 4GB of temp memory. This results in garbage results and/or
CUDA_ERROR_ILLEGAL_ADDRESS failures.

A fix in CUDA 9.1.121 is expected in late February 2018. We do not expect a
fix for CUDA 9.0.x. Until the fix is available, the only workaround is to
downgrade to CUDA 8.0.x
or disable XLA:GPU.
```

Source: https://github.com/tensorflow/tensorflow/releases/tag/v1.6.0

**Tensorboard in TensorFlow 1.6+**

```
NOTICE: TensorBoard 1.6.0+ has moved to the tensorboard package name on PyPI:
https://pypi.python.org/pypi/tensorboard. Only bugfix updates on 1.5.x will be
applied to the old package name (tensorflow-tensorboard). To upgrade to
TensorBoard 1.6.0+ we suggest you first pip uninstall tensorflow-tensorboard
before doing pip install tensorboard. See "Known Issues" below if you run into
problems using TensorBoard after upgrading.

The 1.6 minor series tracks TensorFlow 1.6.
```

Source: https://github.com/tensorflow/tensorboard/releases/tag/1.6.0

**OpenCV**

It should support CUDA 9 since v3.4.0 but I couldn't find it explicitly mentioned in release notes.

OpenCV v3.3.0 can be definitely patched to support CUDA 9, if you are in dire need. See these [instructions](https://github.com/BartyzalRadek/face-recognition)
 it's not that hard.
