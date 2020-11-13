from setuptools import setup

from ldscore.common import __version__

setup(name='ldsc',
      version=__version__,
      description='LD Score Regression (LDSC)',
      url='http://github.com/vdtoorn/ldsc',
      author='Brendan Bulik-Sullivan and Hilary Finucane, converted to Python3 by Henk van den Toorn',
      author_email='',
      license='GPLv3',
      packages=['ldscore'],
      scripts=['ldsc.py', 'munge_sumstats.py'],
      install_requires = [
            'bitarray>=0.8',
            'nose>=1.3',
            'pybedtools>=0.7',
            'scipy>=0.18',
            'numpy>=1.16',
            'pandas>=0.20'
      ]
)
