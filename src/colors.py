#!/usr/bin/env python

import math
from i18n import I18n


class EnumColor:
    class Color(object):
        def __init__(self, index, name, rgb):
            self.name = name
            self.rgb = rgb
            self.index = index
    
    ENUM = [
        Color(0,    'white',            (255,255,255)),
        Color(1,    'gainsboro',        (228,228,228)),
        Color(2,    'grey',             (136,136,136)),
        Color(3,    'nero',             ( 34, 34, 34)),
        Color(4,    'carnation pink',   (255,167,209)),
        Color(5,    'red',              (229,  0,  0)),
        Color(6,    'orange',           (229,149,  0)),
        Color(7,    'brown',            (160,106, 66)),
        Color(8,    'yellow',           (229,217,  0)),
        Color(9,    'conifer',          (148,224, 68)),
        Color(10,   'green',            (  2,190,  1)),
        Color(11,   'dark turquoise',   (  0,211,221)),
        Color(12,   'pacific blue',     (  0,131,199)),
        Color(13,   'blue',             (  0,  0,234)),
        Color(14,   'violet',           (207,110,228)),
        Color(15,   'purple',           (130,  0,128))
    ]

    
    
    @staticmethod
    def index(i):
        for color in EnumColor.ENUM:
            if i == color.index:
                return color
        #White is default color
        return EnumColor.ENUM[0]

    @staticmethod
    def rgb(rgb, silent = False):
        for color in EnumColor.ENUM:
            if rgb == color.rgb:
                return color

        #if that colors not in standart colors list
        diff_min = [(255,255,255), 441.7] # sqrt(255*255 + 255*255 + 255*255) = 441.67295593 --> Default white

        for color in EnumColor.ENUM:
            #formula that sqrt( (x1 - x2)2 + (y1 - y2)2 + (z1 - z2)2 )
            diffys = math.sqrt( (rgb[0] - color.rgb[0]) * (rgb[0] - color.rgb[0]) + (rgb[1] - color.rgb[1]) * (rgb[1] - color.rgb[1]) + (rgb[2] - color.rgb[2]) * (rgb[2] - color.rgb[2]))

            if diffys < diff_min[1]:
                diff_min[1] = diffys
                diff_min[0] = color.rgb

        #return rounding colour

        if not silent:
            print(I18n.get(' %s colours rounded %s (%s) ') % (str(rgb) , str(diff_min[0]), I18n.get(str(EnumColor.rgb(diff_min[0]).name), 'true')))
        return EnumColor.rgb(diff_min[0])