import numpy as np
import sounddevice as sd
import cv2

def custom_random(seed, lower_bound=None, upper_bound=None, number_type='int'):
    max_value = 2 ** 32 - 1
    while True:
        seed = hash(seed)
        if lower_bound is not None and upper_bound is not None:
            if number_type == 'int':
                scaled_value = lower_bound + (seed % (upper_bound - lower_bound + 1))
            elif number_type == 'float':
                scaled_value = lower_bound + (seed % (upper_bound - lower_bound + 1)) + np.random.rand()
            elif number_type == 'double':
                scaled_value = lower_bound + (seed % (upper_bound - lower_bound + 1)) + np.random.rand()
        else:
            if number_type == 'int':
                scaled_value = seed % max_value
            elif number_type == 'float':
                scaled_value = seed % max_value + np.random.rand()
            elif number_type == 'double':
                scaled_value = seed % max_value + np.random.rand()
        yield scaled_value


def generate_random_number(lower_bound=None, upper_bound=None, number_type='int'):
    duration = 3
    fs = 44100
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    audio_mean = np.mean(audio_data)
    audio_std = np.std(audio_data)
    audio_random_seed = int((audio_mean + audio_std) * 10000)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image_mean = np.mean(gray_frame)
    image_std = np.std(gray_frame)
    image_random_seed = int((image_mean + image_std) * 10000)

    random_seed = audio_random_seed + image_random_seed + sum(ord(char) for char in "fubá")

    custom_rng = custom_random(random_seed, lower_bound, upper_bound, number_type)

    random_number = next(custom_rng)

    return random_number


if __name__ == "__main__":
    # Generating a random integer without bounds
    random_number = generate_random_number()
    print("Generated random integer without bounds:", random_number)

    # Generating a random integer within the specified range
    lower_bound = -100
    upper_bound = 100
    random_number = generate_random_number(lower_bound, upper_bound)
    print(f"Generated random integer between {lower_bound} and {upper_bound}:", random_number)

    # Generating a random floating-point number without bounds
    random_number = generate_random_number(number_type='float')
    print("Generated random floating-point number without bounds:", random_number)

    # Generating a random double-precision floating-point number within the specified range
    lower_bound = -100.0
    upper_bound = 100.0
    random_number = generate_random_number(lower_bound, upper_bound, number_type='double')
    print(f"Generated random double-precision floating-point number between {lower_bound} and {upper_bound}:",
          random_number)
