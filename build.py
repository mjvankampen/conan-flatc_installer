#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bincrafters import build_template_installer
from bincrafters import build_shared
from conans import tools


if __name__ == "__main__":
    arch = os.environ["ARCH"]
    builder = build_template_installer.get_builder(docker_entry_script=docker_entry_script)
    builder.add({"os" : build_shared.get_os(), "arch_build" : arch, "arch": arch}, {}, {}, {})
    builder.run()
