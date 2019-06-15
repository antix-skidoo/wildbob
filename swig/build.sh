# how to build
swig -python -c++ wildbob_common.i 
g++ -c wildbob_common_wrap.cxx -I/usr/include/python2.4 -I/usr/include/apt-pkg/ -I../common -I../
g++ -shared wildbob_common_wrap.o -o _wildbob_common.so ../common/libwildbob.a -lapt-pkg 
