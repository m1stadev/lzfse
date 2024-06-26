# this file is part of pyliblzfse.
#
# Copyright (c) 2017-2020  Yogesh Khatri
# Copyright (c) 2016, 2017 Dima Krasner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from pathlib import Path

from setuptools import Extension, setup

lzfse_src_path = Path('lzfse/src')
lzfse_src = [
    *[str(f) for f in lzfse_src_path.glob('*.c') if f != 'lzfse/src/lzfse_main.c'],
    'pylzfse.c'
]

setup(
    ext_modules=[
            Extension(
                  'lzfse',
                  sources=lzfse_src,
                  include_dirs=[str(lzfse_src_path)],
            )
    ]
)