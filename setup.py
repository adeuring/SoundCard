from setuptools import setup

setup(
    name='SoundCard',
    version='0.4.2',
    description='Play and record audio without resorting to CPython extensions',
    author='Bastian Bechtold',
    url='https://github.com/bastibe/SoundCard',
    license='BSD 3-clause',
    packages=['soundcard', 'soundcard.__pyinstaller'],
    package_data={'soundcard': ['*.py.h']},
    install_requires=['numpy', 'cffi'],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
    long_description=open('README.rst').read(),
    entry_points={
        "pyinstaller40": [
            "hook-dirs = soundcard.__pyinstaller:get_hook_dirs",
            "tests = soundcard.__pyinstaller:get_test_dirs",
        ],
    },
)
