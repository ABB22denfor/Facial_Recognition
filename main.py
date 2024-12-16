import threading
import cv2
import os
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

person = ""

lock = threading.Lock()

def get_images(folder_path="images"):
    reference_images = {}
    for person in os.listdir(folder_path):
        person_path = os.path.join(folder_path, person)
        if os.path.isdir(person_path):
            reference_images[person] = []
            for image_name in os.listdir(person_path):
                image_path = os.path.join(person_path, image_name)
                try:
                    img = cv2.imread(image_path)
                    reference_images[person].append(img)
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")
    return reference_images


def check_face(frame):
    global face_match
    global person

    ref = get_images()
    try:
        for person in ref:
            for img in ref[person]:
                if DeepFace.verify(frame, img.copy())['verified']:
                    with lock:
                        face_match = True
                        person = person
                        return
    except Exception as e:
        with lock:
            person = ""
            face_match = False

while True:
    ret, frame = cap.read()


    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, person, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NOT FOUND", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
