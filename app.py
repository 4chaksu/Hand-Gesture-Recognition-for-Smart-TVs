import cv2
import numpy as np
from collections import deque, Counter
from tensorflow.keras.models import load_model
import pickle
import time

IMG_SIZE = 64
SEQUENCE_LENGTH = 30
COOLDOWN_SECONDS = 2

# Load model from pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Label map
LABEL_MAP = {"Thumbs Up": 0, "Thumbs Down": 1, "Left Swipe": 2, "Right Swipe": 3, "Stop": 4}
INVERSE_LABEL_MAP = {v: k for k, v in LABEL_MAP.items()}

def preprocess_frame(frame):
    frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    return frame / 255.0

# Initialize webcam
cap = cv2.VideoCapture(0)
sequence = deque(maxlen=SEQUENCE_LENGTH)
predictions = deque(maxlen=5)  # for smoothing
last_prediction_time = 0
display_label = ""

print("📷 Show gesture... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    flipped = cv2.flip(frame, 1)
    processed = preprocess_frame(flipped)
    sequence.append(processed)

    # Make prediction only if 30 frames collected and cooldown passed
    if len(sequence) == SEQUENCE_LENGTH and (time.time() - last_prediction_time) > COOLDOWN_SECONDS:
        input_sequence = np.expand_dims(np.array(sequence), axis=0)
        pred = model.predict(input_sequence)[0]
        predicted_label = INVERSE_LABEL_MAP[np.argmax(pred)]
        confidence = np.max(pred)

        predictions.append(predicted_label)
        most_common_label = Counter(predictions).most_common(1)[0][0]

        display_label = f"{most_common_label} ({confidence:.2f})"
        print("🔍 Prediction:", display_label)

        last_prediction_time = time.time()
        sequence.clear()

    # Show frame with prediction
    cv2.putText(flipped, display_label, (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Live Gesture", flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
