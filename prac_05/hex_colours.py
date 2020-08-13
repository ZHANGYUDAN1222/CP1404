color_to_name={"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2",
               "brown": "#a52a2a", "burlywood": "#deb887", "cadetblue": "#5f9ea0", "chocolate": "#d2691e", "darkgoldenrod": "#b8860b"}
while True:
    color_name=input('Input a color name:').lower()
    if color_name=='':
        break
    elif color_name in color_to_name:
        print('The code for %s is: %s'%(color_name,color_to_name[color_name]))
    else:
        print('Invalid name.')