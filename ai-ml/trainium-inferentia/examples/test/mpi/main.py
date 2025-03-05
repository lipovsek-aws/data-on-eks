import jax, os

print(jax.distributed.initialize())
print(jax.device_count())
print(jax.local_device_count())

xs = jax.numpy.ones(jax.local_device_count())
result = jax.pmap(lambda x: jax.lax.psum(x, 'i'), axis_name='i')(xs)
print(result)
assert (result == int(os.environ.get("NNODES", "1"))*32).all()