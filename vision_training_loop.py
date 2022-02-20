

optimizer    =  torch.optim.Adam(model.fc.parameters(), lr=0.001)
criterion    =  nn.NLLLoss()

tracker = EmissionsTracker()

tracker.start()
for epoch in range(1):

    model.train() # This sets the model back to training after the validation step
    print('\nEpoch Number {}'.format(epoch+1))

    training_loss = 0.0
    correct_preds = 0
    best_acc = 0
    total = 0

    train_data_loader = tqdm.tqdm(dl)

    for i, j in train_data_loader:
        outputs = model(i)
        optimizer.zero_grad()

        loss = criterion(outputs, j)
        loss.backward()
        optimizer.step()
        training_loss += loss.item()

    #epoch_loss = training_loss / dataset_size['train']
tracker.stop()
