import plotea.plt

def plot_topo(*args, api='plt', **kwargs):
  if api == 'plt':
    return plotea.plt.plot_topo(*args, **kwargs)
  else:
    raise NotImplementedError(f'API: {api}')
  
def imshow(*args, api='plt', **kwargs):
  if api == 'plt':
    return plotea.plt.imshow(*args, **kwargs)
  else:
    raise NotImplementedError(f'API: {api}')
def shade(*args, api='plt', **kwargs):
  if api == 'plt':
    return plotea.plt.shade(*args, **kwargs)
  else:
    raise NotImplementedError(f'API: {api}')