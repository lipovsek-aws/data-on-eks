git clone https://github.com/aws-neuron/aws-neuron-samples.git
cd aws-neuron-samples/torch-neuronx/training/mnist_mlp
torchrun --nnodes=1 --nproc_per_node=32 train_torchrun.py 