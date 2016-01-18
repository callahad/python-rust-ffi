#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cffi import FFI

ffi = FFI()
ffi.cdef("""
    int calculate(const char *script);
""")
C = ffi.dlopen("target/release/libcalc.dylib")

def main():
    result = C.calculate(b"+ * * + * - /")
    print(result)

if __name__ == '__main__':
    main()

