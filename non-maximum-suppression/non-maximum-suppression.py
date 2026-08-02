def area(box):

    if box[1] > box[3] or box[0] > box[2]:
        return 0

    return (box[3] - box[1]) * (box[2] - box[0])

def intersects(box_1, box_2, iou_threshold):

    min_x = max(box_1[0], box_2[0])
    min_y = max(box_1[1], box_2[1])
    max_x = min(box_1[2], box_2[2])
    max_y = min(box_1[3], box_2[3])
    
    intersection = area([min_x, min_y, max_x, max_y])
    
    union = area(box_1) + area(box_2) - intersection
    
    iou = intersection / union
    
    return iou >= iou_threshold

def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here

    # sort all boxes by conf in desc order

    bci = []

    for boxes, scores, index in zip(boxes, scores, range(len(scores))):
        bci.append([boxes, scores, index])

    bci = sorted(bci, key = lambda x: x[1], reverse = True)

    selected = []

    for index in range(len(bci)):

        if bci[index][0] == [-1]:
            continue

        selected.append(bci[index][2])
        
        for index_2 in range(index+1, len(bci)):
            
            if bci[index_2][0] != [-1] and intersects(bci[index][0], bci[index_2][0], iou_threshold):
                print("intersects: ", index, index_2)
                bci[index_2][0] = [-1]

    return selected