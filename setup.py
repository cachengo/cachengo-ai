from setuptools import setup, find_packages

setup(
    name='cachengoai',
    version='0.1.0',
    description='Tools for running AI workloads on Cachengo symbiotes',
    author='Brad Churchwell',
    author_email='brad@cachengo.com',
    url='https://github.com/cachengo/cachengo-ai',
    packages=find_packages(),
    package_data={'': ['yolov5s-640-640.rknn']},
    include_package_data=True,
    install_requires=[
        'ffmpeg-python==0.2.0',
        'numpy==1.24.1',
        'opencv-python==4.7.0.68',
        # 'rknn-toolkit-lite2==2.3.0'
        ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
