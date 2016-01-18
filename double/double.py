#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int double(int);
""")

C = ffi.dlopen("target/release/libdouble.dylib")

print(C.double(9))
