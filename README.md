# Empathy Engine

A command-line tool that converts text to speech with emotion-based voice modulation. The service detects sentiment in the input text and adjusts speaking rate and volume to match the emotional tone, bridging the gap between text and expressive human-like audio.

## Features

- **Emotion Detection** – Classifies text as positive, negative, or neutral using VADER sentiment analysis.
- **Intensity Scaling** – Stronger emotions produce more pronounced changes in voice parameters.
- **Vocal Parameter Modulation** – Adjusts **rate** (words per minute) and **volume** (loudness) based on detected emotion and intensity.
- **Audio Output** – Saves a playable `.wav` file.

## Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jamee-azad/empathy_engine.git
   cd empathy_engine
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**
   ```bash
   python empathy_engine.py "Your text here"
   ```
   


