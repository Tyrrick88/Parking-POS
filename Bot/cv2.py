import cv2
import numpy as np
import mrcnn.model
import mrcnn.config
import os


# Define the Mrcnn config
class ParkingLotconfig(mrcnn.config.Config):
    NAME = "Parking lot"
    IMAGE_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 1 + 1 # Background + Prking space 
    STEPS_PER_EPO =   5
    VALIDATION_STEPS = 50

# Loading pre_trained models of the mrcnn
    def load_model(config):
        model = mrcnn.mode.MaskRCNN(mode='Inference', model_dir=config.MODEL_DIR, config=config)
        wieghts_path = os.path.join(config.MODEL_DIR, 'mask_rcnn_coco.h5')
        assert model.load_weight(wieghts_path, by_name=True), \
        "Cannot load the pre trained Weights"

# Creating a function that detects the car in an Image 
        
def detect_car(image, model):
    image = cv2.resize(image, (config.IMAGE_MAX_DIM, max_dim=config.IMAGE_MAX_DIM))
    image = mrcnn.utilis.resize_image(image, min_dim=config.IMAGE_MIN_DIM, mode = "square")
    image = np.expand_dims(image, 0)
    image = prep_image(image)

# Perfom the object detection.
    results = model.detect([image], verbose=0)
    
# Extract the class ID's and Score from the result.
    r = results[0]
    class_ids = r['class_ids']
    scores = r["scores"]