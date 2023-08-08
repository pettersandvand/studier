import timeit
import cv2


def python_color2gray(filename):
    '''
    Convert image to grayscale using python.
    Args:
        filename: filename/path to the wanted image.

    Returns: image

    '''
    try:
        image = cv2.imread(filename)
    except Exception:
        print("cant find file specified")
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #HT Goes through the with of the picture
    for i in range(len(image)):
        #HT Goes through the height of the picture
        for j in range(len(image[i])):
            tmp = image[i][j][0] * .21 + image[i][j][1] * .72 + image[i][j][2] * .07
            #HT Add the weights
            image[i][j] = (tmp, tmp, tmp)
    image = image.astype("uint8")
    return image


def report_py_gray():
    filename = "./rain.jpg"

    f = open("reports/python_report_color2gray.txt", "w")
    time3 = (timeit.timeit(lambda: python_color2gray(filename), number=3)) / 3
    # HT removed comment-out line
    f.write(f"Dimensions of the image being grayscaled: {filename}")
    image = cv2.imread(filename)
    f.write("\n")
    f.write(f"H: {len(image)} \nW: {len(image[0])} \nC: {len(image[0][0])}")
    f.write("\n\n")

    f.write("Timing : python_color2gray")
    f.write("\n")
    f.write("Average runtime running python_color2gray after 3 runs : {:.6f} s".format(time3))
    f.write("\n")
    f.write("Timing performed using : timeit")
    f.close()
