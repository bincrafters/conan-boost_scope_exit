#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostScope_ExitConan(base.BoostBaseConan):
    name = "boost_scope_exit"
    url = "https://github.com/bincrafters/conan-boost_scope_exit"
    lib_short_names = ["scope_exit"]
    header_only_libs = ["scope_exit"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_mpl",
        "boost_preprocessor",
        "boost_type_traits",
        "boost_typeof"
    ]


