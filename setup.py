from setuptools import setup

setup(
    name='robindata',
    version='0.1',
    py_modules=['robindata'],
    install_requires=[
        'Click',
        'robin_stocks'
    ],
    entry_points='''
        [console_scripts]
        robindata=robindata.cli:main
    '''

)
