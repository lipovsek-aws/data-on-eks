# There's https://github.com/aws/deep-learning-containers/tree/master and https://github.com/aws-neuron/deep-learning-containers
FROM public.ecr.aws/neuron/jax-training-neuronx:0.4-neuronx-py310-sdk2.21.1-ubuntu22.04

# RUN mkdir -p /var/run/sshd
# RUN sed -i 's/[ #]\(.*StrictHostKeyChecking \).*/ \1no/g' /etc/ssh/ssh_config && \
#     echo "    UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config && \
#     sed -i 's/#\(StrictModes \).*/\1no/g' /etc/ssh/sshd_config

COPY main.py /main.py