

ds = TextClassificationDataset(900, 128, 10)
dl = DataLoader(ds, batch_size = 32)
input_size = (1, 128)