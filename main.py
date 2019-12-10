from math import exp

type = "warezmaster"

f = open("kddcup.data_10_percent_corrected", "r")
data = f.read()
f.close()
q = data.split(".\n")
for i in range(len(q)):
    q[i] = q[i].split(",")


def norm_text(index):
    to_list = list(normal[index])
    l = len(to_list) - 1
    word_norm = {}
    for i in range(len(to_list)):
        word_norm[to_list[i]] = round(i*(1/l), 2)
    return word_norm


normal = [{"min": int(q[0][0]), "max": int(q[0][0])}, set(), set(), set(), {"min": int(q[4][0]), "max": int(q[4][0])},
          {"min": int(q[5][0]), "max": int(q[5][0])}, {"min": int(q[6][0]), "max": int(q[6][0])}, {"min": int(q[7][0]), "max": int(q[7][0])},
          {"min": int(q[8][0]), "max": int(q[8][0])}, {"min": int(q[9][0]), "max": int(q[9][0])}, {"min": int(q[10][0]), "max": int(q[10][0])},
          {"min": int(q[11][0]), "max": int(q[11][0])}, {"min": int(q[12][0]), "max": int(q[12][0])}, {"min": int(q[13][0]), "max": int(q[13][0])},
          {"min": int(q[14][0]), "max": int(q[14][0])}, {"min": int(q[15][0]), "max": int(q[15][0])}, {"min": int(q[16][0]), "max": int(q[16][0])},
          {"min": int(q[17][0]), "max": int(q[17][0])}, {"min": int(q[18][0]), "max": int(q[18][0])}, {"min": int(q[19][0]), "max": int(q[19][0])},
          {"min": int(q[20][0]), "max": int(q[20][0])}, {"min": int(q[21][0]), "max": int(q[21][0])}, {"min": int(q[22][0]), "max": int(q[22][0])},
          {"min": int(q[23][0]), "max": int(q[23][0])}, {"min": float(q[24][0]), "max": float(q[24][0])}, {"min": float(q[25][0]), "max": float(q[25][0])},
          {"min": float(q[26][0]), "max": float(q[26][0])}, {"min": float(q[27][0]), "max": float(q[27][0])}, {"min": float(q[28][0]), "max": float(q[28][0])},
          {"min": float(q[29][0]), "max": float(q[29][0])}, {"min": float(q[30][0]), "max": float(q[30][0])}, {"min": int(q[31][0]), "max": int(q[31][0])},
          {"min": int(q[32][0]), "max": int(q[32][0])}, {"min": float(q[33][0]), "max": float(q[33][0])}, {"min": float(q[34][0]), "max": float(q[34][0])},
          {"min": float(q[35][0]), "max": float(q[35][0])}, {"min": float(q[36][0]), "max": float(q[36][0])}, {"min": float(q[37][0]), "max": float(q[37][0])},
          {"min": float(q[38][0]), "max": float(q[38][0])}, {"min": float(q[39][0]), "max": float(q[39][0])}, {"min": float(q[40][0]), "max": float(q[40][0])}, set()]

for i in range(len(q) - 1, -1, -1):
    if q[i][41] == type or q[i][41] == "normal":
        for j in range(len(q[i])):
            if j != 1 and j != 2 and j != 3 and j != 41:
                if (j != 24 and j != 25 and j != 26 and j != 27 and j != 28 and j != 29 and j != 30 and j != 33
                    and j != 34 and j != 35 and j != 36 and j != 37 and j != 38 and j != 39 and j != 40):
                    q[i][j] = int(q[i][j])
                    if normal[j]["max"] < q[i][j]:
                        normal[j]["max"] = q[i][j]
                    if normal[j]["min"] > q[i][j]:
                        normal[j]["min"] = q[i][j]
                else:
                    q[i][j] = float(q[i][j])
                    if normal[j]["max"] < q[i][j]:
                        normal[j]["max"] = q[i][j]
                    if normal[j]["min"] > q[i][j]:
                        normal[j]["min"] = q[i][j]
            else:
                normal[j].add(q[i][j])
    else:
        del q[i]
        continue

normal[1] = norm_text(1)
normal[2] = norm_text(2)
normal[3] = norm_text(3)


for i in range(len(q)):
    for j in range(len(q[i]) - 1):
        if j != 1 and j != 2 and j != 3:
            if normal[j]["max"] != normal[j]["min"]:
                q[i][j] = (q[i][j] - normal[j]["min"])/(normal[j]["max"] - normal[j]["min"])
        else:
            q[i][j] = normal[j][q[i][j]]


inputt = "0,tcp,http,SF,219,1337,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,6,6,0.00,0.00,0.00,0.00,1.00,0.00,0.00,39,39,1.00,0.00,0.03,0.00,0.00,0.00,0.00,0.00,normal"
input_data_all = inputt.split(",")
input_data = input_data_all[:-1]
for j in range(len(input_data)):
    if j != 1 and j != 2 and j != 3:
        if normal[j]["max"] != normal[j]["min"]:
            input_data[j] = (float(input_data[j]) - normal[j]["min"])/(normal[j]["max"] - normal[j]["min"])
        else:
            input_data[j] = float(input_data[j])
    else:
        input_data[j] = normal[j][input_data[j]]



class Input_L:
    def activation(self, x):
        self.y = x * 1
        return self.y


class Image_L:
    def __init__(self, w):
        self.w = w

    def activation(self, x):
        sum = 0
        for i in range(len(self.w)):
            sum += exp(-(self.w[i] - x[i])**2/0.3**2)
        return sum


class Add_L:
    def activation(self, x):
        sum = 0
        for i in x:
            sum += i
        res = sum / len(x)
        return res


class Output_L:
    def activation(self, x):
        clas = "normal"
        val = x[clas]
        for i in x.items():
            if i[1] > val:
                clas = i[0]
        return clas


input_list = []
for i in range(len(input_data)):
    input_list.append(Input_L)

image_list = []
for i in range(len(q)):
    image_list.append(Image_L(q[i][:-1]))

class_A = Add_L()
class_B = Add_L()

res = Output_L()

y_input = []
y_image = []
y_add = {}

for i in range(len(input_data)):
    y_input.append(input_list[i].activation(input_list[i], input_data[i]))

y_image.append([])
y_image.append([])
for i in range(len(q)):
    if q[i][41] == "normal":
        y_image[0].append(image_list[i].activation(y_input))
    else:
        y_image[1].append(image_list[i].activation(y_input))



y_add.update({"normal": class_A.activation(y_image[0])})
y_add.update({type: class_B.activation(y_image[1])})

res = res.activation(y_add)

print("Класс",res)