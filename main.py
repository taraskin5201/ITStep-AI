import onnxruntime as ort
from PIL import Image
from torchvision import transforms
import numpy as np

# назви класів (порід собак)
classes_names= [
     'beagle',
     'bulldog',
     'dalmatian',
     'german-shepherd',
     'husky',
     'labrador-retriever',
     'poodle',
     'rottweiler'
]

# відкриваємо модель
session = ort.InferenceSession(
    "model.onnx"
)

# трансформер для підготовки зображення
test_transformer = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# відкриваємо зображення
img = Image.open("data/lesson many/husky10.jpg")

# трансформуємо зображення
input_tensor = test_transformer(img)

# додаємо батч розмір (1)
input_tensor = input_tensor.unsqueeze(0)

# конвертуємо тензор у numpy масив
input_tensor = input_tensor.numpy()

# використовуємо модель
results = session.run(
    None,
    input_feed={
        "image": input_tensor
    }
)

result = results[0][0]
print(result)

# отримуємо індекс з найбільшим значенням
ind = result.argmax()

# отримуємо назву класу за індексом
label = classes_names[ind]

# отримати ймовірність
max_num = result.max()
result -= max_num
exp_result = np.exp(result)
probs = exp_result / exp_result.sum()

prob = probs[ind]

print(f"Індекс найбільшої ймовірності: {ind}")
print(f"Порода собаки: {label}")
print(f"Ймовірність: {prob:.4f}")

img.show(f"title={label}, prob={prob:.4f}")
