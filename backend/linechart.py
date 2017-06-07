# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

radius = range(2, 11, 1)

n3 = [0.016276741,
      0.029058862,
      0.085636699,
      0.091711426,
      0.196106696,
      0.192864549,
      0.235766315,
      0.315268302,
      0.421661913]

n4 = [0.014142346,
      0.035379541,
      0.063546205,
      0.071228421,
      0.188010442,
      0.337064815,
      0.288439417,
      0.522247076,
      0.516940439]

n5 = [0.016383326,
      0.043727791,
      0.058965909,
      0.106060505,
      0.16190685,
      0.432994926,
      0.351295412,
      0.623159075,
      0.582166827]

n6 = [0.014653862,
      0.04613421,
      0.075379837,
      0.081629765,
      0.197323585,
      0.280209374,
      0.35197475,
      0.554120958,
      0.690368271]

n7 = [0.021924758,
      0.076971459,
      0.091825044,
      0.182436454,
      0.186425698,
      0.322083163,
      0.377884984,
      0.577236032,
      0.600158274]

n8 = [0.024144757,
      0.044984221,
      0.076922607,
      0.10859338,
      0.221794713,
      0.324042702,
      0.628946567,
      0.894170415,
      0.817410147]

plt.plot(radius, n3, marker='o', linestyle='--', color='k', label='k=3')
plt.plot(radius, n4, marker=',', linestyle='--', color='g', label='k=4')
plt.plot(radius, n5, marker='.', linestyle='--', color='b', label='k=5')
plt.plot(radius, n6, marker='+', linestyle='--', color='r', label='k=6')
plt.plot(radius, n7, marker='x', linestyle='--', color='m', label='k=7')
plt.plot(radius, n8, marker='*', linestyle='--', color='y', label='k=8')
plt.xlabel('Number of query points', fontsize=20)
plt.ylabel('Query time', fontsize=20)
plt.xticks(np.arange(2, 11, 1))
# plt.yticks(np.arange(0.8, 1, 0.02))
# plt.title('Query with order restraint')
plt.legend()
plt.grid(True)
plt.show()

'''
n3 = [0.001487601, 0.016630685, 0.024340749, 0.023057306, 0.025396514, 0.0260952, 0.023756242, 0.026666129, 0.028610301,
      0.03223139, 0.034379208, 0.03708756, 0.03800379, 0.042188704, 0.043840563]
n5 = [0.001994658,
      0.069986367,
      0.073917532,
      0.092471111,
      0.129105949,
      0.105986857,
      0.116688859,
      0.149283648,
      0.126900756,
      0.160054159,
      0.142239654,
      0.158575404,
      0.164269125,
      0.156806731,
      0.190750551]
n7 = [0.002787173,
      0.173442173,
      0.28256427,
      0.369242716,
      0.306691849,
      0.321112669,
      0.383266997,
      0.366864443,
      0.421359241,
      0.450593841,
      0.460163236,
      0.534065735,
      0.627562177,
      0.605715787,
      0.717689979]
n9 = [0.002831674,
      0.283393216,
      0.287879491,
      0.371369839,
      0.443459642,
      0.505169868,
      0.494294,
      0.50528599,
      0.527722251,
      0.574234164,
      0.631705666,
      0.63706373,
      0.683395135,
      0.735476744,
      0.914077401]
      '''

'''
n3 = [0.002801311,
      0.024348438,
      0.034183848,
      0.032212198,
      0.037176764,
      0.039737689,
      0.04252342,
      0.049229431,
      0.065811336,
      0.059053612,
      0.071233475,
      0.059240353,
      0.067979157,
      0.07740109,
      0.071918643]
n5 = [0.002549851,
      0.066168964,
      0.088895321,
      0.08641454,
      0.111253607,
      0.117491984,
      0.113117313,
      0.137906611,
      0.157438076,
      0.16519506,
      0.197676098,
      0.196307731,
      0.1842996,
      0.231729329,
      0.223693967]
n7 = [0.002187777,
      0.220420444,
      0.303237987,
      0.36426791,
      0.368897116,
      0.39447974,
      0.418135428,
      0.448424077,
      0.437297273,
      0.485547125,
      0.49675349,
      0.559642231,
      0.587806308,
      0.636338925,
      0.765443397]
n9 = [0.00416686534882,
      0.274491751194,
      0.35971442461,
      0.491861712933,
      0.426585578918,
      0.572198104858,
      0.663222193718,
      0.675632619858,
      0.690891373158,
      0.567868959904,
      0.621867513657,
      0.663797199726,
      0.777584373951,
      0.739952254295,
      1.09999885559]
'''

# f3
'''
n3 = [0.021890414,
      0.026178896,
      0.047250175,
      0.095644343,
      0.101896667,
      0.241303194,
      0.300618017,
      0.309632242,
      0.306670201]
n4 = [
    0.018843377,
    0.03863728,
    0.068162298,
    0.056103027,
    0.172500896,
    0.319369841,
    0.307381141,
    0.364521551,
    0.524597383
]
n5 = [
    0.013465822,
    0.041370237,
    0.05742681,
    0.108433032,
    0.110176766,
    0.187552691,
    0.255442345,
    0.373998666,
    0.435675156
]
n6 = [
    0.029054284,
    0.040067446,
    0.050279403,
    0.132849872,
    0.154665017,
    0.200432622,
    0.270846522,
    0.419410479,
    0.497699106
]
n7 = [
    0.016842592,
    0.054663157,
    0.110079932,
    0.092386448,
    0.128165388,
    0.268464279,
    0.41053009,
    0.716375995,
    0.75073123
]
n8 = [
    0.0165017843246,
    0.041869699955,
    0.118467235565,
    0.230720829964,
    0.228949570656,
    0.472649979591,
    0.327817714214,
    0.741956841946,
    0.836182153225
]
'''

# f4
'''
n3 = [0.016276741,
      0.029058862,
      0.085636699,
      0.091711426,
      0.196106696,
      0.192864549,
      0.235766315,
      0.315268302,
      0.421661913]

n4 = [0.014142346,
      0.035379541,
      0.063546205,
      0.071228421,
      0.188010442,
      0.337064815,
      0.288439417,
      0.522247076,
      0.516940439]

n5 = [0.016383326,
      0.043727791,
      0.058965909,
      0.106060505,
      0.16190685,
      0.432994926,
      0.351295412,
      0.623159075,
      0.582166827]

n6 = [0.014653862,
      0.04613421,
      0.075379837,
      0.081629765,
      0.197323585,
      0.280209374,
      0.35197475,
      0.554120958,
      0.690368271]

n7 = [0.021924758,
      0.076971459,
      0.091825044,
      0.182436454,
      0.186425698,
      0.322083163,
      0.377884984,
      0.577236032,
      0.600158274]

n8 = [0.024144757,
      0.044984221,
      0.076922607,
      0.10859338,
      0.221794713,
      0.324042702,
      0.628946567,
      0.894170415,
      0.817410147]
'''

# a1 without order
'''
a3 = [0.990337506,
      0.988309031,
      0.986665411,
      0.985339912,
      0.983895763,
      0.982353999,
      0.980777027,
      0.978996645,
      0.977412226,
      0.976024563,
      0.974817025,
      0.973748279,
      0.97278422]

a5 = [0.991509833,
      0.989139764,
      0.98718774,
      0.985534638,
      0.984176632,
      0.982934564,
      0.981827412,
      0.980843778,
      0.979980462,
      0.979095951,
      0.978292733,
      0.97754225,
      0.976786809]

a7 = [0.988922789,
      0.985501688,
      0.983093307,
      0.981046584,
      0.979278186,
      0.977708653,
      0.976281958,
      0.975067456,
      0.9740128,
      0.973043607,
      0.972140164,
      0.971205879,
      0.970329132]

a9 = [0.986033606,
      0.983015396,
      0.979348659,
      0.976173494,
      0.973504912,
      0.97120573,
      0.969191886,
      0.967473173,
      0.965504268,
      0.963730976,
      0.962045534,
      0.960538729,
      0.959136635]

a11 = [0.98699765122,
       0.983439126545,
       0.980300614753,
       0.97714073482,
       0.974686117428,
       0.972730465337,
       0.971053849553,
       0.969452875491,
       0.967968934443,
       0.966578735629,
       0.965332809979,
       0.96416668452,
       0.963084838316]
'''
# a6 with order
'''
a3 = [0.819580512,
      0.820651181,
      0.811496999,
      0.799349758,
      0.787422147,
      0.77500168,
      0.780364561,
      0.772786561,
      0.754538286,
      0.741503326,
      0.727627217,
      0.73459869,
      0.656425611]

a5 = [0.871807588,
      0.864326021,
      0.858333373,
      0.856690331,
      0.853426722,
      0.854409781,
      0.853530017,
      0.850011035,
      0.846527538,
      0.843029469,
      0.83968693,
      0.838653401,
      0.836111148]

a7 = [0.903494149,
      0.900451844,
      0.896864301,
      0.894444988,
      0.892372419,
      0.890192877,
      0.888341677,
      0.886895274,
      0.885391912,
      0.883616604,
      0.882546205,
      0.881003778,
      0.879933236]

a9 = [0.884088669,
      0.879414659,
      0.87544339,
      0.87101921,
      0.866920916,
      0.863453441,
      0.860088475,
      0.85784707,
      0.854499698,
      0.851283274,
      0.847378754,
      0.843783869,
      0.837462369]

a11 = [0.909466807,
       0.904809731,
       0.901455267,
       0.898515556,
       0.895834914,
       0.89348298,
       0.891430287,
       0.889451154,
       0.887544577,
       0.885667827,
       0.883920565,
       0.882238991,
       0.880455865]
'''

# a7 without order
'''
a3 = [0.995064174,
0.994764951,
0.993283044,
0.991911798,
0.98854427,
0.990477992,
0.989470517,
0.985141973,
0.988674613]

a4 = [0.99215443,
0.993076436,
0.99348538,
0.988766267,
0.988685052,
0.984385921,
0.98644352,
0.981516625,
0.982334676]

a5 = [0.991214657,
0.990950458,
0.990239104,
0.991469908,
0.982195863,
0.990661625,
0.979603437,
0.980011908,
0.978649766]

a6 = [0.989187555,
0.989789457,
0.986604135,
0.985567981,
0.983925961,
0.984388715,
0.976648069,
0.979107381,
0.977991656]

a7 = [0.982413049,
0.983680959,
0.98060858,
0.985182327,
0.985919518,
0.982710623,
0.973110776,
0.968226751,
0.969141293]

a8 = [0.987353525,
0.98191155,
0.989901368,
0.983051771,
0.98373131,
0.976081951,
0.974269315,
0.981514194,
0.970942847]
'''

# a8 with order
'''
a3 = [0.720151726,
0.780562938,
0.871524578,
0.893405924,
0.860837963,
0.878480317,
0.904762673,
0.895000178,
0.894889403]

a4 = [0.818070984,
0.871087679,
0.825885848,
0.852094539,
0.879105842,
0.886744625,
0.886795871,
0.893122485,
0.893036107]

a5 = [0.768926613,
0.8776249,
0.853970657,
0.870867506,
0.861034337,
0.886632126,
0.895064001,
0.878062616,
0.8819663]

a6 = [0.761582309,
0.831152502,
0.854412081,
0.851286851,
0.868536635,
0.856799424,
0.879388846,
0.876604132,
0.884896405]

a7 = [0.817125595,
0.83133689,
0.847498387,
0.847847598,
0.8158568,
0.884976226,
0.883631695,
0.871397759,
0.863155979]

a8 = [0.836727631,
0.842567871,
0.856920497,
0.84165584,
0.86628226,
0.857483146,
0.866025672,
0.878763431,
0.878091619]
'''
