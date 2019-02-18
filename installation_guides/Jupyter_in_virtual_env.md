## Use virtual environment kernel inside Jupyter notebook

### Windows

1. activate environment 

2. `pip3 install jupyter`

3. `ipython kernelspec install-self --user` 
This will create a kernelspec for your virtualenv and tell you where it is:
[InstallNativeKernelSpec] Installed kernelspec python3 in C:\Users\admin\AppData\Roaming\jupyter\kernels\python3 

4. Go to: `C:\Users\admin\AppData\Roaming\jupyter\kernels\python3`

5. Change the name of the directory `<pythonX>` to your own `<kernel_name>`

6. Go inside `<kernel_name>/kernel.json` and change `'display_name'` to `<kernel_name>`
It should look like this:
{
 "argv": [
  "c:\\users\\admin\\envs\\tensorflow-0.12\\scripts\\python.exe",
  "-m",
  "ipykernel",
  "-f",
  "{connection_file}"
 ],
 "language": "python",
 "display_name": `"<kernel_name>"`
}

7. Check that the `python.exe` is the one used in virtualenv:
```
 import os
 import sys
 os.path.dirname(sys.executable)
 ```
 
 ### Ubuntu
 1. `source <ENV_NAME>/bin/activate`
 2. `pip3 install ipykernel`
 3. python3 -m ipykernel install --user --name <ENV_NAME> --display-name "<DISPLAYED NAME IN JUPYTER KERNEL SELECTION>"
    
    e.g.: `python3 -m ipykernel install --user --name tensorflow --display-name "TF_1.3_Python3"`
 4. deactivate
 
 Now you can run `jupyter notebook` without activating any environment and it will have the kernel in its dropdown menu under `New`.

 ### Adding Python 2(3) kernel
 If you’re running Jupyter on Python 3, you can set up a Python 2 kernel like this:

 1. python2 -m pip install ipykernel
 2. python2 -m ipykernel install --user
 
 Or just change 2 to 3 if you need the other way around.
 
 
