import cv2


def findIngre(in_str):
    if ':' in in_str:
        in_start = in_str.find(':')
        n_str = in_str[in_start + len(':'):]
        for i in n_str:
            if (i.isalpha()):
                break
            elif (not i.isalpha()):
                n_str = n_str[n_str.index(i) + 1:]
        n_str = n_str.replace("\n", " ")
        n_str = n_str.rstrip()
        return n_str
    n_str = in_str.lower()
    if 'ingredients' in n_str:
        in_start = n_str.find('ingredients')
        n_str = in_str[in_start + len('ingredients'):]
        for i in n_str:
            if (i.isalpha()):
                break
            elif (not i.isalpha()):
                n_str = n_str[n_str.index(i) + 1:]
        n_str = n_str.replace("\n", " ")
        n_str = n_str.rstrip()
        return n_str
    return in_str


def slicein(ingres):
    aloha = findIngre(ingres)
    ingre = ''
    in_list = []
    for i in aloha:
        if i == ',':
            in_list.append(ingre.strip())
            ingre = ''
            continue
        if i.isalnum :
            ingre += i
    in_list.append(ingre.strip())
    for i in in_list:
        if len(i) == 1 and i.isnumeric:
            if in_list.index(i) < len(in_list) - 2:
                temp = i
                in_list[in_list.index(i) + 1] = temp + "," + in_list[in_list.index(i) + 1]
                in_list.remove(i)
    return in_list

def editImg(imgPath):
    img = cv2.imread(imgPath)
    sigma=15
    blur_img = cv2.GaussianBlur(img, (0, 0), sigma)
    usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
    gray = cv2.cvtColor(usm, cv2.COLOR_BGR2GRAY)
    return gray
