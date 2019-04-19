import openslide
import cv2
import numpy as np

'''
slide_path = './patient_000/patient_000_node_3.tif'
slide = openslide.OpenSlide(slide_path)
levels = slide.level_count
print(levels)
mask_level = 5
slide_map = np.array(slide.get_thumbnail(slide.level_dimensions[mask_level]))
slide_map = cv2.cvtColor(np.array(slide_map), cv2.COLOR_RGBA2BGR)
cv2.imwrite('slide.png', slide_map)

#extract patches from slide image
patch_size = 256
step = int(patch_size / (2 * mask_level))
mask_local1 = np.array([3250,1000])
x = mask_local1[0]
y = mask_local1[1]

patch_local1 = 2 * mask_level * mask_local1
patch = slide.read_region((patch_local1[0]*5,patch_local1[1]*5), 0, (patch_size,patch_size)) #extract normal patch in level 0
patch.save('patch1.png')
'''
'''
cv2.rectangle(slide_map, (mask_local1[0],mask_local1[1]), (mask_local1[0]+255, mask_local1[1]+255), (255, 255, 255), 1)
cv2.imwrite('slide_map.png', slide_map)
print(slide_map.shape)
patch1 = slide_map[x:x+patch_size, y:y+patch_size] #extract normal patch in level 0
print(patch1.shape)
cv2.imwrite('patch1.png', patch1)
'''


import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image

# Open image file
image = Image.open('unseen WSI.png')
my_dpi=300.

# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

# Set the gridding interval: here we use the major tick interval
myInterval=50.
loc = plticker.MultipleLocator(base=myInterval)
print(loc)
ax.xaxis.set_minor_locator(plticker.MultipleLocator(base=20))
ax.yaxis.set_minor_locator(plticker.MultipleLocator(base=20))

# Add the grid
#ax.grid(which='major', axis='both', linestyle='-',c='r')
ax.grid(which = 'minor', axis='both', linestyle='-',c='r',linewidth = 0.5)
# Add the image
ax.imshow(image)

# Find number of gridsquares in x and y direction
#nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval)))
#ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval)))

# Add some labels to the gridsquares
'''
for j in range(ny):
    y=myInterval/2+j*myInterval
    for i in range(nx):
        x=myInterval/2.+float(i)*myInterval
        ax.text(x,y,'{:d}'.format(i+j*nx),color='w',ha='center',va='center')
'''
# Save the figure
fig.savefig('myImageGrid.tiff',dpi=my_dpi)