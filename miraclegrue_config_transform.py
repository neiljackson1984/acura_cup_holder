import hjson
import math

def transformMiraclegrueConfig(config: dict):
    try:  
        del config['baseLayer']
    except:
        pass   
    # the baseLayer propery is not part of the official miraclegrue config schema, but makerbot print tends to insert it anyway.    
    
    config['layerHeight'] = 0.2
    config['modelFillProfiles']['sparse']['density'] = 0.5

    
    # To get from the default miraclgrue config to the result of setting baseLayer=paddedBase in the MAkerbot Print ui:
    if True:
        config['baseLayer'] = "paddedBase" # this property is not present in the default miraclegrue config
        config['doPaddedBase'] = True
        config['doRaft'] = False
        
        config['floorSolidLayerCount'] = 2
        config['floorSurfaceLayerCount'] = 2
        config['floorSurfaceThickness'] = 0.2
        config['floorThickness'] = 0.2

        config['modelFillProfiles']['base_layer_surface']['doExternalSpurs'] = True
        config['modelFillProfiles']['base_layer_surface']['doInternalSpurs'] = True
        config['modelFillProfiles']['base_layer_surface']['extrusionWidth'] = 2.5
        config['modelFillProfiles']['base_layer_surface']['firstShellOffset'] = 0
        config['modelFillProfiles']['base_layer_surface']['linearFillGroupDensity'] = 2
        config['modelFillProfiles']['base_layer_surface']['linearFillGroupSize'] = 2.5
        
        
        config['modelShellProfiles']['base_layer_surface']['doExternalSpurs'] = True
        config['modelShellProfiles']['base_layer_surface']['doInternalSpurs'] = True
        config['modelShellProfiles']['base_layer_surface']['extrusionWidth'] = 2.5
        config['modelShellProfiles']['base_layer_surface']['firstShellOffset'] = 0
        config['modelShellProfiles']['base_layer_surface']['infillShellSpacingMultiplier'] = 0.0

        config['paddedBaseWidth'] = 2.5
        config['raftModelShellsSpacing'] = 0.0
        config['raftModelSpacing'] = 0.0

        config['supportFillProfiles']['base_layer_surface']['doExternalSpurs'] = True
        config['supportFillProfiles']['base_layer_surface']['doInternalSpurs'] = True
        config['supportFillProfiles']['base_layer_surface']['extrusionWidth'] = 2.5
        config['supportFillProfiles']['base_layer_surface']['firstShellOffset'] = 0
        config['supportFillProfiles']['base_layer_surface']['linearFillGroupDensity'] = 2
        config['supportFillProfiles']['base_layer_surface']['linearFillGroupSize'] = 2.5
        
        config['supportFloorSolidLayerCount'] = 2
        config['supportFloorSurfaceLayerCount'] = 2

        config['supportShellProfiles']['base_layer_surface']['extrusionWidth'] = 2.5

    #undo the floor thickness changes that were don above as part of padded base.
    config['floorSurfaceThickness'] = 0.8
    config['floorThickness'] = 0.8

    config['doRaft'] = False
    config['bedZOffset'] = - config['layerHeight'] + 0.04

    config['doFixedShellStart'] = False
    
    #support:
    config['doBreakawaySupport'] = True
    config['doSupport'] = True
    config['doSupportUnderBridges'] = True
    config['supportBreakawayModelRoofSpacing'] = 0.16
    config['supportCutout'] = 0.1
    config['supportCutoutExtraDistance'] = 0.6
    config['supportFillProfiles']['base_layer_surface']['consistentOrder'] = True
    config['supportFillProfiles']['base_layer_surface']['density'] = 0.16
    config['supportFillProfiles']['base_layer_surface']['orientationOffset'] = 45
    config['supportFillProfiles']['solid']['density'] = 0.32
    config['supportFillProfiles']['solid']['orientationOffset'] = 45
    config['supportFillProfiles']['solid']['pattern'] = "hilbert_fill"
    config['supportFillProfiles']['sparse']['consistentOrder'] = True
    config['supportFillProfiles']['sparse']['density'] = 0.16
    config['supportFillProfiles']['sparse']['orientationOffset'] = 45
    config['supportRoofSolidThickness'] = 3.0
    config['supportType'] = "breakaway"

    config['extruderProfiles'][0]['extrusionProfiles']['base_layer_surface']['fanSpeed'] = 0
    config['extruderProfiles'][0]['extrusionProfiles']['base_layer_surface']['feedrate'] = min(config['extruderProfiles'][0]['extrusionProfiles']['base_layer_surface']['feedrate'], 15) 

    config['modelShellProfiles']['base_layer_surface']['numberOfShells'] = 3
    config['modelShellProfiles']['extent']['numberOfShells'] = 3

    return config


    
