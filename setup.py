from setuptools import setup, find_packages

setup(name='strategic-fruits-card-detection', version='0.1.0',
    description='A project for detecting strategic fruits cards using YOLOv8', author='MacMat01, SenseiBonsai2k',
    author_email='matteo.machella01@gmail.com, cristian.marinozzi1@gmail.com',
    url='https://github.com/MacMat01/strategic-fruits-card-detection', packages=find_packages(),
    install_requires=['opendatasets', 'ultralytics', 'opencv-python', 'pandas', 'seaborn', 'matplotlib', 'ipykernel',
        'torch', 'torchvision', 'torchaudio', 'imgaug', 'tqdm', 'requests'],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.12.3', ], )
