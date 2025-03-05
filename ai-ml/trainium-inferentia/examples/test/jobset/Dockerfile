# aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com
FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training-neuronx:1.13.1-neuronx-py310-sdk2.20.2-ubuntu20.04
#RUN git clone https://github.com/aws-neuron/aws-neuron-samples.git && \
#    cd aws-neuron-samples/torch-neuronx/training/mnist_mlp
COPY main.py /main.py