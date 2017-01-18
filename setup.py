"""Setup file for data structures assignment."""


from setuptools import setup


setup(
    name="datastructures",
    description="python implementations",
    version=0.1,
    author="Regenal",
    author_email="regenal@mac.com",
    license="MIT",
    py_modules=['link_list',],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        # 'console_scripts': [
        #     "command = module_name:main",
        # ]
    }
)
