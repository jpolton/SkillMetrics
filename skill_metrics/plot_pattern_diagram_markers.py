from skill_metrics.get_from_dict_or_default import get_from_dict_or_default
from skill_metrics import add_legend
import matplotlib.colors as clr
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import warnings

def plot_pattern_diagram_markers(ax: matplotlib.axes.Axes, X, Y, option: dict):
    '''
    Plots color markers on a pattern diagram in the provided subplot axis.
    
    Plots color markers on a target diagram according their (X,Y) 
    locations. The symbols and colors are chosen automatically with a 
    limit of 70 symbol & color combinations.
    
    The color bar is titled using the content of option['titleColorBar'] 
    (if non-empty string).

    It is a direct adaptation of the plot_pattern_diagram_markers() function
    for the scenario in which the Taylor diagram is draw in an
    matplotlib.axes.Axes object.
    
    INPUTS:
    ax     : the matplotlib.axes.Axes to receive the plot
    x      : x-coordinates of markers
    y      : y-coordinates of markers
    z      : z-coordinates of markers (used for color shading)
    option : dictionary containing option values. (Refer to 
        GET_TARGET_DIAGRAM_OPTIONS function for more information.)
    option['axismax'] : maximum for the X & Y values. Used to limit
        maximum distance from origin to display markers
    option['markerlabel'] : labels for markers
    
    OUTPUTS:
    None

    Authors:
    Peter A. Rochford
    rochford.peter1@gmail.com

    Andre D. L. Zanchetta (adapting Peter A. Rochford's code)
        adlzanchetta@gmail.com

    Created on Nov 30, 2016
    Revised on Aug 14, 2022
    '''

    # Set face color transparency
    alpha = option['alpha']
    
    # Set font and marker size
    fontSize = matplotlib.rcParams.get('font.size') - 2
    markerSize = option['markersize']
    
    """
    # Check enough labels provided if markerlabel provided
    numberLabel = len(option['markerlabel'])
    if numberLabel > 0:
        if isinstance(option['markerlabel'], list) and numberLabel < len(X):
            raise ValueError('Insufficient number of marker labels provided.\n' +
                             'target: No. labels=' + str(numberLabel) + ' < No. markers=' +
                             str(len(X)) + '\n' +
                             'taylor: No. labels=' + str(numberLabel+1) + ' < No. markers=' +
                             str(len(X)+1))
        elif isinstance(option['markerlabel'], dict) and numberLabel > 70:
            raise ValueError('Insufficient number of marker labels provided.\n' +
                             'target: No. labels=' + str(numberLabel) + ' > No. markers= 70')
    """
    if option['markerlegend'] == 'on':
        # Check that marker labels have been provided
        if option['markerlabel'] == '':
            raise ValueError('No marker labels provided.')

        # Plot markers of different color and shapes with labels displayed in a legend
        
        # Define markers
        kind = ['+','o','x','s','d','^','v','p','h','*']
        colorm = ['r','b','g','c','m','y','k','gray']
        if len(X) > 80:
            _disp('You must introduce new markers to plot more than 70 cases.')
            _disp('The ''marker'' character array need to be extended inside the code.')
        
        if len(X) <= len(kind):
            # Define markers with specified color
            marker = []
            markercolor = []
            if option['markercolor'] is None:
                for i, color in enumerate(colorm):
                    rgba = clr.to_rgb(color) + (alpha,)
                    marker.append(kind[i] + color)
                    markercolor.append(rgba)
            else:
                rgba = clr.to_rgb(option['markercolor']) + (alpha,)
                for symbol in kind:
                    marker.append(symbol + option['markercolor'])
                    markercolor.append(rgba)
        else:
            # Define markers and colors using predefined list
            marker = []
            markercolor = [] #Bug Fix: missing array initialization
            for color in colorm:
                for symbol in kind:
                    marker.append(symbol + color)
                    rgba = clr.to_rgb(color) + (alpha,)
                    markercolor.append(rgba)
        
        # Plot markers at data points
        limit = option['axismax']
        hp = ()
        markerlabel = []
        for i, xval in enumerate(X):
            if abs(X[i]) <= limit and abs(Y[i]) <= limit:
                h = ax.plot(X[i],Y[i],marker[i], markersize = markerSize,
                     markerfacecolor = markercolor[i],
                     markeredgecolor = markercolor[i][0:3] + (1.0,),
                     markeredgewidth = 2)
                hp += tuple(h)
                markerlabel.append(option['markerlabel'][i])

        # Add legend
        if len(markerlabel) == 0:
            warnings.warn('No markers within axis limit ranges.')
        else:
            add_legend(markerlabel, option, rgba, markerSize, fontSize, hp)
    """
    else:
        # Plot markers as dots of a single color with accompanying labels
        # and no legend
        
        # Plot markers at data points
        limit = option['axismax']

        # Define edge and face colors of the markers
        edge_color = get_from_dict_or_default(option, 'markercolor', 'markercolors', 'edge')
        if edge_color is None: edge_color = 'r'
        face_color = get_from_dict_or_default(option, 'markercolor', 'markercolors', 'face')
        if face_color is None: face_color = edge_color
        face_color = clr.to_rgb(face_color) + (alpha,)

        for i in range(len(X)):
            xval, yval = X[i], Y[i]
            if abs(xval) <= limit and abs(yval) <= limit:
                # Plot marker
                ax.plot(xval, yval, option['markersymbol'],
                        markersize=markerSize,
                        markerfacecolor=face_color,
                        markeredgecolor=edge_color)
                
                # Check if marker labels provided
                if type(option['markerlabel']) is list:
                    # Label marker
                    ax.text(xval, yval, option['markerlabel'][i],
                            color=option['markerlabelcolor'],
                            verticalalignment='bottom',
                            horizontalalignment='right',
                            fontsize=fontSize)
            del i, xval, yval

        # Add legend if labels provided as dictionary
        markerlabel = option['markerlabel']
        marker_label_color = clr.to_rgb(edge_color) + (alpha,)
        if type(markerlabel) is dict:
            add_legend(markerlabel, option, marker_label_color, markerSize, fontSize)
    """

    if option['markerdictch'] != None:
    # markerlabels for legend. plot markers

        markerlabel = []

        # create list from dict
        colmar = []  # colmar for color (belonging to a marker)
        markcol = []  # markcol for marker (belonging to a climate model)
        edgecol = []  # edgecolors for forcings
        hp = ()  # for handles

        for idx1, mar in enumerate(option['markerdictch'].keys()):

            for forcing in option['markerdictch'][mar].keys():
                for idx2, col in enumerate(option['markerdictch'][mar][forcing]):
                    # print(col)
                    colmar.append(col)
                    markcol.append(mar)
                    if forcing == 'w':
                        edgecol.append(col)  # do not use white edgecolor. Just use same color as markercolor
                    else:
                        edgecol.append(forcing)

                    # this is for legend
                    # idx2 == 0 is there so that we take only one color

                    # case where we have only model data, no ERA5 data (ERA5 is reference)
                    if idx1 == 0 and idx2 == 0 and mar != '*':
                        if forcing == 'w':  # do not use white edgecolor
                            my_edge_col = col
                        else:
                            my_edge_col = forcing
                        mark = mlines.Line2D([], [], color=col, marker=mar, markeredgecolor=my_edge_col,
                                             markersize=markerSize)
                        hp += tuple([mark])
                        rgba = clr.to_rgb('k') + (alpha,)  # not really needed, but otherwise rgba is not defined for add_legend

                    # case where we have ERA5 data
                    # make sure that we only run this code if ERA5 is NOT the reference, so if the marker of ERA5 ('*') is in the markerdict
                    if '*' in option['markerdictch'].keys():
                        if idx1 == 1 and idx2 == 0:  # take second entry for displaying forcing, since ERA5 is reanalysis and has no different forcings
                            # markerlabel.append(option['markerlabel'][i]) # only plot legend of markers, which indicate climate model
                            if forcing == 'w':  # do not use white edgecolor
                                my_edge_col = col
                            else:
                                my_edge_col = forcing
                            mark = mlines.Line2D([], [], color=col, marker=mar, markeredgecolor=my_edge_col,
                                                 markersize=markerSize)
                            hp += tuple([mark])
                            rgba = clr.to_rgb('k') + (
                            alpha,)  # not really needed, but otherwise rgba is not defined for add_legend

        # # markerlabels for legend. plot markers
        # markerlabel = []

        # # create list from dict
        # colmar = [] # colmar for color (belonging to a marker)
        # markcol = [] # markcol for marker (belonging to a climate model)
        # hp = () # for handles
        # for mar in option['markerdictch'].keys():
        #     # markerlabel.append(option['markerlabel'][i]) # only plot legend of markers, which indicate climate model
        #     mark = mlines.Line2D([], [], color='k', marker=mar, # edgecolor
        #                   markersize=markerSize)
        #     hp += tuple([mark])
        #     rgba = clr.to_rgb('k') + (alpha,) # not really needed, but otherwise rgba is not defined for add_legend

        #     for col in option['markerdictch'][mar]:
        #         colmar.append(col)
        #         markcol.append(mar)


        # print(f'len of X: {len(X)}, len of Y: {len(Y)}, len of colmar: {len(colmar)}, len of markcol: {len(markcol)}, len of edgecol: {len(edgecol)}')

        # Add legend for forcings
        # only useful if not only ERA5 data is in it
        if len(hp) != 0:
            if len(option['markerlabel']) == 0:
                warnings.warn('No markers within axis limit ranges.')
            else:

                for h in hp: h.set_linestyle("")  # Caroline: do not display lines
                add_legend(option['markerlabel'], option, rgba, markerSize, fontSize, hp)

        # Plot markers at data points

        limit = option['axismax']
        # hp = ()

        # CH made some changes below
        print(X)
        for i, xval in enumerate(X):
            if abs(X[i]) <= limit and abs(Y[i]) <= limit:
                # print(i)
                # print(X[i])
                # print(Y[i])
                # print(colmar[i])
                # print(markcol[i])
                # print(edgecol[i])
                h = plt.plot(X[i], Y[i], color=colmar[i], marker=markcol[i], markersize=markerSize,
                             # markerfacecolor = markercolor[i],
                             markeredgecolor=edgecol[i],
                             markeredgewidth=1.2, alpha=0.7)
                # hp += tuple(h)


        # Add legend
        # if len(option['markerlabel']) == 0:
        #     warnings.warn('No markers within axis limit ranges.')
        # else:

        #     for h in hp: h.set_linestyle("") # Caroline: do not display lines
        #     add_legend(option['markerlabel'], option, rgba, markerSize, fontSize, hp)

        # add title (doesn't work properly)
        # plt.title('Taylor diagram (Frequency = Monthly)')

def _disp(text):
    print(text)
