##
# Copyright (c) 2015-2016 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from setuptools import setup
from distutils.command.build import build
from setuptools.command.install import install


# pip imports setup.py prior to doing the actual build and install so it can
# determine dependency order of modules. The trouble is when it does that, cffi
# is not actually available, so we are not able to use the
# ffi.distutils_extension() call to build the extension module list. Instead
# what we have to do is override the L{Build} and L{Install} setup.py commands
# to lazily add the extension module list during execution of those commands
# only (i.e., not during the initial pip import).

def get_ext_modules():
    from osx import _corefoundation_cffi_build
    return [_corefoundation_cffi_build.ffi.distutils_extension()]


class LazyBuild(build):

    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        build.finalize_options(self)


class LazyInstall(install):

    def finalize_options(self):
        self.distribution.ext_modules = get_ext_modules()
        install.finalize_options(self)


setup(
    name="OSXFrameworks",
    version="0.1",
    description="cffi wrappers for OS X APIs",
    license="Apache 2.0",
    platforms=["any"],
    package_dir={'osx': 'osx'},
    packages=[
        'osx',
        'osx.frameworks',
    ],
    ext_package="osx",
    setup_requires=["cffi>=1.1.0"],
    install_requires=["cffi>=1.1.0"],
    cmdclass={
        "build": LazyBuild,
        "install": LazyInstall,
    }
)
