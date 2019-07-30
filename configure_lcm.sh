export LCM_INSTALL_DIR=/usr/local/lib
echo 'sudo echo $LCM_INSTALL_DIR > /etc/ld.so.conf.d/lcm.conf'
export PYTHON_VERSION=$(python -c "import sys; print(\"%s.%s\" % sys.version_info[:2])")
export PYTHON_USER_SITE=$(python -m site --user-site)
echo 'echo "$LCM_INSTALL_DIR/python$PYTHON_VERSION/site-packages" > /usr/lib/python3.7/site-packages/lcm.pth'
