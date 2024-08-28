# from autologging import logged, traced
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, Normalize
import mpl_toolkits.axes_grid1.inset_locator

def plot_topo(arr, ax=None, cmap='Greys_r', shade=True, extent=None,        
aspect='equal', vmin=-100, vmax=None):
  ax = get_ax(ax)
  kwargs = dict(cmap=cmap, extent=extent, aspect=aspect, vmin=vmin, vmax=vmax)
  if shade:
    ax = shader(ax, arr, **kwargs)
  else:
    ax = imshow(ax, arr, **kwargs)
  return ax

def imshow(ax, array, cmap, extent=None, aspect='auto', vmin=None, vmax=None, \
    cbar=False):
  norm = Normalize(vmin=vmin, vmax=vmax)
  cmap = matplotlib.colormaps[cmap]
  mappable = ax.imshow(array, cmap=cmap, norm=norm, extent=extent, aspect=aspect)
  if cbar:
    cbar = plt.colorbar(mappable, ax=ax) 
  return ax
def shader(ax, array, cmap, extent=None, aspect='auto', vmin=None, vmax=None, \
    cbar=False):
  norm = Normalize(vmin=vmin, vmax=vmax)
  cmap = matplotlib.colormaps[cmap]
  if cbar: # NOTE cbar here may be misleading, as shading alters the colors
    mappable = ax.imshow(array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(mappable, ax=ax) 
  lightsrc = LightSource(azdeg=45, altdeg=45)
  shaded = lightsrc.shade(array, cmap=cmap, norm=norm)
  im = ax.imshow(shaded, extent=extent, aspect=aspect)
  return ax

def add_inset(ax, extent, width=0.5, loc='upper right', borderpad=0,\
              indicate_inset_zoom=True):
  """
  _summary_

  Parameters
  ----------
  ax : _type_
      _description_
  extent : _type_
      _description_
  width : float, optional
      in inches, by default 0.5
  loc : str, optional
      _description_, by default 'upper right'
  borderpad : int, optional
      _description_, by default 0

  Returns
  -------
  _type_
      _description_

  Notes
  -----
  """
  x1, x2, y1, y2 = extent
  aspect = (y2 - y1) / (x2 - x1)
  height = width * aspect 
  axin = mpl_toolkits.axes_grid1.inset_locator.inset_axes(ax, \
    loc=loc, width=width, height=height, borderpad=borderpad)                      
  axin.set_xlim(x1, x2)
  axin.set_ylim(y1, y2)
  if indicate_inset_zoom:
    plt.draw() # force Matplotlib to correctly update the plot and 
    # display the connectors. Otherwise, connector lines are not shown!
    ax.indicate_inset_zoom(axin, edgecolor="black")
  return axin
def get_ax(ax=None, figsize=None):
  if ax is None:
    _, ax = plt.subplots(figsize=None) 
  return ax
