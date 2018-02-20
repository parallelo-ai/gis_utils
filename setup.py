from setuptools import setup
from setuptools.command.install import install
import subprocess

class NPMInstall(install):
    """
    NPMInstall installs the packages in `package.json`
    which are `topojson-client` and `topojson-server`
    used to convert between geojson and topojson
    """
    def run(self):
        print("Installing NodeJS prerequisites")
        st,r = subprocess.getstatusoutput("npm")
        if st == 1:
            # It is expected to have npm installed
            subprocess.run(["npm","install"])
            # subprocess.run(["npm","--global","install"])
        else:
            print("You have to install package.json manually")
        install.run(self)

setup(name='gis_utils',
      cmdclass={
          'install' : NPMInstall,
      },
      version='0.0.1',
      description='Convert between Shapefile, GeoJSON and TopoJSON',
      url='https://github.com/Daniel-M/gis_utils',
      author='Daniel-M',
      author_email='danielmejia55@gmail.com',
      license='MIT',
      packages=['gis_utils'],
      install_requires=[
          'pyshp',
          'geojson'
      ],
      python_requires='>=3',
      zip_safe=False)
