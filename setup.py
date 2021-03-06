from setuptools import setup

setup(
    name='app_creditcard',
    packages=['app_creditcard'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)