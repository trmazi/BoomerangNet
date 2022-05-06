import os
import shutil
from setuptools import Command, setup

class CleanExtCommand(Command):
    description = 'Clean all compiled python extensions from the current directory.'

    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        print("Removing build directory...")
        shutil.rmtree(os.path.abspath("build/"), ignore_errors=True)
        for dirname, subdirList, fileList in os.walk(os.path.abspath(".")):
            for filename in fileList:
                if filename[-3:] == ".so":
                    fullname = os.path.join(dirname, filename)
                    print(f"Removing {fullname}")
                    os.remove(fullname)

setup(
    name='BoomerangNet',
    version='1.0',
    description="A 3rd party network for BeatcraftCyclon.",
    author='Trmazi (Trenton Zimmer)',
    license='Public Domain',
    packages=[
        # Core packages
        'boomerang',
        'boomerang.data',
        'boomerang.db',
        'boomerang.services',
        'boomerang.web',

        # Wrapper scripts, utilities and associated code.
        'boomerang.utils',

    ],
    install_requires=[
        req for req in open('requirements.txt').read().split('\n') if len(req) > 0
    ],
    cmdclass={
        'clean_ext': CleanExtCommand,
    },
    include_package_data=True,
    zip_safe=False,
)
