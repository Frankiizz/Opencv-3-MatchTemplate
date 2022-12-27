Opencv-Python 第三弹 模板匹配
--


环境：


Python 3.9.7


Opencv-python


安装：
    
    pip install opencv-python


主要流程：

1. 获取图片

    
    img = cv2.imread("path/of/img")


2. 载入模板（目标）


    temp = cv2.imread("path/to/target")


3. 匹配
    
标准相关匹配


    result = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)#max为最匹配的

平方差


    result = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)#min为最匹配的


4. 找到置信度最高的目标


    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


5. 绘制方框/圆/中心点 etc


    cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)