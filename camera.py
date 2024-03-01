def cam():
    import cv2
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to shoot")
            break
        cv2.imshow("test", frame)
    
        k = cv2.waitKey(1)
        if k%256 == 27: #########to be changed
            # ESC pressed
            print("closing")
            break
        elif k%256 == 32:#########to be changed
            # SPACE pressed
            img_name = "test_image{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{}".format(img_name))
            img_counter += 1
    
    cam.release()
    
