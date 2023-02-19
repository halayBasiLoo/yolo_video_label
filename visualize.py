import cv2
import os

def visualize_bbox(img_file, yolo_ann_file, label_dict):
    """
    Plots bounding boxes on images

    Input:
    img_file : numpy.array
    yolo_ann_file: Text file containing annotations in YOLO format
    label_dict: Dictionary of image categories    
    """
    
    frame = cv2.imread(img_file)
    im_height, im_width, _ = frame.shape

    with open(yolo_ann_file, "r") as fin:
        for line in fin:
            cat, center_w, center_h, width, height = line.split()
            cat = int(cat)
            category_name = label_dict[cat]
            left = (float(center_w) - float(width) / 2) * im_width
            top = (float(center_h) - float(height) / 2) * im_height
            width = float(width) * im_width
            height = float(height) * im_height

            p1 = (int(left), int(top))
            p2 = (int(left + width), int(top + height))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

            cv2.imshow("frame",frame)


    cv2.imshow("gt",frame)
    cv2.waitKey(0)


def main():
    """
    Plots bounding boxes
    """

    labels = {0: "uav"}

    all_files = os.listdir("./labels")
    image_count = len(all_files)//2
    img_file = "./labels/img_{}.png"
    ann_file =  "./labels/img_{}.txt" #img_file.split(".")[0] + ".txt"
    for i in range(1,image_count):
        print("image : ",img_file.format(i))
        visualize_bbox(img_file.format(i), ann_file.format(i), labels)


if __name__ == "__main__":
    main()

