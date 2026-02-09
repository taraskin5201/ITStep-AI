import onnxruntime as ort
from PIL import Image
from torchvision import transforms
import numpy as np

classes_names = [
    'Apple Braeburn', 'Apple Granny Smith', 'Apricot', 'Avocado',
    'Banana', 'Blueberry', 'Cactus fruit', 'Cantaloupe',
    'Cherry', 'Clementine', 'Corn', 'Cucumber Ripe',
    'Grape Blue', 'Kiwi', 'Lemon', 'Limes',
    'Mango', 'Onion White', 'Orange', 'Papaya',
    'Passion Fruit', 'Peach', 'Pear',
    'Pepper Green', 'Pepper Red', 'Pineapple',
    'Plum', 'Pomegranate', 'Potato Red',
    'Raspberry', 'Strawberry', 'Tomato', 'Watermelon'
]

session = ort.InferenceSession(
    "fruit_classifier.onnx"
)

test_transformer = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

img = Image.open("data/lesson many/fruits/2.jpg").convert("RGB")

input_tensor = test_transformer(img)
input_tensor = input_tensor.unsqueeze(0)
input_tensor = input_tensor.numpy()

results = session.run(
    None,
    input_feed={
        "input": input_tensor
    }
)

result = results[0][0]
print("Raw output:", result)

ind = result.argmax()
label = classes_names[ind]

max_num = result.max()
result -= max_num
exp_result = np.exp(result)
probs = exp_result / exp_result.sum()

prob = probs[ind]

print(f"Індекс найбільшої ймовірності: {ind}")
print(f"Клас фрукта: {label}")
print(f"Ймовірність: {prob:.4f}")

img.show(title=f"{label}, prob={prob:.4f}")
