from PIL import Image
import os, sys
import fractions

im = Image.open(input())
rgb_im = im.convert('RGBA')
(w,h)=im.size
print(w,h)
coord=input("Coord.(x,w):")
coord=coord.split(",")
coord=list(map(int,coord))
print("Transparent color:")
rf=input("\tr:")
gf=input("\tg:")
bf=input("\tb:")
af=input("\ta:")
mode=input("Code-mode:")
monochrome=input("Single-color?(N|Y):")

if monochrome=="Y":
    rcm=input("\tr:")
    gcm=input("\tg:")
    bcm=input("\tb:")
else:
    pass
    
daw=0
arr=[]
print("#include \"Adafruit_GFX.h\"")
print("#include \"Adafruit_ILI9341.h\"")
print("Adafruit_ILI9341 tft = Adafruit_ILI9341(D8,D1,D7,D5,D2,D6);")
print("void setup(){")
print("\ttft.begin();")
print("\ttft.setRotation(3);")
print("\ttft.fillScreen(ILI9341_BLACK);")
for i in range(w):
    for j in range(h):
        r, g, b,a = rgb_im.getpixel((i,j))
        try:
            if r==int(rf) and g==int(gf) and b==int(bf) or a==int(af):
                pass
            elif mode=="1":
                daw+=1
                print("\ttft.drawPixel({},{},tft.color565({},{},{}));".format(str(i+coord[0]),str(j+coord[1]),str(r),str(g),str(b)))
            elif mode=="2":
                arr.append((i,j,r,g,b))
        except:
            break
if mode=="2":
    print("\tint pix[][]={")
    for i in arr:
        z,h,r,b,g=i
        print("{}{},{},{},{},{}{}".format("{",z,h,r,g,b,"}"),end=",")
    print("};")
    print("\nfor(int g=0;g<pix.length();g++){")
    print("\tdrawPixel(g[0],g[1],tft.color565(g[2],g[3],g[4]));}}")
print("\n\n\n\n\n//Lines:{}".format(daw))
print("}")
print("void loop() {")
print(" // put your main code here, to run repeatedly:")
print("}")
