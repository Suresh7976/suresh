while True:
    status , photo = cap.read()
    cv2.imshow("my photo" , photo)
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
