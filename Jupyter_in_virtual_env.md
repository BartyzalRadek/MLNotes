### Use virtual environment kernel inside Jupyter notebook
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
