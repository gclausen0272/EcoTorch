

ds = ImageClassificationDataset(1000, (3, 100, 100), 3)
dl = DataLoader(ds, batch_size = 32)
input_size = (3, 100, 100)