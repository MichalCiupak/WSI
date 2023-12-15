import torch
from torch.utils.data import Dataset


class BCDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.Tensor(features)
        self.labels = torch.LongTensor(labels)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]
