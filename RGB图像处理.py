#------------------------------------------------------------------------------------------------------------------------
#文件名称：RGB图像处理

#文件内容：ov7725的RGB565图像数据，转换为jpg图像

#文件版本：1.0.0

#文件作者：阿顿

#开发环境：Python & Microsoft Visual Studio Community 2019

# 注    意：
#------------------------------------------------------------------------------------------------------------------------*/


from PIL import Image,ImageDraw


#定义图像大小为320*240
w = 320     #宽
h = 240     #高
#用于转换的
HEX = {}
RGB = []

FileAdd = "D:\\1.txt"#源文件路径



#十六进制字符转数字
def Hex_To_Dec(hex):
    if hex == '0':
        re = 0
    elif hex == '1':
        re = 1
    elif hex == '2':
        re = 2
    elif hex == '3':
        re = 3
    elif hex == '4':
        re = 4
    elif hex == '5':
        re = 5
    elif hex == '6':
        re = 6
    elif hex == '7':
        re = 7
    elif hex == '8':
        re = 8
    elif hex == '9':
        re = 9
    elif hex == 'A':
        re = 10
    elif hex == 'B':
        re = 11
    elif hex == 'C':
        re = 12
    elif hex == 'D':
        re = 13
    elif hex == 'E':
        re = 14
    elif hex == 'F':
        re = 15
    else :
        return (100)
    return (re)
#main()
if __name__ == "__main__":
    f = open(FileAdd,encoding = "utf-8")#打开文件
    print("正在合成来自" + FileAdd + "的图像数据，合成为" + str(w) + "*" + str(h) + "的图像")
    x = 0
    z = 0
    for x in range(w * h * 60):#将文本型十六进制，转为数值型十六进制
        f.seek(z+0,0)
        f1 = f.read(1)
        f.seek(z+1,0)
        f2 = f.read(1)
        f.seek(z+3,0)
        f3 = f.read(1)
        f.seek(z+4,0)
        f4 = f.read(1)
        z = z + 6
        HEX[x] = ((Hex_To_Dec(f1) << 12) + (Hex_To_Dec(f2) << 8) + (Hex_To_Dec(f3) << 4) + Hex_To_Dec(f4))
        if z >= (w * h * 6):
            break;
    f.close()#关闭文件
    x = 0
    for x in range(len(HEX)):#将RGB565转为RGB888
        r = (((HEX[x] & 0xF800) >> 8))
        g = (((HEX[x] & 0x7E0 ) >> 3))
        b = (((HEX[x] & 0x1F) << 3))
        rgb = (r, g, b)
        RGB.append(rgb)
   
    #print(RGB)
    #print(HEX)

    image = Image.new('RGB', (w, h), (255, 255, 255))#创建新图片对象
 
    draw = ImageDraw.Draw(image)# 创建Draw对象用于绘制新图:
 
    x = 0
    y = 0
    i = 0

    for y in range(h):# 填充每个像素并对对应像素填上RGB值:
       for x in range(w):
        draw.point((x, y), fill=RGB[i])
        i = i + 1
         
    image.save('D:\\2.jpeg', 'jpeg')#保存文件
    image.show()#查看图像