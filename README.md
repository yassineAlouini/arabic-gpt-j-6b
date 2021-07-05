# Arabic GPT-J-6B
Fine-tuning the GPT-J-6B model on some Arabic datasets using Jax and its ecosystem.

## Implementation

We will be using the following GPT-J-6B implementation: https://github.com/kingoflolz/mesh-transformer-jax/.
Most likely, due to time constraints we will focus on fine-tuning on some datasets rather than training from scratch.

## Datasets

For now, Arabic Wikipedia.
Other options:

- [Arabic Poetry](https://www.kaggle.com/fahd09/arabic-poetry-dataset-478-2017)

## First results

Without even fine-tuning, it seems that the GPT-J

## Thanks

Thanks to HuggingFace and the TPU team for organising and providing the infra.

## Links

- A good introduction and many examples of Flax/JAX in [HuggingFace](https://github.com/huggingface/transformers/tree/master/examples/flax)
- The original GPT-J-6B [implementation](https://github.com/kingoflolz/mesh-transformer-jax/)
- A web [demo](https://6b.eleuther.ai/) of GPT-J-6B 
- A colab [notebook](https://colab.research.google.com/github/kingoflolz/mesh-transformer-jax/blob/master/colab_demo.ipynb#scrollTo=nvlAK6RbCJYg)
- A GPT-J "simple" [implementation](https://github.com/nickthorpie/gpt-j-simple)
- Some notes from Shawn Presser about [Swarm Training](https://www.docdroid.net/faDq8Bu/swarm-training-v01a-pdf)