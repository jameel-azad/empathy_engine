# Empathy Engine

A command-line tool that converts text to speech with emotion-based voice modulation. The service detects sentiment in the input text and adjusts speaking rate and volume to match the emotional tone, bridging the gap between text and expressive human-like audio.

---

## Features

* **Emotion Detection** – Classifies text as positive, negative, or neutral using VADER sentiment analysis.
* **Intensity Scaling** – Stronger emotions produce more pronounced changes in voice parameters.
* **Vocal Parameter Modulation** – Adjusts **rate** (words per minute) and **volume** (loudness) based on detected emotion and intensity.
* **Audio Output** – Saves a playable `.wav` file.

---

## Setup

### Prerequisites

* Python 3.7 or higher
* pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/jameel-azad/empathy_engine.git
   cd empathy_engine
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   ```

   * Windows:

     ```bash
     venv\Scripts\activate
     ```
   * macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt**

   ```
   pyttsx3==2.90
   vaderSentiment==3.3.2
   ```

---

## Usage

Run the script from the command line:

```bash
python empathy_engine.py "Your text here"
```

### Example

```bash
python empathy_engine.py "This is absolutely fantastic news!"
```

**Output:**

```
Audio saved to: output.wav
Detected emotion: positive (intensity: 0.68)
Voice parameters: rate=184, volume=0.94
```

### Specify Output File

```bash
python empathy_engine.py "I'm feeling a bit down." -o sad.wav
```

If no text is provided, the script will prompt for input.

---

## Design Choices

### Emotion Detection

* **Why VADER?**
  VADER (Valence Aware Dictionary and sEntiment Reasoner) is optimized for short text and returns a compound score from **-1 to +1**, capturing both polarity and intensity.

### Thresholds

* `compound ≥ 0.05` → positive
* `compound ≤ -0.05` → negative
* otherwise → neutral

---

### Intensity Scaling

* Uses absolute compound score as intensity.
* Example:

  * `"This is good"` → ~0.2 → moderate
  * `"Best news ever!"` → ~0.9 → strong

---

### Voice Parameter Modulation

| Emotion  | Rate (wpm)             | Volume                  |
| -------- | ---------------------- | ----------------------- |
| Positive | 150 + (intensity × 50) | 0.8 + (intensity × 0.2) |
| Neutral  | 150                    | 0.8                     |
| Negative | 150 – (intensity × 50) | 0.8 – (intensity × 0.2) |

**Constraints:**

* Rate: 100 → 200
* Volume: 0.6 → 1.0

---

### Why Rate & Volume?

These are reliably supported by `pyttsx3`.

* Faster + louder → excitement
* Slower + softer → sadness

(Simple, but effective emotional signaling.)

---

## Testing Examples

| Input Text               | Emotion  | Rate | Volume |
| ------------------------ | -------- | ---- | ------ |
| "I am so happy!"         | positive | ~184 | 0.94   |
| "This is just okay."     | neutral  | 150  | 0.80   |
| "I'm really frustrated." | negative | ~120 | 0.66   |

---
