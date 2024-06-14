# Strategic Fruits Card Detection

This project aims to detect strategic fruits cards using YOLOv8. It is implemented in Python and uses several libraries
for data processing and model training.

## Project Structure

The project has the following structure:

- `src/`: Contains the source code of the project.
  - `main/python/`: Contains the Python scripts for the project.
    - `app/`: Contains the scripts for the real-time application.
      - `card_detection_app.py`: Main application script for card detection.
      - `manager/`: Contains the manager classes for the application.
        - `influxdb_manager.py`: Manages interactions with InfluxDB.
        - `player_manager.py`: Manages player interactions.
    - `dataset_creation/`: Contains the scripts for creating the dataset.
    - `model_training/`: Contains the scripts for training the YOLOv8 model.
- `environment.yml`: Contains the conda environment configuration.
- `setup.py`: Contains the setup configuration for the Python package.
- `README.md`: Provides an overview of the project and instructions for installation and usage.

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

2. Navigate to the project directory:

```bash
cd strategic-fruits-card-detection
```

3. Create a new conda environment from the `environment.yml` file:

```bash
conda env create --name strategic-fruits-card-detection -f environment.yml # Change <strategic-fruits-card-detection> to your desired environment name
```

4. Activate the conda environment:

```bash
conda activate strategic-fruits-card-detection # Change <strategic-fruits-card-detection> to your desired environment name
```

5. Install the `build` and `pip` tools:

```bash
pip install --upgrade build pip
```

6. Build a source distribution (sdist) and a binary distribution (wheel) of your package:

```bash
python -m build
```

7. Install the package from the wheel file:

```bash
pip install --user dist/*.whl # If it doesn't works, change <*.whl> to the name of the wheel file generated in step 6
```

8. (OPTIONAL) If gpu isn't working for model training, install pytorch-cuda manually (remember to restart pc, it often works):

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

### Running the Application

#### For Using the Main Application

To run the main application, navigate to the `src/main/python/app` directory and run the `app.py` script:

```bash
cd src/main/python/app
```

```bash
python card_detection_app.py
python video_app.py
```

#### For Creating Your Own Card Detection

Follow the instruction in the following Jupyter notebooks:

1. `Cards Extraction.ipynb`
2. `Dataset Creation.ipynb`
3. `Strategic Fruits Card Detection - YOLOv8.ipynb`

Ensure you have Jupyter installed in your environment, and start it with:

```bash
jupyter notebook
```

Navigate to the `notebooks` directory and open the respective notebook.

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.
