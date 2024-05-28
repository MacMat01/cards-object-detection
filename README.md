# Strategic Fruits Card Detection

This project aims to detect strategic fruits cards using YOLOv8. It is implemented in Python and uses several libraries
for data processing and model training.

## Project Structure

The project has the following structure:

- `src/main/python/model_training/strategic-fruits-card-detection-dataset/`: Contains the dataset used for training the
  model.
- `environment.yml`: Contains the conda environment configuration.
- `setup.py`: Contains the setup configuration for the Python package.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.12.3
- Conda package manager
- Cuda Toolkit 11.1 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MacMat01/strategic-fruits-card-detection.git
```

1. Navigate to the project directory:

```bash
cd strategic-fruits-card-detection
```

2. Create a new conda environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
```

3. Activate the conda environment:

```bash
conda activate strategic-fruits-card-detection
```

4. Install the Python package:

```bash
python setup.py install
```

5. If gpu isn't working for model training, install pytorch-cuda manually (remember to restart pc, it often works):

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

### Running the Application

To run the main application, navigate to the `src/main/python/app` directory and run the 'app.py' script:

```bash
cd src/main/python/app
```

```bash
python app.py
```

### Usage

You can use the Jupyter Notebook for interactive data exploration and model training. Ensure you have Jupyter installed
in your environment, and start it with:

```bash
jupyter notebook
```

Navigate to the `notebooks` directory and open the `strategic-fruits-card-detection.ipynb` notebook.

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.
