f = open("output.txt", "w")

def detect_labels():
    import io
    import os
    # Imports the Google Cloud client library
    from google.cloud import vision
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # The name of the image file to annotate
    file_name = os.path.abspath('./wakeupcat.jpg')
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:', file=f)
    for label in labels:
        print(label.description, file=f)

detect_labels()