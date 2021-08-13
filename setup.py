from setuptools import setup, find_packages
import re

requirements = []
with open('requirements.txt',"r",encoding="utf-8") as f:
  requirements = f.read().splitlines()

version = '0.1.0'
readme = ''
with open('README.rst',"r",encoding="utf-8") as f:
    readme = f.read()

extras_require = {
    'docs': [
        'sphinx==4.0.2',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-napoleon',
        'sphinxcontrib-websupport',
    ],
    'speed': [
        'orjson>=3.5.4',
    ]
}

setup(name='pycarbonsh',
      author='Pranav Saxena',
      url='https://github.com/Pranav-Saxena/PyCarbonSh',
      project_urls={
        "Documentation": "https://pycarbonsh.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Pranav-Saxena/PyCarbonSh/issues",
      },
      version=version,
      packages=find_packages(),
      license='MIT',
      description='The Asynchronous web-scraper for carbon.now.sh which helps to create and share beautiful pics of your code!',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)