def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here

    grayscale_img = []

    for row in image:
        
        gs_row = []
        
        for pixel in row:
            gs_pixel = 0.299*pixel[0]+0.587*pixel[1]+0.114*pixel[2]
            gs_row.append(gs_pixel)
        grayscale_img.append(gs_row)

    return grayscale_img
            
            