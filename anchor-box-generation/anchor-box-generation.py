import math

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here

    stride = image_size / feature_size

    boxes = []

    for i in range(image_size):
        for j in range(image_size):

            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            if cx > image_size or cy > image_size:
                continue

            for scale in scales:
                for ar in aspect_ratios:
                    w = scale * math.sqrt(ar)
                    h = scale / math.sqrt(ar)

                    boxes.append([cx - w/2, cy - h/2, cx + w/2, cy + h/2])

    return boxes