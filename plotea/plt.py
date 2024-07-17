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
  if cbar: # NOTE cbar may be misleading, because lighting alters the colormap
    mappable = ax.imshow(array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(mappable, ax=ax) 
  lightsrc = LightSource(azdeg=45, altdeg=45)
  shaded = lightsrc.shade(array, cmap=cmap, norm=norm)
  im = ax.imshow(shaded, extent=extent, aspect=aspect)
  return ax
