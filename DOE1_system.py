#%%
from Optical_object import *
from System import *
import time

Air_coefficient = [0,0,0,0,0,0]
LASF46B_coefficient = [2.17988922,0.306495184,1.56882437,0.012580538,0.056719137,105.316538]    #1.9
SF69_coefficient = [1.62594647,0.235927609,1.674346230,0.01216966770,0.0600710405,145.6519080]  #1.7
Nc_coefficient = [1.9**2-1,0,0,0,0,0]
Air = Material('Air',Air_coefficient)
LASF46B = Material('LASF46B',LASF46B_coefficient)
NC = Material('nc',Nc_coefficient)

source = Source([-38,11.53,1.45],-0.1,[-20,20,-15,15],[0.525], 
                stokes_vector = [1,0,0,0],
                fov_grid = (5,5),
                spatial_grid = (7,7))

G1 = Grating([[0.3795,11]],[Air,LASF46B], add_order = (1,0))
F2 = Fresnel_loss([LASF46B,Air])
R1 = Receiver()

system = System(Air)
system.add_source(source)
system.add_element(0,G1,np.array([-38,11.53,1.5]))
system.add_element(0,R1,np.array([[14.62,28.76],[-40.38,28.76],[-40.38,-11.24],[14.62,-11.24],[14.62,28.76]]))
system.add_element(0.5,F2,np.array([[14.62,28.76],[-40.38,28.76],[-40.38,-11.24],[14.62,-11.24],[14.62,28.76]]))

#%%
t0 = time.time()
system.run(max_iter = 300,save_rays = True)
print(time.time()-t0)

#%%
system.draw()
# %%
import matplotlib.pyplot as plt
eyebox = np.vstack(R1.store)
first_order = eyebox[:,1]>0
plt.scatter(eyebox[first_order,4] , eyebox[first_order,5])

plt.show()
# %%