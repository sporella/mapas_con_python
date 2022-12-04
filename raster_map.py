from rasterio.crs import CRS
import cartopy
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray

r = xr.open_rasterio("data/soil_moisture.tif")
crs_utm = CRS.from_string('EPSG:3857')
r2 = r.rio.reproject(crs_utm)
print(r2.rio.crs)

fig, ax = plt.subplots(dpi = 300, figsize=(4, 4), subplot_kw=dict(projection=cartopy.crs.Mercator())) 

r.plot(cbar_kwargs={'label': "Humedad de Suelo [mm]", "orientation": "horizontal"}, cmap = "Purples"
)
plt.title("")
plt.axis('off')
plt.show()
fig.savefig("./img/humedad_suelo.png", dpi=300, format="png", bbox_inches='tight', transparent=True)