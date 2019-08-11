import os
from conans import ConanFile, CMake, tools


class ProtobufConan(ConanFile):
    name = "flatc_installer"
    version = "1.11.0"
    url = "https://github.com/bincrafters/conan-protoc_installer"
    homepage = "https://github.com/google/flatbuffers"
    topics = ("flatbuffers", "flatbuffers compiler", "serialization", "rpc")
    author = "markjan <>"
    description = ("flatc is a compiler for flatbuffers schema files. It can "
                   "generate among others C++, Java and Python code.")
    license = "BSD-3-Clause"
    exports = ["LICENSE.txt"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "compiler", "arch", "os_build", "arch_build"
    #short_paths = True
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        sha256 = "3f4a286642094f45b1b77228656fbd7ea123964f19502f9ecfd29933fd23a50b"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        os.rename("flatbuffers-%s" % self.version, self._source_subfolder)

    def requirements(self):
        self.requires.add("flatbuffers/{}@google/stable".format(self.version), private=True)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["FLATBUFFERS_BUILD_TESTS"] = False
        cmake.definitions["FLATBUFFERS_BUILD_FLATLIB"] = False
        cmake.definitions["FLATBUFFERS_BUILD_FLATHASH"] = False
        cmake.definitions["FLATBUFFERS_INSTALL"] = True
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*FlatBuffers*", dst="", src=os.path.join(self._source_subfolder,"CMake"))
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        del self.info.settings.compiler
        del self.info.settings.arch
        self.info.include_build_settings()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.FlatBuffers_ROOT = self.package_folder