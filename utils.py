import torch
import torch.nn as nn
import torch.nn.functional as F

def save_checkpoint(model, optimizer, epoch, loss, model_name):
  PATH = './' + model_name + '.tar'
  state = {
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss
          }
  torch.save(state, PATH)
  print(f"Saved checkpoint at epoch {state['epoch']} with loss {state['loss']}")

def pad_sequence(batch):
  # Make all tensor in a batch the same length by padding with zeros
  batch = [item.t() for item in batch]
  batch = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=0.)
  return batch.permute(0, 2, 1)


def collate_fn(batch):
  # A data tuple has the form:
  # waveform, label

  tensors, targets = [], []

  # Gather in lists, and encode labels as indices
  for waveform, label in batch:
      tensors += [waveform]
      targets += [torch.tensor(label)]

  # Group the list of tensors into a batched tensor
  tensors = pad_sequence(tensors)
  targets = torch.stack(targets)

  return tensors, targets

def number_of_correct(pred, target):
    # count number of correct predictions
    return pred.squeeze().eq(target).sum().item()


def get_likely_index(tensor):
    # find most likely label index for each element in the batch
    return tensor.argmax(dim=-1)