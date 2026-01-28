import onnxruntime as ort
from PIL import Image
from torchvision import transforms
import numpy as np
import torch



test_transform = transforms.Compose(
    [transforms.Resize([200, 200]),
    transforms.CenterCrop(180),
    transforms.ToTensor()
    ]
)

classes_names = ['all', 'hem']

names_codes = ['хвора', 'здоровa']

session = ort.InferenceSession("leukemia.onnx")

image = Image.open("data/lesson many/cells/UID_H13_11_5_hem.bmp")

# image.show()

input_tensor = test_transform(image)

# print(input_tensor, input_tensor.shape)

input_tensor = input_tensor.unsqueeze(0)

input_tensor = input_tensor.numpy()

results = session.run(
    None,
    input_feed={
        "input": input_tensor
    }
)

print(results)

result = results[0][0]
# print(result)

# print(input_tensor, input_tensor.shape)

ind = result.argmax()
print(ind)

name = classes_names[ind]
# print(name)

result_tensor = torch.tensor(result)

softmax = torch.nn.Softmax()

prob = softmax(result_tensor)

print(f"Class: {name}, Probability: {prob[ind].item():.4f}, {names_codes[ind]}")


