## Required Python Libraries

### Qiling Framework
```
pip3 install qiling
```

### Unicorn Engine
```
pip install unicorn
```

### Capstone
```
pip install capstone
```


## Setup Test

After installing libraries run `cp_test.py`. It it works and you get the following output then proceed to the next section.
```
0x1000: mov     r0, #0x37
0x1004: sub     r1, r2, r3
```

If `incompatible architecture (have 'x86_64', need 'arm')` error or simlar error shows up when executing the python scipt try the following.

```
conda install -c conda-forge lxml
```

If the issue persists, kindly install an ubuntu virtual machine on your device and install the python libraries required for the lab on the VM

You can follow these video guides:

Windows     : https://www.youtube.com/watch?v=v1JVqd8M3Yc
macOS Intel : https://www.youtube.com/watch?v=Hzji7w882OY 
macOS M1/M2 : https://www.youtube.com/watch?v=1WWj6qoWhJw

## Initial setup


Download rootfs for the qiling framework

```
https://github.com/qilingframework/rootfs.git
```

Copy the pass binary to the `rootfs/arm_linux/bin` folder

