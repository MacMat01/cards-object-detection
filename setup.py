from setuptools import setup, find_packages

setup(name='cards-object-detection', version='0.1.1-alpha', license='MIT',
      description='A project for detecting cards using YOLOv8', author='MacMat01, SenseiBonsai2k',
      author_email='matteo.machella01@gmail.com, cristian.marinozzi1@gmail.com',
      url='https://github.com/MacMat01/cards-object-detection', packages=find_packages(),
      install_requires=['opendatasets', 'ultralytics', 'opencv-python', 'pandas', 'seaborn', 'matplotlib', 'ipykernel',
                        'torch', 'torchvision', 'torchaudio', 'imgaug', 'tqdm', 'requests', 'pyzbar', 'influxdb-client',
                        'influxdb'], classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
                                                  'License :: OSI Approved :: MIT License',
                                                  'Programming Language :: Python :: 3.12.3', ], )
