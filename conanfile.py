from conans import ConanFile, tools, os

class BoostScope_ExitConan(ConanFile):
    name = "Boost.Scope_Exit"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/scope_exit"
    description = "For a description of this library, please visit http://boost.org/scope_exit "
    license = "www.boost.org/users/license.html"
    lib_short_name = "scope_exit"

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = src=os.path.join(os.getcwd(), self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)
