import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, Normalize

def get_ax(ax=None, figsize=None):
  if ax is None:
    _, ax = plt.subplots(figsize=None) 
  return ax

def imshow(ax, array, cmap, extent=None, aspect='auto', vmin=None, vmax=None, \
    cbar=False):
  norm = Normalize(vmin=vmin, vmax=vmax)
  cmap = matplotlib.colormaps[cmap]
  mappable = ax.imshow(array, cmap=cmap, norm=norm)
  if cbar:
    cbar = plt.colorbar(mappable, ax=ax) 
  return ax

def shade(ax, array, cmap, extent=None, aspect='auto', vmin=None, vmax=None, \
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

def plot_inset(self, ax, extent, ticks=False, labels=False, \
  width=0.4, add_to_y=0.03, **kwargs):
  x1, x2, y1, y2 = extent
  aspect = (y2 - y1) / (x2 - x1)
  height = width * aspect 
  x0 = 1 - width
  y0 = 1 - height + add_to_y
  axins = ax.inset_axes([x0, y0, width, height])
  self.plot(ax=axins, cbar=0, **kwargs)
  axins.set_xlim(x1,x2)
  axins.set_ylim(y1,y2)
  if not ticks:
    axins.set_xticks([])
    axins.set_yticks([])
  if not labels:
    axins.set_xlabel(None)
    axins.set_ylabel(None)
  ax.indicate_inset_zoom(axins, edgecolor="black")
  return axins
