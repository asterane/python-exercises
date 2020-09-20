{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(414, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuConvert',
             'label':'&Convert',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuConvertFtoC',
                   'label':'&Fahrenheit to Celsius',
                  },
                  {'type':'MenuItem',
                   'name':'menuConvertCtoF',
                   'label':'&Celsius to Fahrenheit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(292, 117), 
    'text':'Fahrenheit', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(36, 115), 
    'size':(33, 14), 
    'text':'Celsius', 
    },

{'type':'Spinner', 
    'name':'spinFahr', 
    'position':(265, 88), 
    'max':1000, 
    'min':-1000, 
    'value':0, 
    },

{'type':'TextField', 
    'name':'tfCel', 
    'position':(9, 85), 
    },

{'type':'Button', 
    'name':'btnFtoC', 
    'position':(114, 100), 
    'label':'<<< Fahrenheit to Celsius', 
    },

{'type':'Button', 
    'name':'btnCtoF', 
    'position':(113, 75), 
    'size':(-1, 22), 
    'label':'Celsius to Fahrenheit >>>', 
    },

] # end components
} # end background
] # end backgrounds
} }
