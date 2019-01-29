#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostScope_ExitConan(base.BoostBaseConan):
    name = "boost_scope_exit"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_scope_exit"
    lib_short_names = ["scope_exit"]
    header_only_libs = ["scope_exit"]
    b2_requires = [
        "boost_config",
        "boost_function",
        "boost_preprocessor",
        "boost_type_traits",
        "boost_typeof"
    ]
