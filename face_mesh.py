import cv2
import mediapipe as mp
import numpy as np
mp_face_mesh = mp.solutions.face_mesh
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(1)
cap.set(3, 1000)
cap.set(4, 600)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = mp_face_mesh.FaceMesh(refine_landmarks=True).process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=img, landmark_list= face_landmarks, 
                    connections = mp_face_mesh.FACEMESH_IRISES, 
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,0,255)),
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style()
                    )

        cv2.imshow('Mediapipe Feed', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()
