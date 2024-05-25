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

### Usage

You can use the Jupyter Notebook for interactive data exploration and model training. Ensure you have Jupyter installed
in your environment, and start it with:

```bash
jupyter notebook
```

Navigate to the `notebooks` directory and open the `strategic-fruits-card-detection.ipynb` notebook.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.