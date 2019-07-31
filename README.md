# LCM-vs-CANBus

## This repository serves the purpose of comparing the [Lightweight Communications Marshalling](https://github.com/lcm-proj/lcm) (LCM) communications infrastructure vs CAN Bus

### Installation Instructions
Before starting anything, run the following commands

```
git submodule init
git submodule update
```
### Installation Instructions - LCM
#### This is for linux (I run Arch, it should work on Ubuntu/Debian also. For Mac, windows, or others, check the documentation [here](https://github.com/lcm-proj/lcm/blob/master/docs/content/build-instructions.md)

Before getting started, make sure the LCM repository is checked out to `v1.4.0` (it should already be)
To check this, run `git branch` -> you should see something like `(HEAD detached at v1.4.0)`
If not, run `git checkout v1.4.0`

The following packages are required:
- build-essential
- libglib2.0-dev

The following packages are strongly recommended:
- default-jdk (or openjdk-9-jdk)
- python-dev

Run the following commands

```
cd lcm
mkdir build
cd build
cmake ..
make
sudo make install
```
Finally, run the following ... (This is for Arch, I am not 100% sure you need to do this for Arch/Debian. Check the [link](https://github.com/lcm-proj/lcm/blob/master/docs/content/build-instructions.md))
```
export LCM_INSTALL_DIR=/usr/local/lib
sudo echo 'sudo echo $LCM_INSTALL_DIR > /etc/ld.so.conf.d/lcm.conf
export PYTHON_VERSION=$(python -c "import sys; print(\"%s.%s\" % sys.version_info[:2])")
export PYTHON_USER_SITE=$(python -m site --user-site)
sudo echo "$LCM_INSTALL_DIR/python$PYTHON_VERSION/site-packages" > /usr/lib/python$PYTHON_VERSION/site-packages/lcm.pth
```

* note, I use `pyenv` to control python versions on my system, so I also added the `site-packages` location for my `python 3.7.3` installation to `/usr/lib/python$PYTHON_VERSION/site-packages/lcm  .pth`

Additionally, you may need to configure pkgconfig to find lcm.pc
`export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:$LCM_LIBRARY_DIR/pkgconfig`

### Installation Instructions - CANBus


### Testing Instructions
First, setup the python environment
To do so, it's best practice to maybe create a virtual environment
`python -m venv venv`
To activate it... `. ./venv/bin/activate` -> If you use some other virtual environment tool, go ahead and use that one

Now, in the directory with the `setup.py` file, run `pip install -e .`
The package should now be `pip` install-able

LCM message types are created by first defining a `*message*.lcm` file that follows the format define [here](https://lcm-proj.github.io/type_specification.html)

To generate the proper bindings for python, run `lcm-gen -p test_message.lcm` as defined [here](https://lcm-proj.github.io/tut_lcmgen.html)

Then, to run the lcm test, just run `python -m lcm_vs_canbus.lcm_send_and_receive` and watch the output!
