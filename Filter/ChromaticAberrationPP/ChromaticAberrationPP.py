# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ChromaticAberrationPPExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ChromaticAberrationPPExt import *
except ImportError:
    pass

def getPluginID():
    return "PostPollux.ChromaticAberration"

def getLabel():
    return "ChromaticAberrationPP"

def getVersion():
    return 1

def getIconPath():
    return "ChromaticAberrationPP.png"

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "This PyPlug mimics the optical effect called \"chromatic aberration\".\n\nIt occurs because lenses have different refractive indices for different wave lengths of light (also known as: dispersion) resulting in different convergence points for each wave length.\nNormally this is an unwanted effect which the producers of lens systems try to minimize as much as possible. But if used subtly, it can help cg elements to look a bit more naturally and of course it can be used as a nice effect for motion graphics.\n\nActually there are two types of chromatic aberration:\n1. Axial Chromatic Aberration\nThe axial chromatic abberation occurs because parallel incoming light of different wavelengths is focused on different planes. (As long as the lenses are not corrected) So the green image may be sharp, because it\'s focus is perfectly aligned with the photosensor, but the blue and the red image might be a bit blurred, because their focus can be slightly off.\nThis kind of chromatic aberration is present all over the image. It\'s noticable especially at the high contrast areas.\n\n2. Lateral Chromatic Aberration\nThe lateral chromatic aberration will only occure at the periphery of the image. If light falls in from an angle the dispersion causes the light of different wave lengths to focus at different points on the sensor/film. This results in slightly shifted color channels at the periphery, if the lens is not corrected."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.controls = lastNode.createPageParam("controls", "Controls")
    param = lastNode.createGroupParam("LateralChromaticAberrationGroup", "Lateral Chr. Aberration")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Lateral chromatic abberration will only occure at the periphery of the image. If light falls in from an angle the dispersion causes the light of different wave lengths to focus at different points on the sensor/film. This results in slightly shifted color channels at the periphery, if the lens is not corrected. As the refractive index for blue light is higher than for red, blue will be shifted outwards more then red.")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setOpened(True)
    lastNode.LateralChromaticAberrationGroup = param
    del param

    param = lastNode.createDoubleParam("KOne", "K1")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-0.02, 0)
    param.setDisplayMaximum(0.02, 0)
    param.setDefaultValue(0.005, 0)
    param.restoreDefaultValue(0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("First radial distortion coefficient (coefficient for r^2)\n\n\nIn order to get a lateral chromatic aberration effect the channels are distorted as following:\n\nred -> +K1\ngreen -> no distortion\nblue -> -K1\n\nIf \"distort outwards only\" is active, it\'s:\n\nred -> no distortion\ngreen -> K1\nblue -> K1 * 2")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.KOne = param
    del param

    param = lastNode.createDoubleParam("KTwo", "K2")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-0.02, 0)
    param.setDisplayMaximum(0.02, 0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("Second radial distortion coefficient (coefficient for r^4)\n\n\nIn order to get a lateral chromatic aberration effect the channels are distorted as following:\n\nred -> +K2\ngreen -> no distortion\nblue -> -K2\n\nIf \"distort outwards only\" is active, it\'s:\n\nred -> no distortion\ngreen -> K2\nblue -> K2 * 2")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.KTwo = param
    del param

    param = lastNode.createDoubleParam("assymetric", "Assymetric")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-0.04, 0)
    param.setDisplayMaximum(0.04, 0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("Assymetric distortion. (only for anamorphic lenses)")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.assymetric = param
    del param

    param = lastNode.createDoubleParam("adjustRedChannel", "adjust red channel")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-1.5, 0)
    param.setDisplayMaximum(1.5, 0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("Finetune only the distortion of the red channel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.adjustRedChannel = param
    del param

    param = lastNode.createDoubleParam("adjustBlueChannel", "adjust blue/green channel")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-1.5, 0)
    param.setDisplayMaximum(1.5, 0)
    param.setDefaultValue(0.75, 0)
    param.restoreDefaultValue(0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("Finetune only the distortion of the blue channel.\n\nIf \"distort outwards only\" is active, this will finetune the distortion of the green channel instead.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.adjustBlueChannel = param
    del param

    param = lastNode.createDoubleParam("intensify", "Intensify")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("This value basically multiplies everything, so that the effect is more visible.\n\nThe ranges of the sliders above are pretty small to ensure really fine tuning for realistic results.\n\nHowever, if you want to do motion graphics and therefore need an exaggerated effect, this slider comes in handy. ")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.intensify = param
    del param

    param = lastNode.createBooleanParam("distOutwardsOnly", "distort outwards only")

    # Add the param to the group, no need to add it to the page
    lastNode.LateralChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("If checked, no channel will be distorted inwards. Instead of distorting blue inwards and red outwards, both red and green will be distorted outwards.\n\nA distortion inwards leads to the repetition of the border pixels, because there is no image information outside those borders. This is especially noticable with a strong chromatic aberration effect.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.distOutwardsOnly = param
    del param

    param = lastNode.createSeparatorParam("separator1", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.separator1 = param
    del param

    param = lastNode.createGroupParam("AxialChromaticAberrationGroup", "Axial Chr. Abberation")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("Axial chromatic abberation occurs because parallel incoming light of different wavelengths is focused on different planes. (As long as the lenses are not corrected) So the green image may be sharp, because it\'s focus is perfectly aligned with the photosensor, but the blue and the red image might be a bit blurred, because their focus can be slightly off.\nThis kind of chromatic aberration is present all over the image. It\'s noticable especially at the high contrast areas.")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setOpened(True)
    lastNode.AxialChromaticAberrationGroup = param
    del param

    param = lastNode.createDoubleParam("blurSize", "blur size")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(25, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the group, no need to add it to the page
    lastNode.AxialChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("Blur red and  blue channel by this value")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.blurSize = param
    del param

    param = lastNode.createDoubleParam("spread", "Spread")
    param.setMinimum(-1, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(-1, 0)
    param.setDisplayMaximum(1, 0)

    # Add the param to the group, no need to add it to the page
    lastNode.AxialChromaticAberrationGroup.addParam(param)

    # Set param properties
    param.setHelp("The spread value controls how different the blur sizes of the red- and the blue-channel are.\n\n 0   ->  Both blurs are the same.\n-1   ->  red blur will be three times as big as blue\n 1   ->  blue blur will be three times as big as red\n\nChanging the \"Spread\" value is like shifting the red and blue focus a bit.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.spread = param
    del param

    param = lastNode.createSeparatorParam("separator2", "")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.separator2 = param
    del param

    param = lastNode.createBooleanParam("applyOnAlpha", "Apply on Alpha")

    # Add the param to the page
    lastNode.controls.addParam(param)

    # Set param properties
    param.setHelp("If checked, the lens distortion and the blur will also affect the alpha channel.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.applyOnAlpha = param
    del param

    lastNode.userNatron = lastNode.createPageParam("userNatron", "User")
    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['controls', 'Node', 'Settings', 'Info', 'userNatron'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "LensDist_r"
    lastNode = app.createNode("net.sf.openfx.LensDistortion", 2, group)
    lastNode.setScriptName("LensDist_r")
    lastNode.setLabel("LensDist_r")
    lastNode.setPosition(545, 332)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupLensDist_r = lastNode

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("k1")
    if param is not None:
        param.setValue(0.005, 0)
        del param

    param = lastNode.getParam("k2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("asymmetricDistortion")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "LensDist_r"

    # Start of node "LensDist_b"
    lastNode = app.createNode("net.sf.openfx.LensDistortion", 2, group)
    lastNode.setScriptName("LensDist_b")
    lastNode.setLabel("LensDist_b")
    lastNode.setPosition(996, 334)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupLensDist_b = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("k1")
    if param is not None:
        param.setValue(-0.00125, 0)
        del param

    param = lastNode.getParam("k2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("asymmetricDistortion")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "LensDist_b"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(820, 231)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(1041, 231)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(590, 231)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "combine1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("combine1")
    lastNode.setLabel("combine1")
    lastNode.setPosition(775, 547)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupcombine1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGB")
        del param

    param = lastNode.getParam("outputComponents")
    if param is not None:
        param.set("RGB")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.g")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("B.g")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("0")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("0")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.a")
        del param

    del lastNode
    # End of node "combine1"

    # Start of node "combine2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("combine2")
    lastNode.setLabel("combine2")
    lastNode.setPosition(775, 669)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupcombine2 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGB")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.b")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("B.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.a")
        del param

    del lastNode
    # End of node "combine2"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(592, 561)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(1041, 683)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(775, -87)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(773, 1376)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "CopyAlpha"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("CopyAlpha")
    lastNode.setLabel("CopyAlpha")
    lastNode.setPosition(775, 817)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupCopyAlpha = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.a")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("B.a")
        del param

    del lastNode
    # End of node "CopyAlpha"

    # Start of node "Dot7"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot7")
    lastNode.setLabel("Dot7")
    lastNode.setPosition(820, 158)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot7 = lastNode

    del lastNode
    # End of node "Dot7"

    # Start of node "Dot8"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot8")
    lastNode.setLabel("Dot8")
    lastNode.setPosition(1214, 158)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot8 = lastNode

    del lastNode
    # End of node "Dot8"

    # Start of node "Dot9"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot9")
    lastNode.setLabel("Dot9")
    lastNode.setPosition(1054, 748)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot9 = lastNode

    del lastNode
    # End of node "Dot9"

    # Start of node "Blur_r"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 3, group)
    lastNode.setScriptName("Blur_r")
    lastNode.setLabel("Blur_r")
    lastNode.setPosition(547, 444)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_r = lastNode

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur_r"

    # Start of node "Blur_b"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 3, group)
    lastNode.setScriptName("Blur_b")
    lastNode.setLabel("Blur_b")
    lastNode.setPosition(996, 441)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur_b = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Blur_b"

    # Start of node "LensDist_g"
    lastNode = app.createNode("net.sf.openfx.LensDistortion", 2, group)
    lastNode.setScriptName("LensDist_g")
    lastNode.setLabel("LensDist_g")
    lastNode.setPosition(775, 335)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupLensDist_g = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("k1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("k2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("asymmetricDistortion")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    del lastNode
    # End of node "LensDist_g"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(773, 1121)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(copy)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("mask")
    lastNode.setLabel("mask")
    lastNode.setPosition(963, 1133)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupmask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "mask"

    # Start of node "Dot10"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot10")
    lastNode.setLabel("Dot10")
    lastNode.setPosition(419, 1147)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot10 = lastNode

    del lastNode
    # End of node "Dot10"

    # Start of node "Dot11"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot11")
    lastNode.setLabel("Dot11")
    lastNode.setPosition(590, 409)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot11 = lastNode

    del lastNode
    # End of node "Dot11"

    # Start of node "Dot12"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot12")
    lastNode.setLabel("Dot12")
    lastNode.setPosition(421, 158)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot12 = lastNode

    del lastNode
    # End of node "Dot12"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(1361, 627)
    lastNode.setSize(104, 74)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("max")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("max")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(max)</Natron>")
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Clamp1"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp1")
    lastNode.setLabel("Clamp1")
    lastNode.setPosition(1361, 815)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp1 = lastNode

    param = lastNode.getParam("premult")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("premultChanged")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Clamp1"

    # Start of node "apply_on_alpha"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("apply_on_alpha")
    lastNode.setLabel("apply on alpha")
    lastNode.setPosition(1009, 815)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupapply_on_alpha = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "apply_on_alpha"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(1214, 748)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Dot13"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot13")
    lastNode.setLabel("Dot13")
    lastNode.setPosition(1406, 455)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot13 = lastNode

    del lastNode
    # End of node "Dot13"

    # Start of node "Dot14"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot14")
    lastNode.setLabel("Dot14")
    lastNode.setPosition(820, 489)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot14 = lastNode

    del lastNode
    # End of node "Dot14"

    # Start of node "Dot15"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot15")
    lastNode.setLabel("Dot15")
    lastNode.setPosition(1370, 489)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot15 = lastNode

    del lastNode
    # End of node "Dot15"

    # Start of node "Dot16"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot16")
    lastNode.setLabel("Dot16")
    lastNode.setPosition(592, 509)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot16 = lastNode

    del lastNode
    # End of node "Dot16"

    # Start of node "Dot17"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot17")
    lastNode.setLabel("Dot17")
    lastNode.setPosition(1341, 509)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot17 = lastNode

    del lastNode
    # End of node "Dot17"

    # Now that all nodes are created we can connect them together, restore expressions
    groupLensDist_r.connectInput(0, groupDot3)
    groupLensDist_b.connectInput(0, groupDot2)
    groupDot1.connectInput(0, groupDot7)
    groupDot2.connectInput(0, groupDot1)
    groupDot3.connectInput(0, groupDot1)
    groupcombine1.connectInput(0, groupDot14)
    groupcombine1.connectInput(1, groupDot4)
    groupcombine2.connectInput(0, groupDot5)
    groupcombine2.connectInput(1, groupcombine1)
    groupDot4.connectInput(0, groupDot16)
    groupDot5.connectInput(0, groupBlur_b)
    groupOutput1.connectInput(0, groupMerge1)
    groupCopyAlpha.connectInput(0, groupapply_on_alpha)
    groupCopyAlpha.connectInput(1, groupcombine2)
    groupDot7.connectInput(0, groupInput1)
    groupDot8.connectInput(0, groupDot7)
    groupDot9.connectInput(0, groupDot6)
    groupBlur_r.connectInput(0, groupDot11)
    groupBlur_b.connectInput(0, groupLensDist_b)
    groupLensDist_g.connectInput(0, groupDot1)
    groupMerge1.connectInput(0, groupDot10)
    groupMerge1.connectInput(1, groupCopyAlpha)
    groupMerge1.connectInput(2, groupmask)
    groupDot10.connectInput(0, groupDot12)
    groupDot11.connectInput(0, groupLensDist_r)
    groupDot12.connectInput(0, groupDot7)
    groupMerge2.connectInput(0, groupDot15)
    groupMerge2.connectInput(1, groupDot17)
    groupMerge2.connectInput(3, groupDot13)
    groupClamp1.connectInput(0, groupMerge2)
    groupapply_on_alpha.connectInput(0, groupDot9)
    groupapply_on_alpha.connectInput(1, groupClamp1)
    groupDot6.connectInput(0, groupDot8)
    groupDot13.connectInput(0, groupBlur_b)
    groupDot14.connectInput(0, groupLensDist_g)
    groupDot15.connectInput(0, groupDot14)
    groupDot16.connectInput(0, groupBlur_r)
    groupDot17.connectInput(0, groupDot16)

    param = groupLensDist_r.getParam("k1")
    param.setExpression("k1 = thisGroup.KOne.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustRedChannel = thisGroup.adjustRedChannel.get()\nif outwardsOnly:\n\tret = abs(k1*2*mult + k1*2*mult*adjustRedChannel)\nelse:\n\tret = k1*mult + k1*mult*adjustRedChannel\n", True, 0)
    del param
    param = groupLensDist_r.getParam("k2")
    param.setExpression("k2 = thisGroup.KTwo.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustRedChannel = thisGroup.adjustRedChannel.get()\nif outwardsOnly:\n\tret = abs(k2*2*mult + k2*2*mult*adjustRedChannel)\nelse:\n\tret = k2*mult + k2*mult*adjustRedChannel", True, 0)
    del param
    param = groupLensDist_r.getParam("asymmetricDistortion")
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustRedChannel = thisGroup.adjustRedChannel.get()\nif outwardsOnly:\n\tret = 0\nelse:\n\tret = assymetric*mult + assymetric*mult*adjustRedChannel", True, 0)
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustRedChannel = thisGroup.adjustRedChannel.get()\nif outwardsOnly:\n\tret = 0\nelse:\n\tret = assymetric*mult + assymetric*mult*adjustRedChannel", True, 1)
    del param
    param = groupLensDist_b.getParam("k1")
    param.setExpression("k1 = thisGroup.KOne.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustBlueChannel = thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  0\nelse:\n\tret = -k1*mult + k1*mult*adjustBlueChannel", True, 0)
    del param
    param = groupLensDist_b.getParam("k2")
    param.setExpression("k2 = thisGroup.KTwo.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustBlueChannel = thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  0\nelse:\n\tret = -k2*mult + k2*mult*adjustBlueChannel", True, 0)
    del param
    param = groupLensDist_b.getParam("asymmetricDistortion")
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustBlueChannel = thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  abs(assymetric*2*mult + assymetric*2*mult*adjustBlueChannel)\nelse:\n\tret = -assymetric*mult + assymetric*mult*adjustBlueChannel", True, 0)
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustBlueChannel = thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  abs(assymetric*2*mult + assymetric*2*mult*adjustBlueChannel)\nelse:\n\tret = -assymetric*mult + assymetric*mult*adjustBlueChannel", True, 1)
    del param
    param = groupBlur_r.getParam("size")
    param.setExpression("thisGroup.blurSize.get()+-thisGroup.spread.get()*thisGroup.blurSize.get()*0.5", False, 0)
    param.setExpression("thisGroup.blurSize.get()+-thisGroup.spread.get()*thisGroup.blurSize.get()*0.5", False, 1)
    del param
    param = groupBlur_b.getParam("size")
    param.setExpression("thisGroup.blurSize.get()+thisGroup.spread.get()*thisGroup.blurSize.get()*0.5", False, 0)
    param.setExpression("thisGroup.blurSize.get()+thisGroup.spread.get()*thisGroup.blurSize.get()*0.5", False, 1)
    del param
    param = groupLensDist_g.getParam("k1")
    param.setExpression("k1 = thisGroup.KOne.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustGreenChannel = -thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret = abs(k1*mult + k1*mult*adjustGreenChannel)\nelse:\n\tret = 0", True, 0)
    del param
    param = groupLensDist_g.getParam("k2")
    param.setExpression("k2 = thisGroup.KTwo.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustGreenChannel = -thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret = abs(k2*mult + k2*mult*adjustGreenChannel)\nelse:\n\tret = 0", True, 0)
    del param
    param = groupLensDist_g.getParam("asymmetricDistortion")
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustGreenChannel = -thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  abs(assymetric*mult+ assymetric*mult*adjustGreenChannel)\nelse:\n\tret = 0", True, 0)
    param.setExpression("assymetric = thisGroup.assymetric.get()\nmult = thisGroup.intensify.get()\noutwardsOnly = thisGroup.distOutwardsOnly.get()\nadjustGreenChannel = -thisGroup.adjustBlueChannel.get()\nif outwardsOnly:\n\tret =  abs(assymetric*mult+ assymetric*mult*adjustGreenChannel)\nelse:\n\tret = 0", True, 1)
    del param
    param = groupapply_on_alpha.getParam("which")
    param.setExpression("thisGroup.applyOnAlpha.get()", False, 0)
    del param

    try:
        extModule = sys.modules["ChromaticAberrationPPExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
