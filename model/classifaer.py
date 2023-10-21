from torchvision.models import resnet50
import torch
import torch.nn as nn
import pickle


class Predictor(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.l =  { 0 : 'dog',
                    1 : 'cat'}
        self.weights  = torch.load('./model/best.pt', map_location=torch.device('cpu'))

        self.resnet50 = resnet50()
        num_features = self.resnet50.fc.in_features
        self.resnet50.fc = nn.Linear(num_features,2)
        self.resnet50.load_state_dict(self.weights)
        self.resnet50.eval()

    def pred(self, x: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            y_pred = self.resnet50(x)
            _, probabilities = y_pred.max(1)            
            return self.l[int(probabilities)]


