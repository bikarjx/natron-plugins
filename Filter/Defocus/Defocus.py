# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named DefocusExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from DefocusExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Defocus"

def getLabel():
    return "Defocus"

def getVersion():
    return 1.2

def getIconPath():
    return "Defocus.png"

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "Add a bokeh blur to the image. You can use an image to guide blur size. \nIt\'s not suited to act as a ZBlur plugin ( to fake DOF using a Zpass ) . But in some cases it can work.\nTypicall use case can be to blur the bakground image in a composite to match the blur of the foreground.\n\nCredits : \nOrginal Shader by David Hoskins\nLicense Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.\nhttps://www.shadertoy.com/view/4d2Xzw"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createDoubleParam("DefocusparamValueFloat0", "Blur radius")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.5, 0)
    lastNode.DefocusparamValueFloat0 = param
    del param

    param = lastNode.createDoubleParam("DefocusparamValueFloat1", "Image Contrast")
    param.setMinimum(0.1000000014901161, 0)
    param.setMaximum(10, 0)
    param.setDisplayMinimum(0.1000000014901161, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.DefocusparamValueFloat1 = param
    del param

    param = lastNode.createIntParam("DefocusparamValueInt2", "Samples")
    param.setMinimum(64, 0)
    param.setMaximum(1024, 0)
    param.setDisplayMinimum(64, 0)
    param.setDisplayMaximum(1024, 0)
    param.setDefaultValue(256, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.DefocusparamValueInt2 = param
    del param

    param = lastNode.createChoiceParam("Shuffle1outputA", "ZChannel")
    param.setDefaultValue(3)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.Shuffle1outputA = param
    del param

    param = lastNode.createSeparatorParam("sep", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep = param
    del param

    param = lastNode.createBooleanParam("Merge1enableMask_Mask", "Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Merge1enableMask_Mask = param
    del param

    param = lastNode.createChoiceParam("Merge1maskChannel_Mask", "")
    param.setDefaultValue(4)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Merge1maskChannel_Mask = param
    del param

    param = lastNode.createBooleanParam("Merge1maskInvert", "Invert Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Merge1maskInvert = param
    del param

    param = lastNode.createDoubleParam("Merge1mix", "Mix")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Merge1mix = param
    del param

    lastNode.userNatron = lastNode.createPageParam("userNatron", "User")
    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Node', 'Settings', 'Info', 'userNatron'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setScriptName("Output1")
    lastNode.setLabel("Output1")
    lastNode.setPosition(774, 552)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(561, 81)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Defocus"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Defocus")
    lastNode.setLabel("Defocus")
    lastNode.setPosition(573, 297)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupDefocus = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(0.5, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("// iChannel0: Source (Source image.), filter=linear, wrap=clamp\n// iChannel1: zDepth (Source image.), filter=linear, wrap=clamp\n\n#define USE_MIPMAP\n#define GOLDEN_ANGLE 2.39996323\n\n\nuniform int pSamples = 256; // Samples, min=64, max=1024\nuniform float pAmount = 1.0; // Blur radius, min=0.0, max=100.0 \nuniform float pContrast = 1.0; // Image Contrast, min=0.1, max=10.0 \n\nmat2 rot = mat2(cos(GOLDEN_ANGLE), sin(GOLDEN_ANGLE), -sin(GOLDEN_ANGLE), cos(GOLDEN_ANGLE));\n\n//-------------------------------------------------------------------------------------------\nvec3 Bokeh(sampler2D tex, vec2 uv, float radius, float amount)\n{\n    vec3 acc = vec3(0.0);\n    vec3 div = vec3(0.0);\n    vec2 pixel = (1.0 / iResolution.xy) * iRenderScale.xy;\n    float r = 1.0;\n    vec2 vangle = vec2(0.0,radius); \n    amount += radius*500.0;\n    \n\tfor (int j = 0; j < pSamples; j++)\n    {  \n        r += 1. / r;\n\tvangle = rot * vangle;\n        \n        #ifdef USE_MIPMAP\n\tvec3 col = texture2D(tex, uv + pixel * (r-1.) * vangle, radius*1.25).xyz;\n        #else\n        vec3 col = texture2D(tex, uv + pixel * (r-1.) * vangle).xyz;\n        #endif\n        col *= pContrast; \n\tvec3 bokeh = pow(col, vec3(9.0)) * amount+.4;\n\tacc += col * bokeh;\n\tdiv += bokeh;\n\t}\n\treturn acc / div;\n}\n\n//-------------------------------------------------------------------------------------------\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n    \n    vec2 uv = fragCoord.xy / iResolution.xy;\n\n    vec4 inpMask = texture2D( iChannel1, uv);\n\n    float bokehSize = mix(0.0,inpMask.a,pAmount);\n    \n    float r = (.8 - .8*cos(0.5 * 6.283))*bokehSize;\n       \n    float a = 40.0;\n    \n    uv *= vec2(1.0, 1.0);\n\n    fragColor = vec4(Bokeh(iChannel0, uv, r, a), 1.0);\n    \n    \n}")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("Linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("Clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputHint0")
    if param is not None:
        param.setValue("Source image.")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("Linear")
        del param

    param = lastNode.getParam("wrap1")
    if param is not None:
        param.set("Clamp")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("zDepth")
        del param

    param = lastNode.getParam("inputHint1")
    if param is not None:
        param.setValue("Source image.")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("pAmount")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Blur radius")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(100, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("pContrast")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Image Contrast")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0.1000000014901161, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("pSamples")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Samples")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(256, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(64, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(1024, 0)
        del param

    del lastNode
    # End of node "Defocus"

    # Start of node "ZDepth"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("ZDepth")
    lastNode.setLabel("ZDepth")
    lastNode.setPosition(19, 75)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupZDepth = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "ZDepth"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(774, 285)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(819, 95)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(1015, 297)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Mask"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(19, 297)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

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

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("A.a")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "White"
    lastNode = app.createNode("net.sf.openfx.ConstantPlugin", 1, group)
    lastNode.setScriptName("White")
    lastNode.setLabel("White")
    lastNode.setPosition(308, 85)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupWhite = lastNode

    param = lastNode.getParam("color")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        param.setValue(1, 3)
        del param

    del lastNode
    # End of node "White"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(308, 285)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("multiply")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("multiply")
        del param

    del lastNode
    # End of node "Merge2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupMerge1)
    groupDefocus.connectInput(0, groupSource)
    groupDefocus.connectInput(1, groupMerge2)
    groupMerge1.connectInput(0, groupDot1)
    groupMerge1.connectInput(1, groupDefocus)
    groupMerge1.connectInput(2, groupMask)
    groupDot1.connectInput(0, groupSource)
    groupShuffle1.connectInput(0, groupZDepth)
    groupShuffle1.connectInput(1, groupZDepth)
    groupMerge2.connectInput(0, groupWhite)
    groupMerge2.connectInput(1, groupShuffle1)

    param = groupDefocus.getParam("paramValueFloat0")
    group.getParam("DefocusparamValueFloat0").setAsAlias(param)
    del param
    param = groupDefocus.getParam("paramValueFloat1")
    group.getParam("DefocusparamValueFloat1").setAsAlias(param)
    del param
    param = groupDefocus.getParam("paramValueInt2")
    group.getParam("DefocusparamValueInt2").setAsAlias(param)
    del param
    param = groupMerge1.getParam("maskInvert")
    group.getParam("Merge1maskInvert").setAsAlias(param)
    del param
    param = groupMerge1.getParam("mix")
    group.getParam("Merge1mix").setAsAlias(param)
    del param
    param = groupMerge1.getParam("enableMask_Mask")
    group.getParam("Merge1enableMask_Mask").setAsAlias(param)
    del param
    param = groupMerge1.getParam("maskChannel_Mask")
    group.getParam("Merge1maskChannel_Mask").setAsAlias(param)
    del param
    param = groupShuffle1.getParam("outputA")
    group.getParam("Shuffle1outputA").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["DefocusExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
