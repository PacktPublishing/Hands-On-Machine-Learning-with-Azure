# Author: Parashar Shah
# Chapter: Cognitive Services
# Version: 1.0
# Date: May 25, 2018
# Replace <Subscription Key> with your valid subscription's api access key.
subscription_key = "<Access Key>"
assert subscription_key

# Replace the base url with what you see as Endpoint in the portal’s Overview section under your api

vision_base_url = "https://westus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "analyze"

# Set image_url to the URL of an image that you want to analyze.
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
    "Flickr_-_Duncan~_-_London_from_Parliament_Hill.jpg/640px-Flickr_-_Duncan~_-_London_from_Parliament_Hill.jpg"

import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Categories,Description,Color'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'descriptions' property.
analysis = response.json()
print(analysis)

image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)