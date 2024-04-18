# Visual Detection Card Game

## Overview

This repository contains the code for a visual detection system designed for card games. It uses OpenCV and TensorFlow
to capture and analyze the visual data from a card game in real-time, identifying cards and their positions.

## Features

- **Real-time card detection**: Utilizes the camera feed to detect and identify playing cards during a game.
- **Card recognition**: Can recognize different cards, including their suits and ranks.
- **Game analysis**: Provides insights into the game by tracking the cards played.
- **Machine Learning**: Uses TensorFlow for image recognition and processing.

## Prerequisites

- Python 3.12.3 or higher
- OpenCV library
- TensorFlow
- A webcam or external camera

## Installation

To set up the project, follow these steps:

1. Clone the repository:``````

```
git clone https://github.com/your-username/visual-detection-card-game.git
```

2. Navigate to the project directory:

```
cd visual-detection-card-game
```

3. Create a conda environment and install dependencies:

```
conda env create --file environment.yml 
```

```
conda activate visual-detection-card-game
```

## Usage

To run the card detection system, execute the following command:

```
python src/main/python/app/main.py
```

This will start the card detection system and open a window displaying the camera feed with the detected cards.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
