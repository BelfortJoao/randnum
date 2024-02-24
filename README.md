
```
# Random Number Generator using Audio and Video Input

This Python project demonstrates how to generate pseudo-random numbers using data captured from the computer's audio and video inputs.

## Dependencies

- numpy
- sounddevice
- opencv-python

You can install the dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:
```
git clone https://github.com/BelfortJoao/randnum
```

2. Navigate to the project directory:
```
cd randnum
```

3. Install the dependencies:
```
pip install sounddevice numpy opencv-python
```

4. Run the script( run as admin or sudo):
```
python main.py
```

## Description

This project captures audio data from the computer's microphone and video data from the webcam. It then processes this data to generate a pseudo-random number using a custom random number generator. The generated number can be an integer within a specified range, or it can be a floating-point number.

## Configuration

You can configure the range of the generated random numbers and the data type (integer, floating-point, double) in the `main.py` file.

```
