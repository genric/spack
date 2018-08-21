# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cubew(AutotoolsPackage):
    """Component of CubeBundle: High performance C Writer library """

    homepage = "http://www.scalasca.org/software/cube-4.x/download.html"
    url = "http://apps.fz-juelich.de/scalasca/releases/cube/4.4/dist/cubew-4.4.tar.gz"

    version('4.4.1', 'c09e3f5a3533ebedee2cc7dfaacd7bac4680c14c3fa540669466583a23f04b67')
    version('4.4',   'e9beb140719c2ad3d971e1efb99e0916')

    depends_on('zlib')

    def url_for_version(self, version):
        filename = 'cubew-{0}.tar.gz'.format(version)

        return 'http://apps.fz-juelich.de/scalasca/releases/cube/{0}/dist/{1}'.format(version.up_to(2), filename)

    def url_for_version(self, version):
        url = 'http://apps.fz-juelich.de/scalasca/releases/cube/{0}/dist/cubew-{1}.tar.gz'

        return url.format(version.up_to(2), version)

    def configure_args(self):
        spec = self.spec

        configure_args = ['--enable-shared']

        if spec.satisfies('%intel'):
            configure_args.append('--with-nocross-compiler-suite=intel')
        elif spec.satisfies('%pgi'):
            configure_args.append('--with-nocross-compiler-suite=pgi')
        elif spec.satisfies('%clang'):
            configure_args.append('--with-nocross-compiler-suite=clang')

        return configure_args

    def install(self, spec, prefix):
        make('install', parallel=True)
