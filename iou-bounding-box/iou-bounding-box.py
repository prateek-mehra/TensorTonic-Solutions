def area(box):

    if box[0] > box[2] or box[1] > box[3]:
        return 0
    
    return max(0, (box[2] - box[0]) * (box[3] - box[1]))

def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    
    inter_area = area([max(box_a[0],box_b[0]),max(box_a[1],box_b[1]),min(box_a[2],box_b[2]),min(box_a[3],box_b[3])])
    union_area = area(box_a) + area(box_b) - inter_area
    print("inter area: ", inter_area)
    print("union area: ", union_area)

    return inter_area / union_area