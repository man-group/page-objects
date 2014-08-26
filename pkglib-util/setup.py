import os, sys
from setuptools import setup, Command, find_packages


classifiers = [
    'License :: OSI Approved :: MIT License',
    'Development Status :: 4 - Beta',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
    'Intended Audience :: Developers',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

long_description = "PkgLib common utilities"

trailing_args = []

class Test(Command):
    user_options = [('unit', None, 'Just run unit tests'),
                    ('integration', None, 'Just run integration tests'),
                    ]
    boolean_options = ['unit', 'integration']

    def initialize_options(self):
        self.unit = False
        self.integration = False

    def finalize_options(self):
        pass

    def run(self):
        self.distribution.fetch_build_eggs(self.distribution.tests_require)
        import subprocess
        import pytest
        tests = []
        if not (self.unit or self.integration):
            tests = ['tests']
        if self.unit:
            tests.append(os.path.join('tests', 'unit'))
        if self.integration:
            tests.append(os.path.join('tests', 'integration'))

        # Make sure to add any downloaded eggs to sys.path
        env = dict(os.environ)
        env['PYTHONPATH'] = os.pathsep.join(sys.path)
        errno = subprocess.call([sys.executable, pytest.__file__] + tests + trailing_args,
                                env=env)
        raise SystemExit(errno)


def main():
    # Gather trailing arguments for pytest, this can't be done using setuptools' api
    global trailing_args
    if 'test' in sys.argv:
        test_args = sys.argv[sys.argv.index('test') + 1:]
        for idx, arg in enumerate(test_args):
            if arg not in ('--unit', '--integration'):
                trailing_args = test_args[idx:]
                sys.argv = sys.argv[:-len(trailing_args)]
                break

    if sys.version_info.major < 3:
        tests_require.append('mock')

    setup(
        name='pkglib-util',
        description='PkgLib Utility Library',
        long_description=long_description,
        version='0.10.7',
        # url='',
        license='MIT license',
        platforms=['unix', 'linux'],
        author='Edward Easton',
        author_email='eeaston@gmail.com',
        classifiers=classifiers,
        install_requires=[],
        tests_require=['pytest'],
        packages=find_packages(),
        cmdclass={'test': Test},
    )

if __name__ == '__main__':
    main()
