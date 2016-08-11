wget url_from_python2.7

tar -zxvf Python2.7.*.tgz

cd Python2.7.*

./configure --prefix=INSTALLPATH

make 

make install

cd $INSTALLPATH

echo $PATH

export PATH=INSTALL/bin:$PATH

export PYTHONPATH=/usr/lib/python2.7/dist-packages:$INSTALLPATH/lib/python2.7/site-packages

pip install packages --install-option="--prefix=$INSTALLPATH/lib/python2.7/site-packages" --ignore-installed 

or

easy_install -d $INSTALLPATH/lib/python2.7/site-packages "packages>version"
