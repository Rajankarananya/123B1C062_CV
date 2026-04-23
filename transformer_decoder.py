import torch
import torch.nn as nn

model = nn.Transformer(
    d_model=512,
    nhead=8,
    num_encoder_layers=2,
    num_decoder_layers=2
)

src = torch.rand((10, 1, 512))
tgt = torch.rand((8, 1, 512))

out = model(src, tgt)

print("Transformer Sequence Model Complete")
print("Output Shape:", out.shape)