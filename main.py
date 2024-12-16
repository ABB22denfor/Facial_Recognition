import threading
import cv2
import os
from deepface import DeepFace #import använda libraries

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) #val av använda kamera, 0 = datorns video kamera, 1 = extern kamera

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #val av dimensioner på kamera fönstret

frame_counter = 0 #sätter frame countern till 0

face_match = False #sätter face_match till falsk

person = "" #identifierar variabeln person som en tom string

lock = threading.Lock() #Definierar ett lås så att variabler i aktuell thread inte kan nås av andra threads

def get_images(folder_path="images"): #skapar funktionen get_imaages med folder_path som argument, 
                                    #funktionen hämtar alla bilder under images och lägger in de i reference images dictionary under rätt person
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


def check_face(frame):#skapar funktionen check_face med frame som argument, 
                    #funktionen jämför framen med bilderna från reference images 
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

while True: #true loopen checkar för identifikation genom att kolla om personen i framen matchar en av personerna på bilderna
    ret, frame = cap.read()


    if ret:
        if frame_counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        frame_counter += 1

        if face_match:
            cv2.putText(frame, person, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NOT FOUND", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
