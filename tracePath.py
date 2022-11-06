import cv2 as cv

def trace(nodes, path: list[int]) -> None:
    result = cv.imread('images/map3.jpg')

    length = len(path)

    for i in range (1, length - 1):   # path to middle point
        point = nodes[path[i]]
        x, y = int(point[0]) + 2, int(point[1]) + 2
        cv.circle(result, (x, y), 5, (0, 0, 255), thickness=3)

        x, y = int(point[0]) - 2, int(point[1]) - 2

        cv.circle(result, (x, y), 5, (0, 255, 0), thickness=3)
    
    point0 = nodes[path[0]]     # draw line 1
    x0, y0 = int(point0[0]) + 2, int(point0[1]) + 2
    point1 = nodes[path[1]]
    x1, y1 = int(point1[0]) + 2, int(point1[1]) + 2

    cv.line(result, (x0, y0), (x1, y1), (0, 0, 255), thickness=3)

    for i in range (1, length):
        point = nodes[path[i]]
        pointPrev = nodes[path[i-1]]

        xPrev, yPrev = int(pointPrev[0]), int(pointPrev[1])
        x, y = int(point[0]) + 2, int(point[1]) + 2

        point = nodes[path[length - 1]]
        cv.circle(result, (int(point[0]), int(point[1])), 5, (0, 0, 255), thickness=3)

        cv.line(result, (xPrev, yPrev), (x, y), (0, 0, 255), thickness=3)

    point = nodes[path[0]]

    cv.circle(result, (int(point[0]), int(point[1])), 5, (0, 0, 0), thickness=3)

    cv.imshow("image", result)  # display result
    cv.imwrite('images.jpg', result)
    cv.waitKey(0)