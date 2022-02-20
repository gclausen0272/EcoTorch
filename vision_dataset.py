

ds = ImageClassificationDataset(900, (3, 100, 100), 10)
dl = DataLoader(ds, batch_size = 32)
input_size = (3, 100, 100)