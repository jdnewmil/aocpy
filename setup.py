from setuptools import setup

setup(
   name='aocpy',
   version='0.1',
   description='Some Advent of Code solutions',
   author='Jeff Newmiller',
   author_email='jdnewmil@dcn.davis.ca.us',
   packages=['aocpy'],  #same as name
   install_requires=['wheel', 'pandas', 'python>=3.11'], #external packages as dependencies
)
