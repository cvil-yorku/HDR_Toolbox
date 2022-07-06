import datetime

import matlab.engine
import imageio
import numpy as np
import pathlib

eng = matlab.engine.start_matlab()

imname = "0014"
#pathlib.
img = imageio.imread("./0014.exr")
eng.cd(r'/Users/saitedla/OneDrive - York University/School/York/Lab/HDRExploration/HDR_Toolbox', nargout=0)
eng.installHDRToolbox(nargout=0)
eng.cd(r'./source_code/Tmo/')
#eng.triarea(nargout=0)
#img = img*255
matIm = matlab.double(img.tolist())

# TMOs = ["AshikhminTMO", "BanterleTMOWithGamma", "BestExposureTMO", "BruceExpoBlendTMO", "ChiuTMO", "DragoTMOWithGamma",
#         "DurandTMO", "ExponentialTMO", "FerwerdaTMO", "KimKautzConsistentTMO", "KrawczykTMO",
#         "KuangTMO", "LischinskiTMO", "LogarithmicTMO", "NormalizeTMO", "PattanaikTMO", "RamanTMO", "ReinhardTMO",
#         "ReinhardDevlinTMO", "SchlickTMO", "TumblinTMO", "VanHaterenTMO", "WardGlobalTMO", "WardHistAdjTMO", "YPFerwerdaTMO",
#         "YPTumblinTMO", "YPWardGlobalTMO"]

TMOs = ["YPFerwerdaTMO"]
print(datetime.datetime.now())
for TMO in TMOs:
    print(TMO)
    tmo = getattr(eng, TMO)
    out = tmo(matIm)
    outNonNegative = np.array(out)
    outNonNegative = np.clip(outNonNegative, 0, None)
    print("Clipped values")
    if(TMO in ["BanterleTMOWithGamma", "DragoTMOWithGamma"]):
        eng.cd(r'./util')
        gammaOut = out
        #gammaOut = eng.GammaDrago(matlab.double(outNonNegative.tolist()))
        eng.cd(r'./../')
        print("GAMMA BANTERLE")
    else:
        gammaOut = eng.GammaTMO(matlab.double(outNonNegative.tolist()))
    print("COMPLETED GAMMA")
    npGammaOut = np.array(gammaOut)
    npOut = np.array(out)
    imageio.imwrite("out/{}.jpg".format(TMO), npOut)
    imageio.imwrite("out/gamma{}.jpg".format(TMO), npGammaOut)
print(datetime.datetime.now())
print("HI")