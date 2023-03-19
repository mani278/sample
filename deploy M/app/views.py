from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, "home.html")


def predict(request):
    values = []
    a = 0
    b = 1
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        for i in range(len(int_features)):
            int_features[i] = int(int_features[i])
        print(int_features)

        for i in range(int(len(int_features)/2)):
            print(i)
            print((int_features[a]/int_features[b]))
            z = (int_features[a]/int_features[b])
            values.append(z)
            a += 2
            b += 2


        print('values',values)
    
    if values[0] > 1 and values[0] < 15:
        a = 'High'
    elif values[0] > 15.1 and values[0] < 30:
        a = 'Medium'
    elif values[0] > 30:
        a = 'Low'


    if values[1] > 1 and values[1] < 120:
        b = 'High'
    elif values[1] > 120.1 and values[1] < 240:
        b = 'Medium'
    elif values[1] > 240:
        b = 'Low'

    values[2] = values[2]*100
    if values[2] > 70:
        c = 'High'
    elif values[2] > 35.1 and values[2] < 70:
        c = 'Medium'
    elif values[2] > 1 and values[2] < 35:
        c = 'Low'

    values[3] = values[3]*100
    if values[3] > 60:
        d = 'High'
    elif values[3] > 30.1 and values[3] < 70:
        d = 'Medium'
    elif values[3] > 0 and values[3] < 30:
        d = 'L'

    values[4] = values[4]*100
    if values[2] > 70:
        e = 'High'
    elif values[2] > 35.1 and values[2] < 70:
        e = 'Medium'
    elif values[2] > 1 and values[2] < 35:
        e = 'Low'

    values[5] = values[5]*100
    if values[5] > 0 and values[5] < 30:
        f = 'High'
    elif values[5] > 31.1 and values[5] < 60:
        f = 'Medium'
    elif values[5] > 60:
        f = 'Low'


    if values[6] > 0 and values[6] < 1.6:
        g = 'H'
    elif values[6] > 1.61 and values[6] < 3.2:
        g = 'M'
    elif values[6] > 3.3 and values[6] < 5:
        g = 'L'

    values[7] = values[7]*100
    if values[7] > 66.1 and values[7] < 100:
        h = 'High'
    elif values[7] > 33.1 and values[7] < 66:
        h = 'Medium'
    elif values[7] > 1 and values[7] < 33:
        h = 'Low'

    values[8] = values[8]*100
    if values[8] > 0 and values[8] < 0.5:
        i = 'High'
    elif values[8] > 0.6 and values[8] < 1:
        i = 'Medium'
    elif values[8] > 1:
        i = 'Low'

    values[9] = values[9]*100
    if values[9] > 66.1 and values[9] < 100:
        j = 'High'
    elif values[9] > 33.1 and values[9] < 66:
        j = 'Medium'
    elif values[9] > 1 and values[9] < 33:
        j = 'Low'

    values[10] = values[10]*100
    if values[10] > 66.1 and values[10] < 100:
        k = 'High'
    elif values[10] > 33.1 and values[10] < 66:
        k = 'Medium'
    elif values[10] > 1 and values[10] < 33:
        k = 'Low'


    if values[11] > 1 and values[11] < 30:
        l = 'High'
    elif values[11] > 30.1 and values[11] < 60:
        l = 'Medium'
    elif values[11] > 60:
        l = 'Low'

    values[12] = values[12]*100
    if values[11] > 66.1 and values[11] < 100:
        m = 'High'
    elif values[11] > 33.1 and values[11] < 66:
        m = 'Medium'
    elif values[11] > 1 and values[11] < 33:
        m = 'Low'

    
    if values[13] > 1 and values[13] < 15:
        n = 'High'
    elif values[13] > 15.1 and values[13] < 30:
        n = 'Medium'
    elif values[13] > 30:
        n = 'Low'



#########################################################################


    values[14] = values[14]*100
    if values[14] > 66.1 and values[14] < 100:
        o = 'High'
    elif values[14] > 33.1 and values[14] < 66:
        o = 'Medium'
    elif values[14] > 1 and values[14] < 33:
        o = 'Low'

    values[15] = values[15]*100
    if values[15] > 0 and values[11] < 0.05:
        p = 'High'
    elif values[11] > 0.06 and values[11] < 1:
        p = 'Medium'
    elif values[11] > 1:
        p = 'Low'


    if values[16] > 6 and values[16] < 7:
        q = 'High'
    elif values[16] > 4 and values[16] < 5:
        q = 'Medium'
    elif values[16] > 1 and values[16] < 3:
        q = 'Low'

    values[17] = values[17]*100
    if values[17] > 0 and values[17] < 1:
        r = 'High'
    elif values[17] > 1.1 and values[17] < 2:
        r = 'Medium'
    elif values[17] > 2:
        r = 'Low'


    values[18] = values[18]*100
    if values[18] > 85:
        s = 'High'
    elif values[18] > 44.1 and values[18] < 85:
        s = 'Medium'
    elif values[18] > 1 and values[18] < 44:
        s = 'Low'


    values[19] = values[19]*100
    if values[19] > 5:
        t = 'High'
    elif values[19] > 2.6 and values[19] < 4.9:
        t = 'Medium'
    elif values[19] > 1 and values[19] < 2.5:
        t = 'Low'


    values[20] = values[20]*100
    if values[20] > 14:
        u = 'High'
    elif values[20] > 7 and values[20] < 13.9:
        u = 'Medium'
    elif values[20] > 1 and values[20] < 6.9:
        u = 'Low'


    values[21] = values[21]*100
    if values[21] > 0 and values[21] < 1:
        v = 'High'
    elif values[21] > 1.1 and values[11] < 2:
        v = 'Medium'
    elif values[11] > 2:
        v = 'Low'

    
    values[22] = values[22]*100
    if values[22] > 0 and values[22] < 1:
        w = 'High'
    elif values[22] > 1.1 and values[22] < 2:
        w = 'Medium'
    elif values[22] > 2:
        w = 'Low'


    values[23] = values[23]*100
    if values[23] > 0 and values[23] < 0.05:
        x = 'High'
    elif values[23] > 0.06 and values[23] < 1:
        x = 'Medium'
    elif values[23] > 1:
        x = 'Low'


    
########################################################################


    values[24] = values[24]*100
    if values[24] >= 66.1 and values[24] <= 100:
        i1 = 'High'
    elif values[24] >= 33.1 and values[24] <= 66:
        i1 = 'Medium'
    elif values[24] >= 1 and values[24] <= 33:
        i1 = 'Low'


    values[25] = values[25]*100
    if values[25] >= 0 and values[25] <= 10:
        i2 = 'High'
    elif values[25] >= 10.1 and values[25] <= 20:
        i2 = 'Medium'
    elif values[25] >= 20.1 and values[25] <=30:
        i2 = 'Low'


    values[26] = values[26]*100
    if values[26] >= 0 and values[26] <= 0.05:
        i3 = 'High'
    elif values[26] >= 0.06 and values[26] <= 1:
        i3 = 'Medium'
    elif values[26] > 1:
        i3 = 'Low'


    values[27] = values[27]*1000
    if values[27] >= 0 and values[27] <= 0.6:
        i4 = 'High'
    elif values[27] >= 0.7 and values[27] <= 1.2:
        i4 = 'Medium'
    elif values[27] > 1.2:
        i4 = 'Low'


    values[28] = values[28]*100
    if values[28] >= 0 and values[28] <= 0.05:
        i5 = 'High'
    elif values[28] >= 0.06 and values[28] <= 1:
        i5 = 'Medium'
    elif values[28] > 1:
        i5 = 'Low'


    values[29] = values[29]*100
    if values[29] >= 0 and values[29] <= 0.05:
        i6 = 'High'
    elif values[29] >= 0.06 and values[29] <= 1:
        i6 = 'Medium'
    elif values[29] > 1:
        i6 = 'Low'


    values[30] = values[30]*100
    if values[30] >= 0 and values[30] <= 0.05:
        i7 = 'High'
    elif values[30] >= 0.06 and values[30] <= 1:
        i7 = 'Medium'
    elif values[30] > 1:
        i7 = 'Low'


    values[31] = values[31]*100
    if values[31] >= 66.1 and values[31] <= 100:
        i8 = 'High'
    elif values[31] >= 33.1 and values[31] <= 66:
        i8 = 'Medium'
    elif values[31] >= 1 and values[31] <= 33:
        i8 = 'Low'


    values[32] = values[32]*1000
    if values[32] >= 0 and values[32] <= 0.05:
        i9 = 'High'
    elif values[32] >= 0.06 and values[32] <= 1:
        i9 = 'Medium'
    elif values[32] > 1:
        i9 = 'Low'


    values[33] = values[33]*100
    if values[33] >= 0 and values[33] <= 0.1:
        i10 = 'High'
    elif values[33] >= 0.2 and values[33] <= 0.3:
        i10 = 'Medium'
    elif values[33] > 0.3:
        i10 = 'Low'


    values[34] = values[34]*1000
    if values[34] >= 0 and values[34] <= 0.005:
        i11 = 'High'
    elif values[34] >= 0.006 and values[34] <= 0.01:
        i11 = 'Medium'
    elif values[34] > 0.01:
        i11 = 'Low'


    values[35] = values[35]*100
    if values[35] >= 0 and values[35] <= 0.05:
        i12 = 'High'
    elif values[35] >= 0.06 and values[35] <= 1:
        i12 = 'Medium'
    elif values[35] > 1:
        i12 = 'Low'


    values[36] = values[36]*100
    if values[36] >= 67.1 and values[36] <= 100:
        i13 = 'High'
    elif values[36] >= 33.1 and values[36] <= 67:
        i13 = 'Medium'
    elif values[36] >=1 and values[36] <= 33:
        i13 = 'Low'


    values[37] = values[37]*100
    if values[37] >= 0 and values[37] <= 2.59:
        i14 = 'High'
    elif values[37] >= 2.6 and values[37] <= 5:
        i14 = 'Medium'
    elif values[37] > 5:
        i14 = 'Low'


    values[38] = values[38]*100
    if values[38] >= 0 and values[38] <= 0.05:
        i15 = 'High'
    elif values[38] >= 0.06 and values[38] <= 1:
        i15 = 'Medium'
    elif values[38] > 1:
        i15 = 'Low'


    values[39] = values[39]*1000
    if values[39] >= 0 and values[39] <= 0.005:
        i16 = 'High'
    elif values[39] >= 0.006 and values[39] <= 0.01:
        i16 = 'Medium'
    elif values[39] > 0.01:
        i16 = 'Low'


    values[40] = values[40]*100
    if values[40] >= 0 and values[40] <= 5:
        i17 = 'High'
    elif values[40] >= 5.1 and values[40] <= 10:
        i17 = 'Medium'
    elif values[40] > 10:
        i17 = 'Low'



##########################################################################

    values[41] = values[41]*100
    if values[41] > 70:
        l1 = 'High'
    elif values[41] >= 35.1 and values[41] <= 70:
        l1 = 'Medium'
    elif values[41] >= 1 and values[41] <= 35:
        l1 = 'Low'


    if values[42] >= 66.1 and values[42] <= 100:
        l2 = 'High'
    elif values[42] >= 33.1 and values[42] <= 66:
        l2 = 'Medium'
    elif values[42] >= 1 and values[42] <= 33:
        l2 = 'Low'


    if values[43] >= 66.1 and values[43] <= 100:
        l3 = 'High'
    elif values[43] >= 33.1 and values[43] <= 66:
        l3 = 'Medium'
    elif values[43] >= 1 and values[43] <= 33:
        l3 = 'Low'


    values[44] = values[44]*100
    if values[44] >= 75:
        l4 = 'High'
    elif values[44] >= 37.6 and values[44] <= 75:
        l4 = 'Medium'
    elif values[44] >= 1 and values[44] <= 37.5:
        l4 = 'Low'


    values[45] = values[45]*100
    if values[45] >= 66.1 and values[45] <= 100:
        l5 = 'High'
    elif values[45] >= 33.1 and values[45] <= 66:
        l5 = 'Medium'
    elif values[45] >= 1 and values[45] <= 33:
        l5 = 'Low'


    values[46] = values[46]*100
    if values[46] >= 0 and values[46] <= 1:
        l6 = 'High'
    elif values[46] >= 1.1 and values[46] <= 2:
        l6 = 'Medium'
    elif values[46] > 2:
        l6 = 'Low'


    values[47] = values[47]*100
    if values[47] >= 0 and values[47] <= 2.59:
        l7 = 'High'
    elif values[47] >= 2.6 and values[47] <= 5:
        l7 = 'Medium'
    elif values[47] >= 5:
        l7 = 'Low'


    values[48] = values[48]*100
    if values[48] >= 66.1 and values[48] <= 100:
        l8 = 'High'
    elif values[48] >= 33.1 and values[48] <= 66:
        l8 = 'Medium'
    elif values[48] >= 1 and values[48] <= 33:
        l8 = 'Low'


    values[49] = int_features[98] - int_features[99]
    if values[49] >= 0 and values[49] <= 1.59:
        l9 = 'High'
    elif values[49] >= 1.6 and values[49] <= 3:
        l9 = 'Medium'
    elif values[49] >= 3:
        l9 = 'Low'


    values[50] = int_features[100] * int_features[101]
    if values[50] >= 20:
        l10 = 'High'
    elif values[50] >= 10.1 and values[50] <= 20:
        l10 = 'Medium'
    elif values[50] >= 1 and values[50] <= 10:
        l10 = 'Low'


    values[51] = values[51]*100
    if values[51] >= 0 and values[51] <= 1:
        l11 = 'High'
    elif values[51] >= 1.1 and values[51] <= 2:
        l11 = 'Medium'
    elif values[51] > 2:
        l11 = 'Low'

    


    return render(request, 'home.html', {"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"s":s,"t":t,"u":u,"v":v,"w":w,"x":x,
                                         "i1":i1,"i2":i2,"i3":i3,"i4":i4,"i5":i5,"i6":i6,"i7":i7,"i8":i8,"i9":i9,"i10":i10,"i11":i11,"i12":i12,"i13":i13,"i14":i14,"i15":i15,"i16":i16,"i17":i17,
                                         "l1":l1,"l2":l2,"l3":l3,"l4":l4,"l5":l5,"l6":l6,"l7":l7,"l8":l8,"l9":l9,"l10":l10,"l11":l11})

